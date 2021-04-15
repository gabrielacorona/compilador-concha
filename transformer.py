from lark import Tree, Transformer, v_args

currFunction = ""

class TransformerLark(Transformer):
  
  def __init__(self):
    self.functions = {}
  
  def global_scope(self,args):
    self.functions["global"] = {"tipo" :"void" , "vars" :{}}
    # print(self.functions["global"])
    # print("globalbb")
    return Tree('programa', args)
  
  def functions_scope(self,value):
    self.functions[value[2].value] = {"tipo" : value[0].value, "vars": {}}
    func_var_table = self.functions[value[2]]

    declaraciones = value[6].find_data('declaracion')
    temp = []
    for i in declaraciones :
      temp.append(i.children)

    for i in temp:
      print("new decl")
      print(i[0].value) ## tipo 
      print(type(i[0].value))
      print(i[1]) ## nombre de var
      func_var_table['vars'] = {i[1].value : {"tipo" : i[0].value, "valor": -9999}}

    print(self.functions)
    res = 1
    return res

  def asignaciones_scope(self,value):
   # print(currFunction, "asignaciones",value[0])
    # for i in value[0]:
    #   print(i)
    res = value[0]
    return res
