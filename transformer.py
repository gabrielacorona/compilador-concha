import lark
from lark import Tree, Transformer, v_args
from semanticCube import *

cube = semanticCube()
functions = {}

class TransformerLark(Transformer):
  def global_scope(self,value):
    functions["global"] = {"tipo" :"void" , "vars" :{}}
    func_var_table = functions["global"]

    declaraciones = value[3].find_data('declaracion')
    temp = []
    for i in declaraciones :
      temp.append(i.children)

    for i in temp:
      func_var_table['vars'] = {i[1].value : {"tipo" : i[0].value, "valor": -9999}}

    return Tree('programa', value)
  
  def functions_scope(self,value):
    #print(value)
    # sacando operaciones dentro de scope para cubo semántico
    operaciones =[]
    temporalOp = value[6].find_data('asign_op')
    for i in temporalOp:
      operaciones.append(i)
    
    escritura =[]
    temporalOp = value[6].find_data('escritura')
    for i in temporalOp:
      escritura.append(i)

    # sacando tabla de símbolos
    functions[value[2].value] = {"tipo" : value[0].value, "vars": {}}
    func_var_table = functions[value[2]]

    declaraciones = value[6].find_data('declaracion')
    temp = []
    for i in declaraciones :
      temp.append(i.children)
    
    func_var_table['vars'] = []
    for i in temp:
      func_var_table['vars'].append( {i[1].value : {"tipo" : i[0].value, "valor": -9999}})
      for x in i:
        if isinstance(x,lark.tree.Tree):
          func_var_table['vars'].append( {i[1].value : {"tipo" : "arr_" + i[0].value  , "valor": [], "lim": x.children[1].value}})
    
    self.validateSemanticCube(operaciones)
    




  def validateSemanticCube(self, operaciones):
    astTree = []
    for i in operaciones:
      astTree.append(i.children)
    for i in astTree:
      if isinstance(i[2],lark.tree.Tree):
        tempCube = i[2].children
        cube.validateType(tempCube)
    print()
    print("cambio de func")









#TODO
# checa si está en tabla de simbolos
# si sí está agarra los tipos y manda a validación
# si no, manda error de not declared
# si es valido empieza a meter a stacks
# agregar a gramática input
# "        "    "      comentarios jiji
# operaciones de bools
# operaciones de strings