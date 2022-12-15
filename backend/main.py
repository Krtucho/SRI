from boolean_model import Boolean_model
from query import Clear_Query,Load_Query
from parse import All_Dir_Doc,Create_Data
from vector_model import Vector_Model
import parse_cran 
import numpy as np

# Main booleano de pruebas con Data
def main():

    #dir_docs,ids = All_Dir_Doc()  # contiene las direcciones de todos los doc y su id la pos en que estos se encuentran en estos es la misma que en data
    #data = Create_Data(dir_docs,ids) #array que contiene a todos los doc en estructura
    
    #Con cran
    data,dir_doc = parse_cran.Create_Data()
    modelo=Boolean_model(data)
        
    while(True):
        
        print("Welcome, Please enter your query")
        query_text = input()
        
        if(query_text == "exit"):
            break
        
        query = Clear_Query(query_text,True)
        query = modelo.load_query(query)
        print(query)
        titles = [doc.title for doc in modelo.similitud(query)]
        for t in titles:
            print(t)
        
    
# # Main vectorial de prueba con Data
# def main():

#     #dir_docs,ids = All_Dir_Doc()  # contiene las direcciones de todos los doc y su id la pos en que estos se encuentran en estos es la misma que en data
#     #data = Create_Data(dir_docs,ids)
    
#     #Con cran
#     data,dir_doc = parse_cran.Create_Data()
#     modelo=Vector_Model(data)
        
#     while(True):
        
#         print("Welcome, Please enter your query")
#         query_text = input()
  
#         if(query_text == "exit"):
#             break
        
#         query = Clear_Query(query_text,False)
#         modelo.load_query(query)

#         print(query)

#         for i,doc in enumerate(modelo.documents):
#             similitud = modelo.similitud(query, doc)
#             if(similitud >0.0):
#                 print(doc.title)
#                 print(i)

     
# # # Main booleano y vectorial para presicion y recobrado
# def main():
#     data,dir_doc = parse_cran.Create_Data()
#     #modelo=Vector_Model(data)
#     modelo=Boolean_model(data)
#     k = 100                                     # cantidad de doc a recuperar   
#     querys = Load_Query()                       # carga todas las querys de prueba
#     cran_querys = parse_cran.Parse_Cranqrel()   # carga por querys todos los doc relevantes a ellas
#     for q in querys.keys():  
#         query = Clear_Query(querys[q],False)
#         modelo.load_query(query)
#         querys[q] = modelo.k_doc_best_similitud(query,k)  # por cuery se obtiene todos los doc recuperados
    
#     p=modelo.Presicion(cran_querys,querys)
#     mean_p = np.mean(p)
#     r = modelo.Recobrado(cran_querys,querys)
#     mean_r = np.mean(r)
#     f1 = modelo.f1(p,r)
#     mean_f1 = np.mean(f1)
    
#     print(f"Recall: {mean_r}")
#     print(f"Precision: {mean_p}")
#     print(f"F1: {mean_f1}")
            
    
main()