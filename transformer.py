from lark import Tree, Transformer, v_args

currFunction = ""

class TransformerLark(Transformer):
  
  def __init__(self):
    self.functions = {}
  
  def global_scope(self,args):
    self.functions["global"] = {"tipo" :"void" , "vars" :{}}
    func_var_table = self.functions["global"]

    declaraciones = args[3].find_data('declaracion')
    temp = []
    for i in declaraciones :
      temp.append(i.children)

    for i in temp:
      # for x in i :
      #   if(x.value):
      #     print(x.value)
      #   else:
      #     print("puto tree")
      #print(i[0].value)
      func_var_table['vars'] = {i[1].value : {"tipo" : i[0].value, "valor": -9999}}

    #print(self.functions)
    return Tree('programa', args)
  
  def functions_scope(self,value):
    self.functions[value[2].value] = {"tipo" : value[0].value, "vars": {}}
    func_var_table = self.functions[value[2]]

    declaraciones = value[6].find_data('declaracion')
    temp = []
    for i in declaraciones :
      temp.append(i.children)
    
    func_var_table['vars'] = []
    for i in temp:
      for x in i:
        print(x)
      func_var_table['vars'].append( {i[1].value : {"tipo" : i[0].value, "valor": -9999}})
    res = 1
    return res

  def asignaciones_scope(self,value):
    res = value[0]
    return res
