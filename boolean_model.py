
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
        pass
        