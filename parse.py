from fileinput import close
from documents import Doc
import os, sys


def Open_File(path): 
    dirs = os.listdir( path ) 
    return dirs

def All_Dir_Doc():
    dirs = Open_File("Data")
    dir_docs = []
    ids = []
    for path in dirs: 
        new_path = 'Data/'+ path
        new_dirs = Open_File(new_path)
        for d in new_dirs:
            dir_docs.append(new_path+"/"+d)
            ids.append(d)
    return dir_docs,ids


def Clear(text):
    pass


dir_docs,ids = All_Dir_Doc()  # contiene las direcciones de todos los doc y su id la pos en que estos se encuentran en estos es la misma que en data

def Create_Data(dir_docs):
    data = [] 
    id = 0
    for dir in dir_docs:
        archive = open(dir)
        count = 1
        title = ""
        text = ""
    
        line = archive.readline() 
        while(line):
            line = archive.readline()
            if(count == 1):
               title = line[9:-1]
            elif line != "\n":
                text = text+""+ line[:-1] 
            count = count+1
        count = 0
        #print(text)
        term = Clear(text)
        doc = Doc(id,title,text)
        data.append(doc)
        id = id+1
        archive.close()
        #break
    return data    
   