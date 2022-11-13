from boolean_model import Boolean_model
from query import Clear_Query
from parse import All_Dir_Doc,Create_Data

def main():

    dir_docs,ids = All_Dir_Doc()  # contiene las direcciones de todos los doc y su id la pos en que estos se encuentran en estos es la misma que en data
    data = Create_Data(dir_docs)
    modelo=Boolean_model(data)
        
    while(True):
        
        print("Welcome, Please enter your query")
        query_text = input()
        
        if(query_text == "exit"):
            break
        
        query = Clear_Query(query_text)
        print([doc.title for doc in modelo.similitud(query, modelo.tokens_list)])

    

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