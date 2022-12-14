import math 
from abstract_model import Model
from query import Load_Query, Clear_Query
from parse_cran import Parse_Cranqrel

class Vector_Model(Model):
    def __init__(self,documents):
        self.documents=documents
        self.tokens_list = self.load_documents(documents)
        self.q_weights=None
        self.doc_weights=None

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

    def load_query(self,query):
        self.doc_weights=self.docs_weights(query)
        self.q_weights=self.query_weights(query)

#metodo que calcula la frecuencia normalizada de la consulta
    def freq_normal_q(self, query):
        term_freq={}
        max_freq=-1
        for t in query:
            if t in term_freq:
                term_freq[t] +=1
            else: 
                term_freq[t] = 1
            if max_freq < term_freq[t]:
                max_freq = term_freq[t]
        for f in term_freq:
            term_freq[f] /= max_freq  
        return term_freq


#metodo que calcula la frecuencia normalizada de los documentos
    def freq_normal(self, query):
        freq_normal_term_docs={}

        for doc in self.documents:
            for term in query:
                if term in doc.term:
                    freq_normal_term_docs[(term,doc)] = doc.term_frec[term]
                else:
                    freq_normal_term_docs[(term,doc)] = 0

        return freq_normal_term_docs

    def idf(self,query):
        idf_i={}
        docs_count=len(self.documents)
        for term in query:
            if term in self.tokens_list:
                idf_i[term]=math.log(docs_count/len(self.tokens_list[term]),10)
            else:
                idf_i[term]=0
        return idf_i

    def similitud(self, query, doc):

        q_weights = self.q_weights
        doc_weights = self.doc_weights

        sum_weights_total=0
        sum_cuadrado_doc_weights=0
        sum_cuadrado_q_weights=0

        for term in query:
            if term in doc.term_frec:
                sum_weights_total += doc_weights[(term,doc)] * q_weights[term]
                sum_cuadrado_doc_weights += pow(doc_weights[(term,doc)], 2)
                sum_cuadrado_q_weights += pow(q_weights[term], 2)
            else:
                sum_weights_total += 0
                sum_cuadrado_doc_weights += 0
                sum_cuadrado_q_weights += pow(q_weights[term], 2)
        if sum_cuadrado_doc_weights==0 or sum_cuadrado_q_weights==0:
            return 0
            
        sim_doc_q=sum_weights_total / (math.sqrt(sum_cuadrado_doc_weights) * math.sqrt(sum_cuadrado_q_weights))
        return sim_doc_q

    # pesos en los documentos
    def docs_weights(self, query):

        freq_nor = self.freq_normal(query)
        idf_i = self.idf(query)

        doc_weights={}
        for term,doc in freq_nor.keys():
            doc_weights[(term,doc)]=freq_nor[(term,doc)] * idf_i[term]
        return doc_weights
            
    # pesos en las consultas
    def query_weights(self, query):

        freq_nor_q = self.freq_normal_q(query)
        idf_i = self.idf(query)

        q_weights={}
        for term in query:
            q_weights[term]=( 0.5 + (1 - 0.5) * freq_nor_q[term] ) * idf_i[term]
        
        return q_weights

    # Me devuelve los k doc con mayor similitud con respecto a una query
    def k_doc_best_similitud(self,query,k):
        similitud_dic ={}
        for doc in self.documents:
            similitud = self.similitud(query, doc)
            if(similitud >0.0):
                similitud_dic[doc.title] = similitud
        sortedDictWithValues = dict(sorted(similitud_dic.items(), key=lambda x: x[1], reverse=True)) 
        similitud_dic = sortedDictWithValues       
        return list(similitud_dic.keys())[0:k]
        
    
    def Presicion(self,cran_querys,dict_querys):
        presicion  = []
        Relevantes_q = []
        for q in dict_querys.keys():
            Relevantes_q = cran_querys[q].split()
            Recuperados = dict_querys[q].__len__()
            RRecuperados_q= intersection(Relevantes_q,dict_querys[q])
            presicion.append(RRecuperados_q/Recuperados)
        
        return presicion
     
    
     
    def Recobrado (self,cran_querys,dict_querys):
        recobrado  = []
        Relevantes_q = []
        for q in dict_querys.keys():
            Relevantes_q = cran_querys[q].split()
            Recuperados = dict_querys[q]
            RRecuperados_q= intersection(Relevantes_q,Recuperados)
            NR = Relevantes_q.__len__() - RRecuperados_q
            recobrado.append(RRecuperados_q/(RRecuperados_q + NR))
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
    
 # Cant element comunes entre dos list
def intersection(x, y):
    z = [value for value in x if value in y]
    return len(z)

   