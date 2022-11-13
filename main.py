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