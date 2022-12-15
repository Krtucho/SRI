class Component:
    def __init__(self, n_components, query, components:set, left_components:set) -> None:
        self.n_components = n_components
        self.components:set =  components
        self.query = query
        self.lef_components = left_components
        
    def eval(self):
        components_list: list = []
        
        for left_component in self.lef_components:
            compononents = self.add_component(left_component)
            
            for component in compononents[0].eval():
                components_list.append(component)
                
            for component in compononents[1].eval():
                components_list.append(component)
            
        return Component.reduce(components_list)
        
    @staticmethod
    def reduce(components_list: list) -> dict:
        component_dict: dict = {}
        for component in components_list:
            component_dict[component.query] = component
            
        return component_dict
        
    def add_component(self, component_index: int, component_letter: str):
        return (Component(self.components+1, self.query + " "+component_letter, self.components.union(component_letter), self.components.difference(component_letter)), 
                Component(self.components+1, self.query+" & ~"+component_letter, self.components.union(component_letter), self.components.difference(component_letter)))