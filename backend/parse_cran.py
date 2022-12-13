from parse import Clear
from documents import Doc
import os  

def Read_Write(archive):
        data = {}
        key = 1
        text = ""
        line = archive.readline()
        file = open("Data_Cran/.I 1.txt", "w")
        file.write(line)
        while(line):
            if text != "" and line[0:2] == ".I":
                data[key] = text
                text = ''
                key = line[3:-1]
                file.close() #cierra el archivo abierto
                file = open("Data_Cran/.I "+str(key)+".txt", "w") #abre un nuevo archivo
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
        title = ".I " + str(key)
        doc = Doc(id,title,term)
        data.append(doc)
        dir.append("Data_Cran/" + str(title) + ".txt")
        id = id+1
    archive.close()
    return data,dir   


