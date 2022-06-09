import pandas
from ..IngestorInterface import IngestorInterface
from ..QuoteModel import QuoteModel
from typing import List



class CsvIngestor(IngestorInterface):

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
     
    allowed_extensions = ['csv']   
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the .csv file to extract quotes.
        
        Instantiate QuoteModel objects for each quote.
        Return list of all QuoteModel Objects created from the file.
        :param path: the file path to be parsed.
        """
        try:
            if not cls.can_ingest(path):
                raise Exception('cannot ingest file')

            quotes = []
            df = pandas.read_csv(path)

            for row in df.iterrows():
                quote = QuoteModel(row['body'], row['author'])
                quotes.append(quote)

            return quotes
        except Exception:
            raise Exception('Error parsing file')
