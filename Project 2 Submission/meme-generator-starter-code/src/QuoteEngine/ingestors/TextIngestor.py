class TextIngestor(IngestorInterface):
    '''
    The class inherits the IngestorInterface.
    The class does not depend on any 3rd party library to complete the defined,
    abstract method signatures to parse Text files.
    The parse method returns a valid QuoteModel
    '''
    @property
    def file_types(self):
        '''Return txt extension type'''
        return "txt"
    