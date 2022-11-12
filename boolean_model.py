
from asyncio import QueueEmpty
from turtle import right


class Boolean_model:

    def __init__(self):
        self.tokens_list = {}

    def load_documents(self, documents)-> dict: # Asumo que documents es un array de documentos de tipo doc
        tokens_list = {}

        for doc in documents:
            tokens = set(documents.text)
            for token in tokens:
                if not tokens_list.__contains__(token):
                    tokens_list[token] = [doc]
                else:
                    tokens_list[token].append(doc)

        return tokens_list


    def load_query(self, query):
        result = []
        for i, token in enumerate(query):
            result.append(token)
            if i == len(query) - 1:
                continue
            if not(query[i] in ("and", "or", "not")) and not query[i+1] in ("and", "or", "not"):
                result.append("and")

        return result

    def similitud(self, query, token_list):
        result = []

        for i, token in enumerate(query): # Procesando or
            if token == "or":
                left = query[i-1]
                right = query[i+1]
                if right == "not":
                    pass # aplicar not
                else:
                    docs = set(token_list[left]).union(set(token_list[right]))
                    result.append(docs)

        for i, token in enumerate(query): # Procesando and
            if token == "and":
                left = query[i-1]
                right = query[i+1]
                if right == "not":
                    pass # aplicar not
                else:
                    docs = set(token_list[left]).intersection(set(token_list[right]))
                    result.append(docs)

        for i, token in enumerate(query): # Procesando not
            if token == "not":
                left = query[i-1]
                right = query[i+1]
                if left == "and" or left == "or":
                    continue # Ya se analizo en los casos de and y or
                else:
                    docs = set(token_list[left]).difference(set(token_list[right]))
                    result.append(docs)
        
        documents = set()
        for item in result:
            documents = documents.intersection(item)

        return documents # Me queda la duda sobre que devolver exactamente, xq podemos aplicarle interseccion a todos los documentos de result por ejemplo 
                      # y eso se supone que te de todos los documentos comunes que cumplen ciertas cosas. Actualmente devolviendolo asi, estariamos
                      # aplicando la union