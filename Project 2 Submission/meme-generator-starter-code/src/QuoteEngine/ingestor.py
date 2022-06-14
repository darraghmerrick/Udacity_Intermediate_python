"""All ingestors are packaged into a main Ingestor class.
This class encapsulates all the ingestors,
to provide one interface to load any supported file type."""

from typing import List
from .IngestorInterface import IngestorInterface
from .ingestors import DocxIngestor
from .ingestors import CsvIngestor
from .ingestors import PDFIngestor
from .ingestors import TextIngestor
from .QuoteModel import QuoteModel


class Ingestor():
    """Parser class which is the user interface for parsing files."""


    """Initialize list of available ingestors."""
    ingestors = [
            PDFIngestor,
            TextIngestor,
            DocxIngestor,
            CsvIngestor]
    
    @classmethod
    def parse(cls, path):
        """Find ingestor to parse file type and return list of quotes."""
        for ingestor in cls.ingestors:
            if ingestor.can_parse(path):
                return ingestor.parse(path)
        raise Exception(f"Parser not found for doc type {path.split('.')[-1]}")
        return []

    def __str__(self):
        """Human readable representation of ingestor."""
        file_types = []
        for p in self.ingestors:
            file_types.append(str(p))
        return f"Parser can handle the following doc types: {str(file_types)}"

