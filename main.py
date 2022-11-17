from boolean_model import Boolean_model
from query import Clear_Query
from parse import All_Dir_Doc,Create_Data

def main():

    dir_docs,ids = All_Dir_Doc()  # contiene las direcciones de todos los doc y su id la pos en que estos se encuentran en estos es la misma que en data
    data = Create_Data(dir_docs,ids)
    modelo=Boolean_model(data)
        
    while(True):
        
        print("Welcome, Please enter your query")
        query_text = input()
        
        if(query_text == "exit"):
            break
        
        query = Clear_Query(query_text)
        query = modelo.load_query(query)
        print(query)
        titles = [doc.title +"\n" for doc in modelo.similitud(query, modelo.tokens_list)]
        
        for title in titles:
            print(title)
    
main()
