'''
IngesterInterface:
The project contains an abstract base class, IngestorInterface, which defines:
A complete classmethod method to verify if the file type is compatible with the ingestor class.
An abstract method for parsing the file content
(i.e., splitting each row) and outputting it to a Quote object.
There is a class defined to support each supported file type:
Text, Docx, Pdf,Csv
'''

from abc import ABC, abstractmethod
from ast import In
import pandas as pd


class IngestorInterface(ABC): # Inherit from ABC(Abstract base class)
    @property
    @abstractmethod  # Decorator to define an abstract method
    def file_types(self):
        pass
    
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass

    def can_ingest(self, path) -> boolean:
        pass

class TextIngestor(IngestorInterface):
    '''
    The class inherits the IngestorInterface.
    The class does not depend on any 3rd party library to complete the defined,
    abstract method signatures to parse Text files.
    The parse method returns a valid QuoteModel
    '''
    def file_types(self):

class DocxIngestor(IngestorInterface):
    '''
    The class inherits from the IngestorInterface class.
    The class depends on the python-docx library to complete the defined,
    abstract method signatures to parse DOCX files.
    The parse method returns a valid QuoteModel
    '''

class PDFIngestor(IngestorInterface):
    '''
    The project contains a PDFIngestor class.
    The PDFIngestor class inherits from the IngestorInterface class.
    The PDFIngestor class utilizes the subprocess module to call the pdftotext CLI utility,
    creating a pipeline that converts PDFs to text and then ingests the text.
    The class handles deleting temporary files.
    The parse method returns a valid QuoteModel
    '''

class CSVIngestor(IngestorInterface):
    '''
    The class inherits the IngestorInterface.
    The class depends on the pandas library to complete the defined, 
    abstract method signatures to parse CSV files.
    The parse method returns a valid QuoteModel
    '''



