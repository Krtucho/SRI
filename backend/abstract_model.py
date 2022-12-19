from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def load_documents(self,documents):
        pass
    def load_query(self,query):
        pass
    
    def set_tokens_list(self, new_tokens_list, documents):
        self.documents = documents
        self.token_list = new_tokens_list
     
    def load_many_documents(self, documents)-> dict: # Asumo que documents es un array de documentos de tipo doc
        tokens_list = {}

        for doc in documents: 
            tokens = set(doc.term)
            for token in tokens:
                if not token in tokens_list:
                    tokens_list[token] = [doc]
                else:
                    tokens_list[token].append(doc)

        return tokens_list