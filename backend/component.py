class Component:
    """Componente Conexa"""
    def __init__(self, n_components: int, query: str, components:set, left_components:set) -> None:
        self.n_components: int = n_components # Numero de terminos(componentes que integran esta cc)
        self.components:set =  components # Conjunto con los distintos terminos que integran la cc
        self.query: str = query  # String con la query que representa a esta cc (sin parentesis)
        self.left_components: set = left_components  # Conjunto con componentes restantes de esta cc...Ej Si ya contiene al termino t1 y t2, pero en la query hay 3 terminos
                                                     # Este set contendra al termino t3 y el set de self.components contendra a t1 y t2
        
    def eval(self):
        """Genera todas las FND restantes de la CC actual agregando las componentes que faltan hasta lograr generar FNDC para cada cc."""
        components_list: list = []
        
        for left_component in self.left_components:
            components = self.add_component(left_component)
            if len(components[0].left_components) == 0:
                components_list.append(components[0])
            else:
                for component in components[0].eval():
                    components_list.append(component)
              
            if len(components[1].left_components) == 0:
                components_list.append(components[1])
            else:  
                for component in components[1].eval():
                    components_list.append(component)
            
        return components_list
        
    @staticmethod
    def reduce(components_list: list, str_components_dict:dict) -> dict:
        """Dada una lista """
        component_dict: dict = {}
         
        for component in components_list:
            index = []
            bool_val = []
            every_cc = component.query.split(" & ")
            for token in every_cc:
                if token[0] == "~":
                    temp_index = str_components_dict[token[1:]]
                    index.append((temp_index, 0))
                    # bool_val.append(0)
                else:
                    temp_index = str_components_dict[token]
                    index.append((temp_index, 1))
                    # bool_val.append(1)
                    
            bool_val = sorted(index, key=lambda x : x[0])
            print(bool_val)
            
            dict_str = ""
            for val in bool_val:
                dict_str += str(val[1])+ " "
            
            if dict_str[len(dict_str) - 1] == " ":
                dict_str = dict_str[:-1]
            component_dict[(dict_str)] = component
            
        return component_dict
        
    def add_component(self, component_letter: str):
        return (Component(self.n_components+1, self.query + " & "+component_letter, self.components.union([component_letter]), self.left_components.difference([component_letter])), 
                Component(self.n_components+1, self.query+" & ~"+component_letter, self.components.union([component_letter]), self.left_components.difference([component_letter])))