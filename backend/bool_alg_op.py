from component import Component

class BooleanAlgOp():
    @staticmethod
    def get_fndc(n_components: int, query: str, components: list, components_ref: list = None):
        components_dict = create_components_dict()
        component_list = extract_query_cc(query, component_list)
        
        cc_final_list = []
        for component in component_list:
            for component_eval in component.eval():
                cc_final_list.append(component_eval[1])
                
        cc_final_dict = Component.reduce(cc_final_list)
        
    @staticmethod
    def extract_query_cc(query: str, components_dict: dict):
        temp_comp = set()
        temp_query: str = ""
        beg = 0
        end = 0
        components_amount = 0
        
        cc_list = []
        
        for index in range(len(query)):
            if query[index] == " ":
                continue
            if query[index] == "&":
                continue
            if query[index] == "|":
                temp_cc = create_cc(beg, end, temp_query, components_amount, temp_comp) # Creando CC
                cc_list.append(temp_cc)
                beg = index
                temp_comp = []
                temp_query = ""
                continue
            
            if query[index] == "(":
                beg = index
                temp_comp = []
                temp_query = ""
                continue
            
            if components_dict.__contains__(query[index]): # Agregando token a la CC que se esta generando actualmente
                temp_query += query[index]
                temp_comp = temp_comp.union(query[index])
                
            if index == len(query) - 1:
                if temp_query != "":
                    create_cc(beg, end, temp_query, components_amount, temp_comp)
                    cc_list.append(temp_cc)
                    beg = index
                    temp_query = ""
                    temp_comp = []
                
    @staticmethod
    create_cc(temp_query: str, components_amount: int):
        Component(components_amount, temp_query, )