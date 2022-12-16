import nltk
from nltk.corpus import stopwords

def Clear_Query(text):
    new_text = text.lower()
    #new_text = re.sub(r"\s+", "", text)
    tokens = nltk.word_tokenize(new_text)
    
    # Remove Special characters (Elimina los caracteres especiales)
    removetable=str.maketrans("", "", "!@#$%^&*()_=-\|][:';:,<.>/?`~") 
    tokens=[x.translate(removetable) for x in tokens]
    
    #Remove the stopwords
    stop_words = stopwords.words('english')
    stop_words.remove("not")
    stop_words.remove("and")
    stop_words.remove("or")
    tokens = [i for i in tokens if i not in stop_words]
    
    return list(filter(None, tokens))
    