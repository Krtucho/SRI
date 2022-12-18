from boolean_model import Boolean_model
from query import Clear_Query,Load_Query
from parse import All_Dir_Doc,Create_Data
from vector_model import Vector_Model
import parse_cran 
import numpy as np
import matplotlib.pyplot as plt
from fuzzy_model import Fuzzy_model
import parse_vaswani



# # Main booleano de pruebas
# def main():

#     #dir_docs,ids = All_Dir_Doc()  # contiene las direcciones de todos los doc y su id la pos en que estos se encuentran en estos es la misma que en data
#     #data = Create_Data(dir_docs,ids) #array que contiene a todos los doc en estructura
    
#     #Con cran
#     #data,dir_doc = parse_cran.Create_Data()
    
#     #Con vaswani
#     data,dir_doc = parse_vaswani.Load_Document()
#     modelo=Boolean_model(data)
        
#     while(True):
        
#         print("Welcome, Please enter your query")
#         query_text = input()
        
#         if(query_text == "exit"):
#             break
        
#         query = Clear_Query(query_text,True)
#         query = modelo.load_query(query)
#         print(query)
#         a = modelo.similitud(query)
#         titles = [doc.title for doc in a ]
#         dir = [dir_doc[doc.id] for doc in a ]
#         for t in range(0,len(titles)):
#             print(titles[t] + dir[t])
        
    
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
    
# Main fuzzy de prueba con Cran
def main():

    #dir_docs,ids = All_Dir_Doc()  # contiene las direcciones de todos los doc y su id la pos en que estos se encuentran en estos es la misma que en data
    #data = Create_Data(dir_docs,ids)
    
    #Con cran
    #data,dir_doc = parse_cran.Create_Data()
    
    #Vaswani
    data,dir_doc = parse_vaswani.Load_Document()
    
    modelo=Fuzzy_model(data)
        
    while(True):
        
        print("Welcome, Please enter your query")
        query_text = input()
  
        if(query_text == "exit"):
            break
        
        query = Clear_Query(query_text,False)
        modelo.load_query(query)      
        
        print(query)

        for i,doc in enumerate(modelo.documents):
            similitud = modelo.ranking_function(doc)
            if(similitud >0.0):
                print(doc.title)
                print(i)

     
# # Main booleano , vectorial, fuzzy con Cran para presicion y recobrado
# def main():
#     data,dir_doc = parse_cran.Create_Data()
#     #modelo=Vector_Model(data)
#     #modelo=Boolean_model(data)
#     modelo=Fuzzy_model(data)
#     k = 10  
#     Recall = []
#     Presicion = []
#     F1 = []
#     while(k<110): 
#                                            # cantidad de doc a recuperar   
#         querys = Load_Query()                       # carga todas las querys de prueba
#         cran_querys = parse_cran.Parse_Cranqrel()   # carga por querys todos los doc relevantes a ellas
#         for q in querys.keys():  
#             query = Clear_Query(querys[q],False)
#             #print(query)
#             modelo.load_query(query)
#             querys[q] = modelo.k_doc_best_similitud(query,k)  # por cuery se obtiene todos los doc recuperados
    
#         p=modelo.Presicion(cran_querys,querys)
#         mean_p = np.mean(p)
#         r = modelo.Recobrado(cran_querys,querys)
#         mean_r = np.mean(r)
#         f1 = modelo.f1(p,r)
#         mean_f1 = np.mean(f1)
        
#         Recall.append(mean_r)
#         Presicion.append(mean_p)
#         F1.append(mean_f1)
        
#         # print("-----------------------")
#         # print(" ")
#         # print(f"Recall: {mean_r}")
#         # print(f"Precision: {mean_p}")
#         # print(f"F1: {mean_f1}")
#         # print(" ")
#         # print("-----------------------")
        
#         k = k+10
   
    


#     Cant_Doc = [10,20,30,40,50,60,70,80,90,100] 
#     Z1 = Recall
#     Z2 = Presicion
#     Z3 = F1


#     plt.plot(Cant_Doc, Z1,  marker='o', linestyle='--', label="Recobrado", c="red")
#     plt.plot(Cant_Doc, Z2,  marker='o', linestyle='--', label="Presición", c="yellow")
#     plt.plot(Cant_Doc, Z3,  marker='o', linestyle='--', label="F1", c="blue")
#     plt.legend(loc="upper left")
    
#     plt.grid(True)
#     plt.show()    
    
            
# # Main booleano , vectorial, fuzzy con Vaswani para presicion y recobrado
# def main():
#     data,dir_doc = parse_vaswani.Load_Document()
#     #modelo=Vector_Model(data)
#     #modelo=Boolean_model(data)
#     modelo=Fuzzy_model(data)
#     k = 10  
#     Recall = []
#     Presicion = []
#     F1 = []
#     #qvas = parse_vaswani.Load_Query()  # carga todas las querys de prueba
#     #vas = parse_vaswani.Parse_Vasrel()
#     while(k<110): 
#                                            # cantidad de doc a recuperar   
#         querys = parse_vaswani.Load_Query()
#         cran_querys = parse_vaswani.Parse_Vasrel()   # carga por querys todos los doc relevantes a ellas
#         for q in querys.keys():  
#             query = Clear_Query(querys[q],False)
#             modelo.load_query(query)
#             querys[q] = modelo.k_doc_best_similitud(query,k)  # por cuery se obtiene todos los doc recuperados
    
#         p=modelo.Presicion(cran_querys,querys)
#         mean_p = np.mean(p)
#         r = modelo.Recobrado(cran_querys,querys)
#         mean_r = np.mean(r)
#         f1 = modelo.f1(p,r)
#         mean_f1 = np.mean(f1)
        
#         Recall.append(mean_r)
#         Presicion.append(mean_p)
#         F1.append(mean_f1)
        
#         # print("-----------------------")
#         # print(" ")
#         # print(f"Recall: {mean_r}")
#         # print(f"Precision: {mean_p}")
#         # print(f"F1: {mean_f1}")
#         # print(" ")
#         # print("-----------------------")
        
#         k = k+10
   
    


#     Cant_Doc = [10,20,30,40,50,60,70,80,90,100] 
#     Z1 = Recall
#     Z2 = Presicion
#     Z3 = F1


#     plt.plot(Cant_Doc, Z1,  marker='o', linestyle='--', label="Recobrado", c="red")
#     plt.plot(Cant_Doc, Z2,  marker='o', linestyle='--', label="Presición", c="yellow")
#     plt.plot(Cant_Doc, Z3,  marker='o', linestyle='--', label="F1", c="blue")
#     plt.legend(loc="upper left")
    
#     plt.grid(True)
#     plt.show()    
    
            
    
main()