import random
import os
import requests
from QuoteEngine.ingestor import Ingestor
from MemeEngine import MemeEngine
from flask import Flask, render_template, abort, request

# @TODO Import your Ingestor and MemeEngine classes

app = Flask(__name__)

# meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./Engines/_data/DogQuotes/DogQuotesTXT.txt',
                   './Engines/_data/DogQuotes/DogQuotesDOCX.docx',
                   './Engines/_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    for file in quote_files:
        list = Ingestor.parse(file)
        for item in list:
            quotes.append(item)

    images_path = "./Engines/_data/photos/dog/"
    imgs = []
    files = os.listdir(images_path)
    for file in files:
        if file.split('.')[-1] == 'jpg':
            imgs.append(file)
    return quotes, imgs


quotes, imgs = setup()

@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = "./_data/photos/dog/" + random.choice(imgs)
    quote = random.choice(quotes)[0]

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    try:
        img = requests.get(request.form['image_url'])
        with open('./static/download.png', 'wb') as f:
            f.write(img.content)
            quote_body = request.form['body']
            quote_author = request.form['author']
            path = meme.make_meme('./static/download.png',
                                  quote_body, quote_author)

        os.remove('./static/download.png')
        
    except Exception:
            raise Exception('Error posting meme')
    path = ''

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
