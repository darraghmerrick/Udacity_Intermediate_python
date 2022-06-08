import random
import os
import requests
from QuoteEngine import ingestor
from  MemeEngine import MemeEngine
from flask import Flask, render_template, abort, request

# @TODO Import your Ingestor and MemeEngine classes

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    quotes_directory = './_data/DogQuotes/'
    for file in os.listdir(quotes_directory):
        quotes.append(ingestor.parse(f'{quotes_directory}/{file}'))
    
    imgs = []
    images_path = "./_data/photos/dog/"
    for file in os.listdir(images_path):
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
