'''
A Python class that defines a QuoteModel object, 
which contains text fields for body and author. 
The class overrides the correct methods to instantiate the class,
prints the model contents as: ”body text” - author
'''

class QuoteModel():

    def __init__(self, quote, author):
    
        self.body = quote
        self.author = author

    def __str__(self):

        return self.body + " - " + self.author