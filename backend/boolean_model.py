
class Boolean_model:

    def __init__(self, documents):
        self.documents=documents
        self.tokens_list = self.load_documents(documents)

    def load_documents(self, documents)-> dict: # Asumo que documents es un array de documentos de tipo doc
        tokens_list = {}

        for doc in documents:
            tokens = set(doc.term)
            for token in tokens:
                if not tokens_list.__contains__(token):
                    tokens_list[token] = [doc]
                else:
                    tokens_list[token].append(doc)

        #print(tokens_list)

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
        #print("Empieza el metodo")
        #print(query)
        #print(token_list)
        if query[0] == "not":
            temp = token_list.get(query[1])
            #if(temp!=None):
            result=set(self.documents).difference(set(temp))
        else:
            temp = token_list.get(query[0])
            #if(temp!=None):
            result=set(temp)
        
        #print(result)
        for i, token in enumerate(query): # Procesando or
            if token == "or":
                if query[i+1] == "not":
                    temp = token_list.get(query[i+2])
                    #if(temp!=None):
                    result=result.union((set(self.documents)).difference(set(temp)))
                else:
                    temp = token_list.get(query[i+1])
                    #if(temp!=None):
                    result=result.union(set(temp))
            elif token == "and":
                if query[i+1] == "not":
                    temp = token_list.get(query[i+2])
                    #if(temp!=None):
                    result=result.intersection(set(self.documents).difference(set(temp)))
                else:
                    #temp = token_list[query[i+1]]
                    temp = token_list.get(query[i+1])
                    #if(temp!=None):
                    result=result.intersection(set(temp))
            #print(result)

        #print("Resultado")
        #print(result)
        return result