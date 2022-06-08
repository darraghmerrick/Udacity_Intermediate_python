class PDFIngestor(IngestorInterface):
    '''
    The PDFIngestor class inherits from the IngestorInterface class.
    The PDFIngestor class utilizes the subprocess module to call the pdftotext CLI utility,
    creating a pipeline that converts PDFs to text and then ingests the text.
    The class handles deleting temporary files.
    The parse method returns a valid QuoteModel
    '''
    @property
    def file_types(self):
        '''Return Docx extension type'''
        return "pdf"

