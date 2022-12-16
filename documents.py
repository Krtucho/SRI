

class Doc:

    def __init__(self,id, title, term):
        self.title=title
        self.term=term
        self.id = id
        self.term_frec = {}  # diccionario de termino_frecuencia normalizada
        self.max_frec = 0
        self.Update_Frecuency()
    
    
    def Update_Frecuency(self):
        for t in self.term:
            if t in self.term_frec:
                self.term_frec[t] +=1
            else: self.term_frec[t] =1
            if self.max_frec< self.term_frec[t]:
                self.max_frec = self.term_frec[t]
        for f in self.term_frec:
            self.term_frec[f] /= self.max_frec        
        
            
    
    