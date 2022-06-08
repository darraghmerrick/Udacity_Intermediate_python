class DocxIngestor(IngestorInterface):
    '''
    The class inherits from the IngestorInterface class.
    The class depends on the python-docx library to complete the defined,
    abstract method signatures to parse DOCX files.
    The parse method returns a valid QuoteModel
    '''
    @property
    def file_types(self):
        '''Return Docx extension type'''
        return "docx"
