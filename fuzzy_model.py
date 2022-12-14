from abstract_model import Model

class Fuzzy_model(Model):

    def __init__(self,documents):
        self.documents=documents
        self.tokens_list = self.load_documents(documents)
        self.correl_matrix=None
        self.query_term=None
        self.fuzzy_set_doc=None

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

    def load_query(self, query):
        query_term=[]
        for term in query:
            if term !="not" and term != "and" and term != "or" and not term in query_term:
                query_term.append(term)

        self.query_term=query_term
        self.correl_matrix=self.correlation_matrix(query_term)
        # corr_matrix={}
        # corr_matrix[(query_term[0],query_term[0])]=1
        # corr_matrix[(query_term[0],query_term[1])]=0.6
        # corr_matrix[(query_term[0],query_term[2])]=0.4

        # corr_matrix[(query_term[1],query_term[0])]=0.6
        # corr_matrix[(query_term[1],query_term[1])]=1
        # corr_matrix[(query_term[1],query_term[2])]=0.75

        # corr_matrix[(query_term[2],query_term[0])]=0.4
        # corr_matrix[(query_term[2],query_term[1])]=0.75
        # corr_matrix[(query_term[2],query_term[2])]=1

        # self.correl_matrix=corr_matrix


        self.fuzzy_set_doc=self.fuzzy_set_associated_with_doc()
        
        result = []
        for i, token in enumerate(query):
            result.append(token)
            if i == len(query) - 1:
                continue
            if not(query[i] in ("and", "or", "not")) and not query[i+1] in ("and", "or", "not"):
                result.append("and")

        return result

    def correlation_matrix(self, query):
        corr_matrix={}

        for term_i in query:
            for term_j in query:
                # n_i = 0
                # n_j =0
                if term_i in self.tokens_list and term_j in self.tokens_list:
                    n_i_j = len(set(self.tokens_list[term_i]).intersection(set(self.tokens_list[term_j])))
                    n_i = len(self.tokens_list[term_i])
                    n_j = len(self.tokens_list[term_j])
                    corr_matrix[(term_i,term_j)] = n_i_j / (n_i + n_j - n_i_j)
                # elif term_i in self.tokens_list:
                #     n_i_j = len(self.tokens_list[term_i])
                #     n_i = n_i_j
                #     corr_matrix[(term_i,term_j)] = n_i_j / (n_i + n_j - n_i_j)
                # elif term_j in self.tokens_list:
                #     n_i_j = len(self.tokens_list[term_j])
                #     n_j = n_i_j
                #     corr_matrix[(term_i,term_j)] = n_i_j / (n_i + n_j - n_i_j)
                else:
                    corr_matrix[(term_i,term_j)] = 0
        
        return corr_matrix
                    
    def fuzzy_set_associated_with_doc(self):
        fuzzy_doc={}
        
        for doc in self.documents:
            for i in range(0,len(self.query_term)):
                term=self.query_term[i]
                if not (term,doc) in fuzzy_doc.keys():
                    mult_kterm_doc=1
                    for k in range(0,len(self.query_term)):
                        if self.query_term[k] in doc.term_frec:
                            mult_kterm_doc*=(1 - self.correl_matrix[(term,self.query_term[k])])
                    
                    fuzzy_doc[(term,doc)]= 1 - mult_kterm_doc

        return fuzzy_doc

    def ranking_function(self):
        pass
                

    
    
