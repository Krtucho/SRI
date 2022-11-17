from documents import Doc
import os, sys
import nltk
from nltk.corpus import stopwords


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
    new_text = text.lower()
    
    tokens = nltk.word_tokenize(new_text)
    #Unique Tokens (Solo deja un conj de tokens)

    
    # Remove Special characters (Elimina los caracteres especiales)
    removetable=str.maketrans("", "", "!@#$%^&*()_=-\|][:';:,<.>/?`~") 
    tokens=[x.translate(removetable) for x in tokens]
    
    #Remove the stopwords
    stop_words = stopwords.words('english')
    tokens = list(set(tokens)-set(stop_words))

    return list(filter(None, tokens))
    
def Read(archive):
        title = ""
        text = ""
        count = 1
        line = archive.readline() 
        while(line):
            line = archive.readline()
            if(count == 1):
               title = line[9:-1]
            elif line != "\n":
                text = text+""+ line[:-1] 
            count = count+1
        return title,text


def Create_Data(dir_docs):
    data = [] 
    id = 0
    for dir in dir_docs:
        archive = open(dir)
        title,text = Read(archive)
        #print(text)
        title= Clear(title)
        term = Clear(text)

        doc = Doc(id,title,term)
        data.append(doc)
        id = id+1

        archive.close()
        #break
    return data   
   
