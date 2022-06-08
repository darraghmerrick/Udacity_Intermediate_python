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
        