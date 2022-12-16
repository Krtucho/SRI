from component import Component

class BooleanAlgOp(): 
    @staticmethod
    def process_query_and_get_fndc(query:str):
        """Primero extrae los datos necesarios de la query y luego procesa esta, devolviendo al final un diccionario con las llaves como Componentes CC y valores como instancias de la clase Component Ej (0 1 0) (1 0 1)"""
        query_set = set(query.split()).difference(["&", "|", "~", "(", ")"])
        components_ref = []
        
        for query_token in query_set:
            components_ref.append(query_token)
            
        return BooleanAlgOp.get_fndc(len(query_set), query, components_ref=components_ref)
    @staticmethod
    def get_fndc(n_components: int, query: str, components_ref: list = None):
        """Dada una query y """
        components_set = set(components_ref)
        components_dict = BooleanAlgOp.create_components_dict(components_ref) # Diccionario con llaves: terminos, valores: indice en array. Al termino t1 le corresponde el indice 1 en el array components_refs
        component_list = BooleanAlgOp.extract_query_cc(query.split(), components_dict, components_set)
        
        cc_final_list = []
        for component in component_list:
            for component_eval in component.eval():
                cc_final_list.append(component_eval)
                
        cc_final_dict = Component.reduce(cc_final_list, components_dict)
        
        return cc_final_dict
        
    @staticmethod
    def create_components_dict(components_ref):
        components_dict = {}
        for i, token in enumerate(components_ref):
            components_dict[token] = i
        return components_dict
        
        
    @staticmethod
    def extract_query_cc(query: str, components_dict: dict, components_set: set):
        temp_comp = set()
        temp_query: str = ""
        beg = 0
        end = 0
        components_amount = 0
        
        cc_list = []
        
        for index in range(len(query)):
            if query[index] == " ":
                end = index
                continue
            if query[index] == "&":
                temp_query += " " + query[index]
                end = index
                continue
            if query[index] == "|":
                temp_cc = BooleanAlgOp.create_cc(" ".join(query[beg:end+1]), len(temp_comp), temp_comp, components_set) # Creando CC
                cc_list.append(temp_cc)
                beg = index+1
                temp_comp = set()
                temp_query = ""
                end = index
                continue
            
            if query[index] == "(":
                beg = index
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
                
            if index == len(query) - 1:
                if temp_query != "":
                    temp_cc = BooleanAlgOp.create_cc(" ".join(query[beg:end+1]), len(temp_comp), temp_comp, components_set)
                    cc_list.append(temp_cc)
                    beg = index
                    temp_query = ""
                    temp_comp = set()
                    end = index
                    
        return cc_list
                
    @staticmethod
    def create_cc(temp_query: str, components_amount: int, temp_comp, components_set:set):
        return Component(components_amount, temp_query, components=temp_comp, left_components=components_set.difference(set(temp_comp)))