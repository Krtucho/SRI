from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import parse_cran
from boolean_model import Boolean_model
from parse import All_Dir_Doc, Create_Data
from query import Clear_Query
from vector_model import Vector_Model
import parse_vaswani
from fuzzy_model import Fuzzy_model


import os
from django.http import JsonResponse, HttpResponse
import json
# TODO: Agregar un import que sea el que contenga la clase en la que se procesen todos los documentos al comienzo de la ejecucion del programa.
# TODO: Tb hay que agregar las clases correspondientes con los modelos para ejecutar y llevar a cabo los metodos de similitud y otros que sean necesarios.

dir_docs_N,ids = All_Dir_Doc()  # contiene las direcciones de todos los doc y su id(nombre) la pos en que estos se encuentran en estos es la misma que en data
data_bd_N = Create_Data(dir_docs_N,ids)
#Cran
data_bd_C,dir_docs_C = parse_cran.Create_Data()
#Vaswani
data_bd_V,dir_docs_V = parse_vaswani.Load_Document()


# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Boolean': '/boolean/',
        'Vectorial':'/vect/',
        'Fuzzy':'/fuzzy/'
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
    return HttpResponse(json.dumps(out), content_type="application/json")

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
    return HttpResponse(json.dumps(out), content_type="application/json")

@api_view(['POST'])
def vect(request):
    return post_vect(request)

def post_fuzzy(request):
    print(request)
    data = request.data
    print(data) # La forma ideal del cuerpo de la peticion seria {"query":"Consulta a realizar por el usuario"}
    # Al hacer print al contenido de data, se puede mostrar el json(diccionario) con los argumentos que necesitemos para que el mismo sea ejecutado correctamente 
    input = data["query"]
    data_base = data.get("data")
    out = process("fuzzy",input,data_base)
    return HttpResponse(json.dumps(out), content_type="application/json")


@api_view(['POST'])
def fuzzy(request):
    return post_fuzzy(request)


def process(model,query_text,db):
    boolean = False
    modelo = None
    
    if(db!= None and db =="cran" ):
        #print("Entre en cran")
        data_bd  = data_bd_C
        dir_docs = dir_docs_C
    elif(db!= None and db =="vas" ):
        print("Entre en vaswani")
        data_bd  = data_bd_V
        dir_docs = dir_docs_V
    else:
        data_bd = data_bd_N
        dir_docs = dir_docs_N
        
    if model == "boolean":
        modelo=Boolean_model(data_bd)
        boolean = True
        
    elif model =="vect":
        modelo = Vector_Model(data_bd) 
    
    elif model == "fuzzy":
        modelo=Fuzzy_model(data_bd)       
           
    query = Clear_Query(query_text,boolean)
    titles = dict()
    
    if model == "boolean":
        query = modelo.load_query(query)
        print("boolean")
        print(query)
        k = 0
        for doc in modelo.similitud(query):
            if k>10:
                break
            titles[doc.title]=dir_docs[doc.id]
            k = k+1
        
    if model =="vect":
        modelo.load_query(query)
        print(query)
        print("vect")
        similitud_dic ={}
        for doc in modelo.documents:
            similitud = modelo.similitud(query, doc)
            if(similitud >0.1):
                similitud_dic[doc] = similitud
                #titles[doc.title]=dir_docs[doc.id]
        sortedDictWithValues = dict(sorted(similitud_dic.items(), key=lambda x: x[1], reverse=True)) 
        similitud_dic = sortedDictWithValues       
        aux = list(similitud_dic.keys())[0:10]
        for doc in aux:
            titles[doc.title]=dir_docs[doc.id]
        
    if model =="fuzzy":
        modelo.load_query(query)      
        print(query)
        print("fuzzy")
        similitud_dic ={}
        for i,doc in enumerate(modelo.documents):
            similitud = modelo.ranking_function(doc)
            if(similitud >0.01):
                similitud_dic[doc] = similitud
                #titles[doc.title]=dir_docs[doc.id]
        sortedDictWithValues = dict(sorted(similitud_dic.items(), key=lambda x: x[1], reverse=True)) 
        similitud_dic = sortedDictWithValues
        aux = list(similitud_dic.keys())[0:10]
        for doc in aux:
            titles[doc.title]=dir_docs[doc.id]       
                
    # for t in titles:
    #     print("T")
    #     print(t)
    #     print(t[0])
    #     print(t[1])

    response = []
    try:
        for doc in titles.items():
            url_doc = doc[1]#.replace(".","_")
            if db != None:
                if db == "news":
                    url_doc = url_doc[5:]
                elif db == "cran":
                    url_doc = url_doc[10:]
                elif db == "vas":
                    url_doc = str(url_doc)
                    url_doc = url_doc[12:]
            # print("url_doc")
            # print(url_doc)
            responseData = {
            'name': doc[0],
            'url': 'http://localhost:8000/static/' + url_doc
            }
            # print(responseData)
            response.append( responseData)
    except Exception as e:
        print(e)
    # responseData = {
    #     'id': 4,
    #     'name': 'Test Response',
    #     'roles' : ['Admin','User']
    # }

    # print(response)
    return response  
