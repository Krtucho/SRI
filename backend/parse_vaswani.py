from documents import Doc
from parse import Clear
#import ir_datasets
#dataset = ir_datasets.load("vaswani")
from parse import Open_File

# def Write_Query():
#     file = open("Data_Vaswani/querys.txt", "w")
#     querys = dataset.queries_iter()
#     for q in querys:
#         file.write("I "+str(q[0])+"\n")
#         file.write(q[1])
    
#     file.close()

# def Write_Documents():
#     docs = dataset.docs_iter()
#     for q in docs:
#         id = str(q[0])
#         file = open("Data_Vaswani/"+ id, "w")
#         file.write("I "+id+"\n")
#         file.write(q[1]+"\n")
#         file.close()
    
# def Write_Rel():
#     file = open("Data_Vaswani/rel.txt", "w")
#     text = ""
#     rel = dataset.qrels_iter()
#     for query in rel:
#         if int(query[2])>0:
#             text = str(query[0]) + " " + str(query[1])+ " " + str(query[2])
#         if text!="":
#             file.write(text + "\n")
#         text = ""
#     file.close()    
    
def Read(archive):
        text = ""
        line = archive.readline() 
        while(line):
            if line != "\n" and line[0:1] !="I":
                text = text+""+ line[:-1]
            line = archive.readline()     
        return text
    
        
def Load_Document():
    dirs = Open_File("Data_Vaswani")
    data=[]
    dir_docs = []
    id = 0
    for path in dirs:
        if(path!= "rel.txt" and path != "querys.txt"): 
            dir_docs.append('Data_Vaswani/'+ path)
            archive = open('Data_Vaswani/'+ path)
            text = Read(archive)
            term = Clear(text)
            doc = Doc(id,path,term)
            data.append(doc)
            id = id+1
            archive.close()
    return data,dir_docs

def Load_Query():
        archive = open("Data_Vaswani/querys.txt")
        data = {}
        key = 1
        text = ""
        line = True
        while(line or text!= ""):
            line = archive.readline()
            if text != "" and (line[0:1] == "I" or line == ''):
                data[key] = text
                text = ''
                key = key +1
            elif line != "\n" and line[0:2] != "I" :
                text = text+""+ line[:-1]
        archive.close()
        return data    

def Parse_Vasrel():
    archive = open("Data_Vaswani/rel.txt")
    data = {}
    line = archive.readline()
    while(line):
        if line != "\n":
            text = line[:-1].split()
            key = int(text[0])
            id = text[1]
            value = data.get(key)
            if(value != None):
                data[key] += str(id)+" "
            else:
                data[key] = str(id)+" "
            line = archive.readline() 
    archive.close()
    return data

        
#Write_Documents()
#Write_Query()
#Write_Rel()    
        

