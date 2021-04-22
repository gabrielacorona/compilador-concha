import lark
from lark import Tree, Transformer, v_args
from semanticCube import *
from symbolTable import *

cube = semanticCube()
symbolTable = symbolTable()
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
    symbolTable.populateSymbolTable(value)

#    print("OOP", operaciones)
    self.validateSemanticCube(value[2],operaciones)

  def validateSemanticCube(self,scope, operaciones):
    astTree = []
    for i in operaciones:
      print(i)
      astTree.append(i.children)

    for i in astTree:
      if isinstance(i[2],lark.tree.Tree):
        tempCube = i[2].children
        print("whoareu")
        pp.pprint(tempCube)
        for i in tempCube:
          print("aaa", i.value)
        type, val = symbolTable.lookupVars(scope,i[0])
        # print("tipooo", type)
        cube.validateType(tempCube)
    print()
    print("cambio de func")


#TODO

# si sí está agarra los tipos y manda a validación
# si es valido empieza a meter a stacks
# agregar gramática de declarar y asignar al mismo tiempo ej 'entero h = 10;'
# agregar a gramática input
# "        "    "      comentarios jiji
# operaciones de bools
# operaciones de strings

#whoareu [Token('ID', 'numeroA'), Token('SUM', '+'),
#   Tree('exp', [Token('ID', 'numeroB'), Token('SUM', '+'), Tree('exp', [Token('ID', 'numeroX'), Token('SUM', '+'), Tree('exp', [Token('CONSTANTE_ENT', '9'), Token('SUM', '+'), Tree('exp', [Token('CONSTANTE_ENT', '0'), Token('SUB', '-'), Tree('termino', [Token('CONSTANTE_ENT', '10'), Token('DIV', '/'), Tree('termino', [Token('CONSTANTE_ENT', '8'), Token('MUL', '*'), Token('CONSTANTE_ENT', '7')])])])])])])]
