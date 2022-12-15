from documents import Doc
import os, sys
import nltk
import re
from nltk.corpus import stopwords

# Dictionary of english Contractions
contractions_dict = {"ain't": "are not", "'s": " is", "aren't": "are not", "can't": "can not",
                     "can't've": "cannot have", "'cause": "because", "could've": "could have", "couldn't": "could not",
                     "couldn't've": "could not have", "didn't": "did not", "doesn't": "does not", "don't": "do not",
                     "hadn't": "had not", "hadn't've": "had not have", "hasn't": "has not", "haven't": "have not",
                     "he'd": "he would", "he'd've": "he would have", "he'll": "he will", "he'll've": "he will have",
                     "how'd": "how did", "how'd'y": "how do you", "how'll": "how will", "i'd": "i would",
                     "i'd've": "i would have", "i'll": "i will", "i'll've": "i will have", "i'm": "i am",
                     "i've": "i have", "isn't": "is not", "it'd": "it would", "it'd've": "it would have",
                     "it'll": "it will", "it'll've": "it will have", "let's": "let us", "ma'am": "madam",
                     "mayn't": "may not", "might've": "might have", "mightn't": "might not",
                     "mightn't've": "might not have", "must've": "must have", "mustn't": "must not",
                     "mustn't've": "must not have", "needn't": "need not", "needn't've": "need not have",
                     "o'clock": "of the clock", "oughtn't": "ought not", "oughtn't've": "ought not have",
                     "shan't": "shall not", "sha'n't": "shall not", "shan't've": "shall not have", "she'd": "she would",
                     "she'd've": "she would have", "she'll": "she will", "she'll've": "she will have",
                     "should've": "should have", "shouldn't": "should not", "shouldn't've": "should not have",
                     "so've": "so have", "that'd": "that would", "that'd've": "that would have",
                     "there'd": "there would", "there'd've": "there would have", "they'd": "they would",
                     "they'd've": "they would have", "they'll": "they will", "they'll've": "they will have",
                     "they're": "they are", "they've": "they have", "to've": "to have", "wasn't": "was not",
                     "we'd": "we would", "we'd've": "we would have", "we'll": "we will", "we'll've": "we will have",
                     "we're": "we are", "we've": "we have", "weren't": "were not", "what'll": "what will",
                     "what'll've": "what will have", "what're": "what are", "what've": "what have",
                     "when've": "when have", "where'd": "where did", "where've": "where have", "who'll": "who will",
                     "who'll've": "who will have", "who've": "who have", "why've": "why have", "will've": "will have",
                     "won't": "will not", "won't've": "will not have", "would've": "would have",
                     "wouldn't": "would not", "wouldn't've": "would not have", "y'all": "you all",
                     "y'all'd": "you all would", "y'all'd've": "you all would have", "y'all're": "you all are",
                     "y'all've": "you all have", "you'd": "you would", "you'd've": "you would have",
                     "you'll": "you will", "you'll've": "you will have", "you're": "you are", "you've": "you have"}

# Regular expression for finding contractions
contractions_re = re.compile('(%s)' % '|'.join(contractions_dict.keys()))

# Function for expanding contractions
def expand_contractions(text, _contractions_dict=None):
    if _contractions_dict is None:
        _contractions_dict = contractions_dict

    def replace(match):
        return _contractions_dict[match.group(0)]
    return contractions_re.sub(replace, text)




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
    
    #Remove the stopwords
    stop_words = stopwords.words('english')
    #tokens = list(set(tokens)-set(stop_words)) #solo es para el booelano
    tokens = [i for i in tokens if i not in stop_words]

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


   