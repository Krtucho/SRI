from abstract_model import Model

class Boolean_model(Model):

    def __init__(self, documents):
        self.documents=documents
        self.tokens_list = self.load_documents(documents)

    def load_documents(self, documents)-> dict: # Asumo que documents es un array de documentos de tipo doc
        tokens_list = {}

        for doc in documents: 
            tokens = set(doc.term)
            for token in tokens:
                if not token in tokens_list:
                    tokens_list[token] = [doc]
                else:
                    tokens_list[token].append(doc)

        return tokens_list

    # def load_documents(self, documents)-> dict: # Asumo que documents es un array de documentos de tipo doc
    #     tokens_list = {}

    #     for doc in documents:
    #         tokens = set(doc.text)
    #         for token in tokens:
    #             if not tokens_list.__contains__(token):
    #                 tokens_list[token] = [doc]
    #             else:
    #                 tokens_list[token].append(doc)

    #     print(tokens_list)

    #     return tokens_list


    def load_query(self, query):
        result = []
        for i, token in enumerate(query):
            result.append(token)
            if i == len(query) - 1:
                continue
            if not(query[i] in ("and", "or", "not")) and not query[i+1] in ("and", "or", "not"):
                result.append("and")

        return result
    def similitud(self, query):
        token_list=self.tokens_list
        result=set()
        # result=None

        if query[0] == "not":
            if query[1] in token_list:
                result=set(self.documents).difference(set(token_list[query[1]]))
            else:
                result=set(self.documents)
        else:
            if query[0] in token_list:
                result=set(token_list[query[0]])
        
        for i, token in enumerate(query): # Procesando or

            if token == "or":
                if query[i+1] == "not":
                    if query[i+2] in token_list:
                        result=result.union((set(self.documents)).difference(set(token_list[query[i+2]])))
                    else:
                        result=result.union(set(self.documents))
                else:
                    if query[i+1] in token_list:
                        result=result.union(set(token_list[query[i+1]]))
                        
            elif token == "and":
                if query[i+1] == "not":
                    if query[i+2] in token_list:
                        result=result.intersection(set(self.documents).difference(set(token_list[query[i+2]])))
                    else:
                        result=result.intersection(set(self.documents))
                else:
                    if query[i+1] in token_list:
                        result=result.intersection(set(token_list[query[i+1]]))
                    else:
                        result=set()

        if result.__len__() == 0:
            return []
        return result
    
    
    # Me devuelve los k doc con mayor similitud con respecto a una query
    def k_doc_best_similitud(self,query,k):
        similitud_dic =[]
        for doc in self.similitud(query):
            similitud_dic.append(doc.title)
        #sortedDictWithValues = dict(sorted(similitud_dic.items(), key=lambda x: x[1], reverse=True)) 
        #similitud_dic = sortedDictWithValues       
        return similitud_dic[0:k]
        
    
    def Presicion(self,cran_querys,dict_querys):
        presicion  = []
        Relevantes_q = []
        for q in dict_querys.keys():
            Relevantes_q = cran_querys[q].split()
            Recuperados = dict_querys[q].__len__()
            RRecuperados_q= intersection(Relevantes_q,dict_querys[q])
            if RRecuperados_q and Recuperados:
                presicion.append(RRecuperados_q/Recuperados)
            else:
                presicion.append(0)    
        return presicion
     
    
     
    def Recobrado (self,cran_querys,dict_querys):
        recobrado  = []
        Relevantes_q = []
        for q in dict_querys.keys():
            Relevantes_q = cran_querys[q].split()
            Recuperados = dict_querys[q]
            RRecuperados_q= intersection(Relevantes_q,Recuperados)
            NR = Relevantes_q.__len__() - RRecuperados_q
            if RRecuperados_q and (RRecuperados_q + NR):
                recobrado.append(RRecuperados_q/(RRecuperados_q + NR))
            else:
                recobrado.append(0) 
        return recobrado
 
    # Medida F1
    def f1(self,p, r):
        f1 = []
        for i in range(0,len(p)):
            pi,ri = 0,0
            if(p[i]!=0):
                pi = 1/p[i]
            if(r[i]!=0):
                ri = 1/r[i]
            d = pi + ri
            if d!= 0:
                f1.append( 2/d)
            else:
                f1.append(0.0)    
        return f1
    
def intersection(x, y):
    z = [value for value in x if value in y]
    return len(z)



