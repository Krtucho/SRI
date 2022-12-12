<<<<<<< Updated upstream
from boolean_model import Boolean_model
from documents import Doc

def main():
    print("hola")
    # documents=[["amarillo","verde","rojo"],["rojo"],["azul","violeta","amarillo"],["blanco","negro"],["blanco","rojo"]]
    docu1=Doc("Hola",["amarillo","verde","rojo"])
    docu2=Doc("Hola1", ["rojo"])
    docu3=Doc("Hola2",["azul","violeta","amarillo"])
    docu4=Doc("Hola3",["blanco","negro"])
    docu5=Doc("Hola4", ["blanco","rojo"])
    documentos=[docu1,docu2,docu3,docu4,docu5]
    print(documentos)
    query=["not","amarillo","and","rojo","or","not","blanco"]
    print(query)
    modelo=Boolean_model(documentos)
    print([doc.title for doc in modelo.similitud(query, modelo.load_documents(documentos))])

main()
=======
from boolean_model import Boolean_model
from vector_model import Vector_Model
from query import Clear_Query
from parse import All_Dir_Doc,Create_Data
from documents import Doc

def main():

    dir_docs,ids = All_Dir_Doc()  # contiene las direcciones de todos los doc y su id la pos en que estos se encuentran en estos es la misma que en data
    data = Create_Data(dir_docs,ids)
    # data=[]
    # doc1= Doc("doc1","hola",["leon","leon","leon"])
    # data.append(doc1)
    # doc2= Doc("doc2","hola1",["leon","leon","leon","zorro"])
    # data.append(doc2)
    # doc3= Doc("doc3","hola2",["leon","zorro","nutria"])
    # data.append(doc3)
    # doc4= Doc("doc4","hola3",["leon","leon","leon","zorro","zorro","zorro"])
    # data.append(doc4)
    # doc5= Doc("doc5","hola4",["nutria"])
    # data.append(doc5)

    modelo=Vector_Model(data)
        
    while(True):
        
        print("Welcome, Please enter your query")
        query_text = input()
    # query_text="shdkjfbdj kjdj"
    # query_text="leon zorro nutria"
    # query_text="lion and tiger tiger tiger be only you and never forget it forget it 2017"
        
        if(query_text == "exit"):
            break
        
    query = Clear_Query(query_text)
        # query = modelo.load_query(query)
    print(query)
    # print(modelo.load_documents(data))
    print(modelo.freq_normal(query))

    print("idf")
    print(modelo.idf(query))

    print("peso de los documentos")
    w_i_j=modelo.docs_weights(query)
    for term,doc in w_i_j:
        print(term, doc.id, w_i_j[(term,doc)])
        # print(doc.id)
    # print(modelo.docs_weights(query))

    print("peso de la consulta")
    print(modelo.query_weights(query))
    
    print("frecuencia normalizada de la consulta")
    print(modelo.freq_normal_q(query))

    print("similitud entre un doc y la consulta")
    print(modelo.similitud(query, doc5))
        
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

>>>>>>> Stashed changes
