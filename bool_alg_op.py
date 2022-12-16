from component import Component

class BooleanAlgOp():
    def __init__(self, query):
        self.components_dict = {}
        self.components_ref = []
        self.initialize(query)
       
    def initialize(self, query):
        """Primero extrae los datos necesarios de la query y luego procesa esta, devolviendo al final un diccionario con las llaves como Componentes CC y valores como instancias de la clase Component Ej (0 1 0) (1 0 1)"""
        query = BooleanAlgOp.process_query_parenthesis(query)
        print("estoy aqui")
        print(query)
        
        query_set = set(query.split()).difference(["&", "|", "~", "(", ")"])
        self.components_ref = []
        
        for query_token in query_set:
            self.components_ref.append(query_token)
            
        self.components_dict = BooleanAlgOp.create_components_dict(self.components_ref) # Diccionario con llaves: terminos, valores: indice en array. Al termino t1 le corresponde el indice 1 en el array components_refs
    
    @staticmethod
    def process_query_parenthesis(query:str):
        last_query = ""
        for i in range(len(query)):
            last_query+= query[i]
            
            if query[i] == "(" or query[i] == "~":
                last_query+= " "
            if i + 1 < len(query) and query[i+ 1] == ")":
                last_query+= " "     
            
        return last_query
    
    @staticmethod
    def process_query_and_get_fndc(query:str):
        """Primero extrae los datos necesarios de la query y luego procesa esta, devolviendo al final un diccionario con las llaves como Componentes CC y valores como instancias de la clase Component Ej (0 1 0) (1 0 1)"""
        query = BooleanAlgOp.process_query_parenthesis(query)
        
        query_set = set(query.split()).difference(["&", "|", "~", "(", ")"])
        components_ref = []
        
        for query_token in query_set:
            components_ref.append(query_token)

        print("estoy aqui")
        print(components_ref)
            
        return BooleanAlgOp.get_fndc(len(query_set), query, components_ref=components_ref)
    @staticmethod
    def get_fndc(n_components: int, query: str, components_ref: list = None):
        """Dada una query, su cantidad de componentes y sus componentes devuelve un diccionario con las cc"""
        components_set = set(components_ref)    # Conjunto para tener todos los terminos sin repetir
        components_dict = BooleanAlgOp.create_components_dict(components_ref) # Diccionario con llaves: terminos, valores: indice en array. Al termino t1 le corresponde el indice 1 en el array components_refs
        component_list = BooleanAlgOp.extract_query_cc(query.split(), components_dict, components_set) # Aqui obtengo todas las CC y las agrego en una lista para luego quitar las que esten repetidas
        
        cc_final_list = []
        for component in component_list:
            for component_eval in component.eval():
                cc_final_list.append(component_eval)
                
        cc_final_dict = Component.reduce(cc_final_list, components_dict) # Aqui me deshago de las componentes repetidas
        
        return cc_final_dict
        
    @staticmethod
    def create_components_dict(components_ref):
        """Creando diccionario donde la llave es el termino y el valor el indice que le corresponde en el array. Al indice t1 le corresponde el indice 1, al indice t2 el indice 2 en el array....termino tn => indice n"""
        components_dict = {}
        for i, token in enumerate(components_ref):
            components_dict[token] = i
        return components_dict
        
        
    @staticmethod
    def extract_query_cc(query: str, components_dict: dict, components_set: set):
        """Se Procesa la query y se extraen las CC y voy creando las clases del tipo Component, para luego expandir cada CC que es un Component y obtener una fndc"""
        temp_comp = set()   # Conjunto para ir guardando temporalmente todos los terminos que vaya encontrando
        temp_query: str = ""    # Str para ir guardando la cadena de la cc que este actualizando actualmente
        beg = 0
        end = 0
        components_amount = 0
        
        cc_list = []
        
        for index in range(len(query)):
            if query[index] == " ":
                end = index
                continue
            if query[index] == "&": # Si viene un & continuo y sigo buscando al proximo termino
                temp_query += " " + query[index]
                end = index
                continue
            if query[index] == "|": # Si viene un | Creo una CC
                temp_cc = BooleanAlgOp.create_cc(" ".join(query[beg:end+1]), len(temp_comp), temp_comp, components_set) # Creando CC
                cc_list.append(temp_cc)
                beg = index+1
                temp_comp = set()
                temp_query = ""
                end = index
                continue
            
            if query[index] == "(": # Si abro parentesis reinicio todo
                beg = index+1
                temp_comp = set()
                temp_query = ""
                end = index
                continue
            
            if (query[index]) in components_dict: # Agregando token a la CC que se esta generando actualmente
                if temp_query != "":
                    temp_query += " " + query[index]
                temp_query += query[index]
                temp_comp = temp_comp.union([query[index]])
                end = index
                
            if index == len(query) - 1: # Si llego al final de mi query, analizo el caso, si tengo alguna cc que aun no se ha procesado, entonces la incluyo en esta parte del codigo
                if temp_query != "":
                    temp_cc = BooleanAlgOp.create_cc(" ".join(query[beg:end+1]), len(temp_comp), temp_comp, components_set) # Creando CC
                    cc_list.append(temp_cc)
                    beg = index
                    temp_query = ""
                    temp_comp = set()
                    end = index
                    
        return cc_list # Devuelvo una lista con todas las cc (pertenecientes a la clase Component)
                
    @staticmethod
    def create_cc(temp_query: str, components_amount: int, temp_comp, components_set:set):
        """Se Crea una clase Component \ntemp_query: pedazo de cadena que representa a la CC actual\ncomponents_amount: cantidad de componentes en la cc actual\nactual_comp: conjunto con todos los terminos que se encuentran en la CC\ncomponents_set: conjunto con todos los terminos, se utiliza para hallar la diferencia con los q se encuentran en el actual y quedarme con los que faltan"""
        return Component(components_amount, temp_query, components=temp_comp, left_components=components_set.difference(set(temp_comp)))