import lark
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
    print(value[1])
    res = value[1]
    asignaciones = value[5].find_data('asignacion')
    asign_op = value[5].find_data('asign_op')

    temp = []
    for i in asignaciones :
      temp.append(i.children)
    for i in asign_op:
      temp.append(i.children)
    for i in temp:
      print(i[2])
    return res
  


  def asignaciones_scope(self,value):
   # print(currFunction, "asignaciones",value[0])
    # for i in value[0]:
    #   print(i)
    res = value[0]
    return res
