from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# TODO: Agregar un import que sea el que contenga la clase en la que se procesen todos los documentos al comienzo de la ejecucion del programa.
# TODO: Tb hay que agregar las clases correspondientes con los modelos para ejecutar y llevar a cabo los metodos de similitud y otros que sean necesarios.

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Boolean': '/boolean/',
    }
    return Response(api_urls)
    
# TODO
# Aqui se supone que sea donde se realicen las modificaciones pertinentes. Luego en caso de agregar nuevos modelos al sistema, modificar el archivo urls.py agregando las urls de para ejecutar los mismos.
# En un principio se supone que se cargue todo el contenido de los documentos en la clase que se supone que debe importarse en el 1er (TODO) de este apartado. Asi que ya llegado a este punto, podremos trabajar libremente
# haciendo uso de esta clase para hallar similitud, etc...
def post_boolean(request):
    # TODO: Aqui va el codigo a ejecutar del modelo booleano para procesar la consulta y luego devolver los documentos necesarios.
    print(request)
    data = request.data
    print(data) # La forma ideal del cuerpo de la peticion seria {"query":"Consulta a realizar por el usuario"}
    # Al hacer print al contenido de data, se puede mostrar el json(diccionario) con los argumentos que necesitemos para que el mismo sea ejecutado correctamente 
    return Response("Se supone que aqui se devuelve un json(diccionario) con todos los documentos relevantes en la consulta", status=status.HTTP_200_OK)
    
@api_view(['POST'])
def boolean(request):
    return post_boolean(request)