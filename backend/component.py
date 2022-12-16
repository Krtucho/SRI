class Component:
    """Componente Conexa"""
    def __init__(self, n_components: int, query: str, components:set, left_components:set) -> None:
        self.n_components: int = n_components # Numero de terminos(componentes que integran esta cc)
        self.components:set =  components # Conjunto con los distintos terminos que integran la cc
        self.query: str = query  # String con la query que representa a esta cc (sin parentesis)
        self.left_components: set = left_components  # Conjunto con componentes restantes de esta cc...Ej Si ya contiene al termino t1 y t2, pero en la query hay 3 terminos
                                                     # Este set contendra al termino t3 y el set de self.components contendra a t1 y t2
        
    def __str__(self):
        return self.query
   
    def eval(self):
        """Genera todas las FND restantes de la CC actual agregando las componentes que faltan hasta lograr generar FNDC para cada cc."""
        components_list: list = [] # Lista que contiene instancias de Component(CC)
        
        for left_component in self.left_components:
            
            components = self.add_component(left_component) # Obtengo las 2 CC que se forman al hacer A & ( ~B v B ) **Logica de toda la laif**
            if len(components[0].left_components) == 0: # Si en la primera forma Ya se agregaron todos los camponentes, agrego esta a la lista a devolver
                components_list.append(components[0])
            else:
                for component in components[0].eval(): # Sino, recorro cada cc que me genera esta cc al hacer A & ( ~B v B ) **Logica de toda la laif**
                    components_list.append(component)
              
            if len(components[1].left_components) == 0: # Si en la segunda forma Ya se agregaron todos los camponentes, agrego esta a la lista a devolver
                components_list.append(components[1])
            else:  
                for component in components[1].eval(): # Sino, recorro cada cc que me genera esta cc al hacer A & ( ~B v B ) **Logica de toda la laif**
                    components_list.append(component)
            
        return components_list
        
    @staticmethod
    def reduce(components_list: list, str_components_dict:dict) -> dict:
        """Dada una lista con las componentes conexas y un diccionario de llave(terminos( => indice en el array. Al indice t1 le corresponde el indice 1, al indice t2 el indice 2 en el array....termino tn => indice n. \n Devuelve un diccionario con las cc en plan llaves: (0 1 0) (1 0 1) y como valores las cc de tipo Component"""
        component_dict: dict = {}
         
        for component in components_list:   # Recorro todas las cc para ver cuales se repiten y deshacerme de estas.
            index = []                      # Me entero de esto al agregar la llave al diccionario. Si la llave ya existe, entonces se repite una cc
            bool_val = []
            every_cc = component.query.split(" & ")
            for token in every_cc:  # Recorro cada termino y verifico si esta negado o no
                if len(token) == 0:
                    continue
                if token[0] == "~":
                    temp_index = str_components_dict[token[1:]]
                    index.append((temp_index, 0))   # Si se encuentra negado agrega la tupla (indice del termino, 0)
                    # bool_val.append(0)
                else:   # Si no se encuentra negado agrega la tupla (indice del termino, 1)
                    temp_index = str_components_dict[token]
                    index.append((temp_index, 1))
                    # bool_val.append(1)
                    
            bool_val = sorted(index, key=lambda x : x[0])   # Los ordeno por valor de indice del termino en el array
            print(bool_val)
            
            dict_str = ""
            for val in bool_val:
                dict_str += str(val[1])+ " "
            
            if dict_str[len(dict_str) - 1] == " ":
                dict_str = dict_str[:-1]
            component_dict[(dict_str)] = component
            
        return component_dict
        
    def add_component(self, component_letter: str):
        """Obtengo las 2 CC que se forman al hacer A & ( ~B v B ) **Logica de toda la laif**. Devuelvo una tupla con 2 cc de tipo Component"""
        return (Component(self.n_components+1, self.query + (" & " if self.n_components >= 1 else "") +component_letter, self.components.union([component_letter]), self.left_components.difference([component_letter])), 
                Component(self.n_components+1, self.query + (" & ~" if self.n_components >= 1 else "~" )+component_letter, self.components.union([component_letter]), self.left_components.difference([component_letter])))