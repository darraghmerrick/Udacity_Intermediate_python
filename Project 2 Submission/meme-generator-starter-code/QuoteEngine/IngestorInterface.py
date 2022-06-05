'''
ingester_interface
The project contains an abstract base class, IngestorInterface, which defines:
A complete classmethod method to verify if the file type is compatible with the ingestor class.
An abstract method for parsing the file content
(i.e., splitting each row) and outputting it to a Quote object.
There is a class defined to support each supported file type:
text, docx, pdf,csv
'''

from abc import ABC, abstractmethod
from ast import In
import pandas as pd
from docx import Document
import pdftotext
import QuoteModel
from typing import List
import os


class IngestorInterface(ABC):
    ''' Inherit from ABC(Abstract base class)
    Base class to be used by the supported file type ingestors'''
    @property
    @abstractmethod
    def file_types(self):
        '''Returns the filetype from supported ingestor'''
        
    @abstractmethod
    def parse(self, path: str):
        '''Parse the data from supported file '''

    def can_ingest(self, path):
        '''Checks that the file extensions is supported'''
    
    @property
    @abstractmethod
    def supported_file_type(self):
        """Return doc type supported by ingestor."""

    def can_parse(self, path):
        """Return boolean value after testing whether
        or not the Ingestor can handle the file type"""
        # this will return a tuple of root and extension
        split_tup = os.path.splitext(path)
        print(split_tup)
        # extract the file name and extension
        file_name = split_tup[0]
        file_extension = split_tup[1]
        file_extension = file_extension[1:]
        print("File Name: ", file_name)
        print("File Extension: ", file_extension)
        if file_extension == self.supported_file_type:
            return True
        return False

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

class CSVIngestor(IngestorInterface):
    '''
    The class inherits the IngestorInterface.
    The class depends on the pandas library to complete the defined, 
    abstract method signatures to parse CSV files.
    The parse method returns a valid QuoteModel
    '''
    @property
    def file_types(self):
        '''Return csv extension type'''
        return "csv"



