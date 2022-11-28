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
    #new_text = re.sub(r"\s+", "", text)
    tokens = nltk.word_tokenize(new_text)
    #Unique Tokens (Solo deja un conj de tokens)
    #tokens=list(set(tokens))
    
    # Remove Special characters (Elimina los caracteres especiales)
    removetable=str.maketrans("", "", "!@#$%^&*()_=-\|][:';:,<.>/?`~") 
    tokens=[x.translate(removetable) for x in tokens]
    
    #Remove the stopwords
    stop_words = stopwords.words('english')
    tokens = list(set(tokens)-set(stop_words))
    #tokens = [i for i in tokens if i not in stop_words]

    return list(filter(None, tokens))
    
def Read(archive):
        title = ""
        text = ""
        count = 1
        line = archive.readline() 
        while(line):
            line = archive.readline()
            if(count == 1):
               #title = line[9:-1]
               text = line[9:-1]
            elif line != "\n":
                text = text+""+ line[:-1] 
            count = count+1
        #return title,text
        return text


def Create_Data(dir_docs,id_doc):
    data = [] 
    id = 0
    for dir in dir_docs:
        archive = open(dir)
        #title,text = Read(archive)
        text = Read(archive)
        #print(text)
        #title= Clear(title)
        term = Clear(text)
        title = str(id_doc[id])
        doc = Doc(id,title,term)
        data.append(doc)
        id = id+1

        archive.close()
        #break
    return data   



#dir_docs,ids = All_Dir_Doc()  # contiene las direcciones de todos los doc y su id la pos en que estos se encuentran en estos es la misma que en data
#data = Create_Data(dir_docs)

#print(data[0].term)
#print(data[0].title)  

# for i in data:
#     print(i.term)
#     print(i.title)  

   

   