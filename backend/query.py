import nltk
import re
from parse import expand_contractions
from nltk.corpus import stopwords

# Elimina ceros a la izquierda de numeros
def Clear_Zero(string):
    text = ''
    ok = False
    for i in range (0,len(string)):
        if string[i] == "0":
            continue
        else:
            text = string[i:]
            break  
    return text        

def Clear_Query(text,booleano):
    # Lleva todo el texto a minuscula
    new_text = text.lower()
    # Arregla las contracciones
    new_text = expand_contractions(new_text)
    
    new_text = re.sub('\w*\d\w*', '', new_text)
    new_text = re.sub('\n', ' ', new_text)
    new_text = re.sub(r"http\S+", "", new_text)
    new_text = re.sub('[^a-z]', ' ', new_text)
    
    # Toqueniza
    tokens = nltk.word_tokenize(new_text)
    
    # Remove Special characters (Elimina los caracteres especiales)
    removetable=str.maketrans("", "", "!@#$%^&*()_=-\|][:';:,<.>/?`~") 
    tokens=[x.translate(removetable) for x in tokens]
    
    stop_words = stopwords.words('english')
    #Remove the stopwords
    if booleano:
        stop_words.remove("not")
        stop_words.remove("and")
        stop_words.remove("or")   
    tokens = list(set(tokens)-set(stop_words)) #solo es para el booelano     
    #tokens = [i for i in tokens if i not in stop_words]
    
    return list(filter(None, tokens))
 

def Load_Query():
        archive = open("Data_Cran/querys.txt")
        data = {}
        key = 1
        text = ""
        line = True
        while(line or text!= ""):
            line = archive.readline()
            if text != "" and (line[0:2] == ".I" or line == ''):
                data[key] = text
                text = ''
                key = key +1
            elif line != "\n" and line[0:2] != ".I" :
                text = text+""+ line[:-1]
        archive.close()
        return data    
    
 
    
    
    
    
        