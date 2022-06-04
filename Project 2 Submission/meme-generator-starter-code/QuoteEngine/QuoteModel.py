
class QuoteModel():

    def __init__(self, quote, author):
    
        self.body = quote
        self.author = author

    def __str__(self):

        return self.body + " - " + self.author