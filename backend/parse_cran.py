from parse import Clear
from documents import Doc
import os  
import ir_datasets

dataset = ir_datasets.load("cranfield")
#for query in dataset.queries_iter():
#    query # namedtuple<query_id, text>

def Read_Write(archive):
        data = {}
        key = 1
        text = ""
        line = archive.readline()
        file = open("Data_Cran/I 1.txt", "w")
        file.write(line)
        while(line):
            if text != "" and line[0:2] == ".I":
                data[key] = text
                text = ''
                key = line[3:-1]
                file.close() #cierra el archivo abierto
                file = open("Data_Cran/I "+str(key)+".txt", "w") #abre un nuevo archivo
                file.write(line)
            line = archive.readline()
            if line[0:2] == ".I" or line == ".T\n" or line == ".A\n" or line == ".B\n" or line == ".W\n":
                file.write(line)
                continue
            elif line != "\n":
                text = text+""+ line[:-1]
                file.write(line)
        file.close()         
        return data


def Create_Data():
    data = []
    dir = [] 
    id = 0
    archive = open("Data_Cran/cran_all.txt")
    data_base = Read_Write(archive)
    for key in data_base.keys():
        text = data_base[key]
        term = Clear(text)
        title = "I " + str(key)
        doc = Doc(id,str(key),term)
        data.append(doc)
        dir.append("Data_Cran/" + str(title) + ".txt")
        id = id+1
    archive.close()
    return data,dir   


def Parse_Cranqrel():
    archive = open("Data_Cran/rel.txt")
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
    
def Load_Query_DataSet():
    data = {}
    for query in dataset.queries_iter():
        data[query[0]] = query[1] 
    return data    

def Write_Query(querys):
    file = open("Data_Cran/querys.txt", "w")
    
    for q in querys.keys():
        file.write(".I "+str(q)+"\n")
        file.write(querys[q]+"\n")
    
    file.close()

def Write_Doc():
    #for query in dataset.queries_iter():
        #data[query[0]] = query[1] 
    pass

def Write_Rel():
    file = open("Data_Cran/rel.txt", "w")
    text = ""
    for query in dataset.qrels_iter():
        if int(query[2])>0:
            text = str(query[0]) + " " + str(query[1])+ " " + str(query[2])
        if text!="":
            file.write(text + "\n")
        text = ""
    file.close()    

    
#Write_Query(Load_Query_DataSet())
Write_Rel()