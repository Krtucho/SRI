
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
        pass

    def similitud(self, query, token_list, documents):
            result=set(token_list[0])

            for i, token in enumerate(query): # Procesando or
                if token == "or":
                    if query[i+1] == "not":
                        result=result.union(set(documents).difference(set(token_list[i+2])))
                    else:
                        result=result.union(set(token_list[i+1]))
                elif token == "and":
                    if query[i+1] == "not":
                        result=result.intersection(set(documents).difference(set(token_list[i+2])))
                    else:
                        result=result.intersection(set(token_list[i+1]))
            return result
            