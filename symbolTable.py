import lark
from lark import Tree, Transformer, v_args
class symbolTable:
    def __init__(self):
        self.functions={}
    
    def populateSymbolTable(self,value):
        self.functions[value[2].value] = {"tipo" : value[0].value, "vars": {}}
        func_var_table = self.functions[value[2]]
        

        declaraciones = value[6].find_data('declaracion')
        temp = []
        for i in declaraciones :
            temp.append(i.children)
        
        func_var_table['vars'] = []
        for i in temp:
            func_var_table['vars'].append( {i[1].value : {"tipo" : i[0].value, "valor": -9999}})
            #para arreglos y su capacidad
            for x in i:
                if isinstance(x,lark.tree.Tree):
                    func_var_table["vars"].pop()
                    func_var_table['vars'].append( {i[1].value : {"tipo" : "arr_" + i[0].value  , "valor": [], "lim": x.children[1].value}})
        
        #print(func_var_table)
        #print(self.functions)
        self.lookupVars("saludarConEdad","ab")
    
    def lookupVars(self,scope,key):
        dictValues = self.functions[scope]
        scopeVars = dictValues["vars"]
        #print(scopeVars)
        #print(scopeVars)
        # for i in dictValues:
        #     print(i)
        
