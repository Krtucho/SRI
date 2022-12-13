from boolean_model import Boolean_model
from query import Clear_Query
from parse import All_Dir_Doc,Create_Data
from vector_model import Vector_Model
import parse_cran 


# # Main booleano de pruebas con Data
# def main():

#     #dir_docs,ids = All_Dir_Doc()  # contiene las direcciones de todos los doc y su id la pos en que estos se encuentran en estos es la misma que en data
#     #data = Create_Data(dir_docs,ids) #array que contiene a todos los doc en estructura
    
#     #Con cran
#     data,dir_doc = parse_cran.Create_Data()
#     modelo=Boolean_model(data)
        
#     while(True):
        
#         print("Welcome, Please enter your query")
#         query_text = input()
        
#         if(query_text == "exit"):
#             break
        
#         query = Clear_Query(query_text,True)
#         query = modelo.load_query(query)
#         print(query)
#         titles = [doc.title for doc in modelo.similitud(query, modelo.tokens_list)]
        
#         print(titles)
    
# Main vectorial de prueba con Data
def main():

    #dir_docs,ids = All_Dir_Doc()  # contiene las direcciones de todos los doc y su id la pos en que estos se encuentran en estos es la misma que en data
    #data = Create_Data(dir_docs,ids)
    
    #Con cran
    data,dir_doc = parse_cran.Create_Data()
    modelo=Vector_Model(data)
        
    while(True):
        
        print("Welcome, Please enter your query")
        query_text = input()
  
        if(query_text == "exit"):
            break
        
        query = Clear_Query(query_text,False)
        modelo.load_query(query)

        print(query)

        for i,doc in enumerate(modelo.documents):
            similitud = modelo.similitud(query, doc)
            if(similitud >0.0):
                print(doc.title)
                print(i)
                
            
    
main()