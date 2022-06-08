'''
A Python class that defines a QuoteModel object,
which contains text fields for body and author.
'''

class QuoteModel():
    '''The class overrides the correct methods to instantiate the class,
    prints the model contents as: ”body text” - author'''
    def __init__(self, quote, author):
        '''Initialize the Quote object'''
        self.body = quote
        self.author = author

    def __str__(self):
        '''String representation of the Quote'''
        return self.body + " - " + self.author
    def __len__(self):
        return self.body.item_count
