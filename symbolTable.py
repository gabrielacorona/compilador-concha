import lark
from lark import Tree, Transformer, v_args
import pprint

pp = pprint.PrettyPrinter(indent=4)

class symbolTable:
    def __init__(self):
        self.functions={}
    

    def populateSymbolTable(self,value):
        self.functions[value[2].value] = {"tipo" : value[0].value, "vars": {}}
        func_var_table = self.functions[value[2].value]
        
        declaraciones = value[6].find_data('declaracion')
        temp = []
        for i in declaraciones :
            temp.append(i.children)
        
        func_var_table['vars'] = {}
        currVarDic = func_var_table['vars']
        for i in temp:          
            if i[1].value in currVarDic:
                print(i[1].value,"variable already declared primer for")
            else:
                currVarDic[i[1].value] = {"tipo" : i[0].value, "valor": -9999}
            #para arreglos y su capacidad
            for x in i:
                if isinstance(x,lark.tree.Tree):
                    currVarDic[i[1].value] = {"tipo" : "arr_" + i[0].value  , "valor": [], "lim": x.children[1].value}

        self.lookupVars("saludarConEdad","ab")
    
    def lookupVars(self,scope,key):
        dictValues = self.functions[scope]
        scopeVars = dictValues["vars"]

    def printSymbolTable(self):
        print("simp table")
        pp.pprint(self.functions)