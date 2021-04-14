from lark import Tree, Transformer

currFunction = ""

class TransformerLark(Transformer):
  
  def __init__(self):
    self.functions = {}
  
  # def globalScope(self,args):
  #   self.functions["global"] = {"tipo" :"void" , "vars" :{}}
  #   print(self.functions["global"])
  #   return Tree('programa', args)
  
  # def functionsScope(self,args):
  #   print(args)
  #   return 

