from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from boolean_model import Boolean_model
from parse import All_Dir_Doc, Create_Data
from query import Clear_Query

# TODO: Agregar un import que sea el que contenga la clase en la que se procesen todos los documentos al comienzo de la ejecucion del programa.
# TODO: Tb hay que agregar las clases correspondientes con los modelos para ejecutar y llevar a cabo los metodos de similitud y otros que sean necesarios.

dir_docs,ids = All_Dir_Doc()  # contiene las direcciones de todos los doc y su id(nombre) la pos en que estos se encuentran en estos es la misma que en data
data_bd = Create_Data(dir_docs,ids)

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
    out = process("boolean",input)
    #return Response("Se supone que aqui se devuelve un json(diccionario) con todos los documentos relevantes en la consulta", status=status.HTTP_200_OK)
    return Response(out, status=status.HTTP_200_OK)

@api_view(['POST'])
def boolean(request):
    return post_boolean(request)

def post_vect(request):
    pass

@api_view(['POST'])
def vect(request):
    return post_vect(request)


def process(model,input):
    #modelo=Boolean_model(data)
    modelo = None
    if(model == "boolean"):
        modelo=Boolean_model(data_bd)
    #print("Welcome, Please enter your query")
    query_text = input     
    #if(query_text == "exit"):
    #    break    
    query = Clear_Query(query_text)
    query = modelo.load_query(query)
    print(query)
    titles = dict()
    doc_p = None
    for doc in modelo.similitud(query, modelo.tokens_list):
        doc_p = doc.title
        titles[doc.title]=dir_docs[doc.id]
        
        
    for t in titles:
        print(t)

    return titles    
