# from boolean_model import Boolean_model
# from vector_model import Vector_model
# from fuzzy_model import Fuzzy_model
# from query import Clear_Query
# from parse import All_Dir_Doc,Create_Data
# from documents import Doc
import time
# import sympy
from component import Component
from bool_alg_op import BooleanAlgOp

# cwd = os.getcwd()
    
#     file = open(os.path.join(cwd,"Data_Cran","rel.txt"), "w")

def main():

    # dir_docs,ids = All_Dir_Doc()  # contiene las direcciones de todos los doc y su id la pos en que estos se encuentran en estos es la misma que en data
    
    # inicio=time.time()
    
    # data = Create_Data(dir_docs,ids)
    
    # fin=time.time()
    # print("El tiempo en crear la data")
    # print(fin-inicio)

    # data=[]
    # doc1= Doc("doc1","hola",["tiger","dog"])
    # data.append(doc1)
    # doc2= Doc("doc2","hola1",["leon","leon","leon","zorro"])
    # data.append(doc2)
    # doc3= Doc("doc3","hola2",["leon","zorro","nutria"])
    # data.append(doc3)
    # doc4= Doc("doc4","hola3",["leon","leon","leon","zorro","zorro","zorro"])
    # data.append(doc4)
    # doc5= Doc("doc5","hola4",["nutria"])
    # data.append(doc5)

    # modelo=Fuzzy_model(data)
        
    # while(True):
        
    #     print("Welcome, Please enter your query")
    #     query_text = input()

    # query_text="shdkjfbdj kjdj"
    # query_text="leon zorro nutria"
    # query_text="lion and tiger tiger tiger be only you and never forget it forget it 2017"
    query_text="(forget & 2017) | tiger "
    
    q_fndc = BooleanAlgOp.process_query_and_get_fndc(query_text)
    # q_fnd = BooleanAlgOp.get_fndc(3, query_text,['forget', '2017', 'tiger'])
    # q_fnd=sympy.to_dnf((query_text))
    
    print(q_fndc)
        # if(query_text == "exit"):
        #     break
    # query_text="lion and tiger or tiger or not dog"

    # query = Clear_Query(query_text)

    # print(modelo.load_query(query))
    # print(modelo.query_term)

    # print(modelo.correl_matrix)
    # print(modelo.fuzzy_set_doc)
    # print(query)


    # print(modelo.load_documents(data))
    # print(modelo.freq_normal(query))

    # print("idf")
    # print(modelo.idf(query))

    # print("peso de los documentos")
    # w_i_j=modelo.docs_weights(query)
    # for term,doc in w_i_j:
    #     print(term, doc.id, w_i_j[(term,doc)])
        # print(doc.id)
    # print(modelo.docs_weights(query))

    # print("peso de la consulta")
    # print(modelo.query_weights(query))
    
    # print("frecuencia normalizada de la consulta")
    # print(modelo.freq_normal_q(query))



    #TIMER: ESO SE PUEDE COMENTAR
    # inicio_general=time.time()

    # for i,doc in enumerate(modelo.documents):
    #     inicio=time.time()

    #     print(modelo.similitud(query, doc))
       

    #     fin=time.time()
    #     print(i)
    #     print("El tiempo que se demoro")
    #     print(fin-inicio)
        
    # final=time.time()
    # print(final-inicio_general)
    
        
        # for title in titles:
        #     print(title)
    # print(titles)
    

    # print("hola")
    # # documents=[["amarillo","verde","rojo"],["rojo"],["azul","violeta","amarillo"],["blanco","negro"],["blanco","rojo"]]
    # docu1=Doc("Hola",["amarillo","verde","rojo"])
    # docu2=Doc("Hola1", ["rojo"])
    # docu3=Doc("Hola2",["azul","violeta","amarillo"])
    # docu4=Doc("Hola3",["blanco","negro"])
    # docu5=Doc("Hola4", ["blanco","rojo"])
    # documentos=[docu1,docu2,docu3,docu4,docu5]
    # print(documentos)
    #query=["not","amarillo","and","rojo","or","not","blanco"]
    #print(query)
    #modelo=Boolean_model(documentos)
    #print([doc.title for doc in modelo.similitud(query, modelo.load_documents(documentos))])
    
main()

