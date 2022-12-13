from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import parse_cran
from boolean_model import Boolean_model
from parse import All_Dir_Doc, Create_Data
from query import Clear_Query
from vector_model import Vector_Model

# TODO: Agregar un import que sea el que contenga la clase en la que se procesen todos los documentos al comienzo de la ejecucion del programa.
# TODO: Tb hay que agregar las clases correspondientes con los modelos para ejecutar y llevar a cabo los metodos de similitud y otros que sean necesarios.

dir_docs_N,ids = All_Dir_Doc()  # contiene las direcciones de todos los doc y su id(nombre) la pos en que estos se encuentran en estos es la misma que en data
data_bd_N = Create_Data(dir_docs_N,ids)
#Cran
data_bd_C,dir_docs_C = parse_cran.Create_Data()

#data_bd,dir_docs = parse_cran.Create_Data()


# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Boolean': '/boolean/',
        'Vectorial':'/vect/'
    }
    return Response(api_urls)
    
# TODO
# Aqui se supone que sea donde se realicen las modificaciones pertinentes. Luego en caso de agregar nuevos modelos al sistema, modificar el archivo urls.py agregando las urls de para ejecutar los mismos.
# En un principio se supone que se cargue todo el contenido de los documentos en la clase que se supone que debe importarse en el 1er (TODO) de este apartado. Asi que ya llegado a este punto, podremos trabajar libremente
# haciendo uso de esta clase para hallar similitud, etc...
def post_boolean(request):
    # TODO: Aqui va el codigo a ejecutar del modelo booleano para procesar la consulta y luego devolver los documentos necesarios.
    # if(loaded == False):
    #     loaded = True
    print(request)
    data = request.data
    print(data) # La forma ideal del cuerpo de la peticion seria {"query":"Consulta a realizar por el usuario"}
    # Al hacer print al contenido de data, se puede mostrar el json(diccionario) con los argumentos que necesitemos para que el mismo sea ejecutado correctamente 
    input = data["query"]
    data_base = data.get("data")
    out = process("boolean",input,data_base)
    #out = process("boolean",input)
    #return Response("Se supone que aqui se devuelve un json(diccionario) con todos los documentos relevantes en la consulta", status=status.HTTP_200_OK)
    return Response(out, status=status.HTTP_200_OK)

@api_view(['POST'])
def boolean(request):
    return post_boolean(request)

def post_vect(request):
    print(request)
    data = request.data
    print(data) # La forma ideal del cuerpo de la peticion seria {"query":"Consulta a realizar por el usuario"}
    # Al hacer print al contenido de data, se puede mostrar el json(diccionario) con los argumentos que necesitemos para que el mismo sea ejecutado correctamente 
    input = data["query"]
    data_base = data.get("data")
    out = process("vect",input,data_base)
    #out = process("vect",input)
    #return Response("Se supone que aqui se devuelve un json(diccionario) con todos los documentos relevantes en la consulta", status=status.HTTP_200_OK)
    return Response(out, status=status.HTTP_200_OK)

@api_view(['POST'])
def vect(request):
    return post_vect(request)


def process(model,query_text,db):
    boolean = False
    modelo = None
    
    if(db!= None and db =="cran" ):
        print("Entre en cran")
        data_bd  = data_bd_C
        dir_docs = dir_docs_C
    else:
        data_bd = data_bd_N
        dir_docs = dir_docs_N
        
    if model == "boolean":
        modelo=Boolean_model(data_bd)
        boolean = True
        
    if model =="vect":
        modelo = Vector_Model(data_bd)    
           
    query = Clear_Query(query_text,boolean)
    titles = dict()
    
    if model == "boolean":
        query = modelo.load_query(query)
        print("boolean")
        print(query)
        for doc in modelo.similitud(query, modelo.tokens_list):
            titles[doc.title]=dir_docs[doc.id]
    
    if model =="vect":
        modelo.load_query(query)
        print(query)
        print("vect")
        similitud_dic ={}
        for doc in modelo.documents:
            similitud = modelo.similitud(query, doc)
            if(similitud >0.0):
                similitud_dic[doc] = similitud
                titles[doc.title]=dir_docs[doc.id]
    
    for t in titles:
        print(t)

    return titles    
