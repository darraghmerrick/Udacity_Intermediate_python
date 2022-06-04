from abc import ABC, abstractmethod
# abc is a builtin module, we have to import ABC and abstractmethod

class IngestorInterface(ABC): # Inherit from ABC(Abstract base class)
    @property
    @abstractmethod  # Decorator to define an abstract method
    def file_types(self):
        pass
    
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass

    def can_ingest(self, path):
        #extension = path.split('.')[-1]
        #if extension == self.supported_file_type:
        #    return True
        #return False