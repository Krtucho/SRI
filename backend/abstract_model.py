from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def load_documents(self,documents):
        pass
    def load_query(self,query):
        pass