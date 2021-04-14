
from lark import Tree, Transformer, v_args

currFunction = ""

class TransformerLark(Transformer):
  
  def __init__(self):
    self.functions = {}
  
  # def globalScope(self,args):
  #   self.functions["global"] = {"tipo" :"void" , "vars" :{}}
  #   print(self.functions["global"])
  #   return Tree('programa', args)
  
  def functions_scope(self,value):
    self.currFunction =  value[1]
    print("funcion ",value[5].pretty())
    res = value[0]
    res = value[5]
    
    # Tree(palabra,json) crea una nueva layer de la tree, no nos sirve en este caso creo
    # test = Tree("asignacion", res)
    # test2 = Tree("asign_op", res)
    # print("test1", currFunction, test)
    # print()
    # print("test2", currFunction, tes2)
    return res

  def asignaciones_scope(self,value):
    #print(currFunction, "asignaciones",value[0])
    # for i in value[0]:
    #   print(i)
    res = value[0]
    return res
