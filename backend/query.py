import nltk
import re
from parse import expand_contractions
from nltk.corpus import stopwords


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
        archive = open("Data_Cran/cran.qry")
        data = {}
        key = 1
        text = ""
        while(line):
            if text != "" and line[0:2] == ".I":
                data[key] = text
                text = ''
                key = line[3:-1]
            line = archive.readline()
            if line[0:2] == ".I" or line == ".W\n":
                continue
            elif line != "\n":
                text = text+""+ line[:-1]
        archive.close()
        return data
    
    
    
    
    
    
    
        