"""All ingestors are packaged into a main Ingestor class.
This class encapsulates all the ingestors,
to provide one interface to load any supported file type."""

from ..IngestorInterface import IngestorInterface
import DocxIngestor
import CsvIngestor
import PDFIngestor
import TextIngestor


class Ingestor(IngestorInterface):
    """Parser class which is the user interface for parsing files."""

    def __init__(self):
        """Initialize list of available ingestors."""
        self.ingestors = [
            PDFIngestor(),
            TextIngestor(),
            DocxIngestor(),
            CsvIngestor()]

    def parse(self, path):
        """Handles file requests and checks against supported ingestors"""
        for ingestor in self.ingestors:
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