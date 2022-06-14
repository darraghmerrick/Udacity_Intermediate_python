'''
ingester_interface
The project contains an abstract base class, IngestorInterface, which defines:
A complete classmethod method to verify if the file type is compatible with the ingestor class.
An abstract method for parsing the file content
(i.e., splitting each row) and outputting it to a Quote object.
There is a class defined to support each supported file type:
text, docx, pdf,csv
'''
from typing import List
from abc import ABC, abstractmethod
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass