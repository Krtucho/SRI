import sympy
import math
from abstract_model import Model
from component import Component
from bool_alg_op import BooleanAlgOp

class Fuzzy_model(Model):

    def __init__(self,documents):
        self.documents=documents
        self.tokens_list = self.load_documents(documents)
        self.correl_matrix=None
        self.query_term=None
        self.mui_i_j=None
        self.q_fnd=None
        self.q_fndc=None
        self.class_BooleanAlgOp=None

    
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
        self.mui_i_j=self.fuzzy_set_associated_with_doc()
        
        result = []
        result_without_number=[]
        for i, token in enumerate(query):
            if token == "or":
                result.append("|")
                result_without_number.append("|")
            elif token =="and":
                result.append("&")
                result_without_number.append("&")
            elif token=="not":
                result.append("~")
                result_without_number.append("~")
            elif token.isnumeric():
                result.append(token)
                result_without_number.append("a"+token)
            else:
                result.append(token)
                result_without_number.append(token)

            if i == len(query) - 1:
                continue
            if not(query[i] in ("and", "or", "not")) and not query[i+1] in ("and", "or", "not"):
                result.append("&")
                result_without_number.append("&")


        string = " "
        fnd_without_number=sympy.to_dnf(string.join(result_without_number))

        self.q_fnd=string.join(self.parser_number(fnd_without_number))
        
        self.class_BooleanAlgOp=BooleanAlgOp(self.q_fnd)
        self.q_fndc = BooleanAlgOp.process_and_get_fndc(self.q_fnd, query_term=query_term)
        
        return result

    def parser_number(self,fnd):
        list=str(fnd).split(" ")
        new_fnd=[]
        for item in list:
            if item[0] =="(":
                new_fnd.append(item[0])
                string=item[1:]
                if len(string)>1 and string[0]== "a" and string[1:].isnumeric():
                    new_fnd.append(string[1:])
                else:
                    new_fnd.append(string)
            elif len(item)>1 and item[-1:]==")":
                string=item[:(len(item)-1)]
                if len(string)>1 and string[0]== "a" and string[1:].isnumeric():
                    new_fnd.append(string[1:])
                else:
                    new_fnd.append(string)
                new_fnd.append(")")
            elif len(item)>1 and item[0]== "a" and item[1:].isnumeric():
                new_fnd.append(item[1:])
            else:
                new_fnd.append(item)
            
        return new_fnd

    def correlation_matrix(self, query):
        corr_matrix={}

        for term_i in query:
            for term_j in query:
                if term_i in self.tokens_list and term_j in self.tokens_list:
                    n_i_j = len(set(self.tokens_list[term_i]).intersection(set(self.tokens_list[term_j])))
                    n_i = len(self.tokens_list[term_i])
                    n_j = len(self.tokens_list[term_j])
                    corr_matrix[(term_i,term_j)] = round(n_i_j / (n_i + n_j - n_i_j),5)
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
                            mult_kterm_doc*=round(1 - self.correl_matrix[(term,self.query_term[k])],5)
                    
                    fuzzy_doc[(term,doc)]=round(1 - mult_kterm_doc,5)


        return fuzzy_doc


    def ranking_function(self, doc):
        index_literal=self.class_BooleanAlgOp.components_dict

        cc_p=1
        for literal in self.q_fndc.keys():
            literal_list = literal.split(" ")
            miu_cc_i_j=1
            for item,index in index_literal.items():
                if literal_list[index]:
                    miu_cc_i_j *= self.mui_i_j[(item,doc)]
                else:
                    miu_cc_i_j *= (1 - self.mui_i_j[(item,doc)])
            cc_p *= (1 - miu_cc_i_j)

        return float(1-self.truncate(cc_p, 3))

    def truncate(self,num, n):
        integer = int(num * (10**n))/(10**n)
        return float(integer)
    # def truncateB(self, number: float, max_decimals: int) -> float:
    #     int_part, dec_part = str(number).split(".")
    #     return float(".".join((int_part, dec_part[:max_decimals])))
    
    
