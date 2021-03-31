
# LittleDuck2020
# Herramienta que se está usando : Lark
# https://github.com/lark-parser/lark
# }

from lark import Lark


gramatica = """
     programa : PROGRAMA ID COLN vars bloque
               |PROGRAMA ID COLN bloque
     vars : VAR ID PTO COLN tipo
               | VAR ID COLN tipo
     tipo : NUMBER 
     bloque : LKEY estatuto RKEY
     estatuto : asignacion 
               | condicion 
               | escritura
     asignacion : ID EQ expresion PTOCOM
     escritura : PRINT LPARENS expresion RPARENS PTOCOM
               | PRINT LPARENS STRING RPARENS PTOCOM
               | PRINT LPARENS STRING COMM LBR expresion RPARENS PTOCOM
               | PRINT LPARENS STRING RBR RPARENS PTOCOM
     expresion : exp MOTHN exp 
               | exp LETHN exp 
               | exp NEQ exp 
               | exp
     condicion : IF LPARENS  expresion RPARENS bloque ELSE bloque PTOCOM
               | IF LPARENS  expresion RPARENS bloque PTOCOM
     exp : termino 
               | SUM 
               | SUB 
               | exp
     termino : factor 
               | MUL 
               | DIV 
               | termino
     factor : LPARENS expresion RPARENS 
               | SUM 
               | SUB 
               | constante 
               | SUM constante 
               | SUB constante
     constante : ID 
               | NUMBER
     
     PROGRAMA : "programa"
     ID : "id"
     IF : "si"
     ELSE : "sino"
     VAR : "var"
     PRINT : "escribir"
     WHILE : "mientras"
     STRING : "cadena"
     INT : "entero"
     CTE_I : "constante_ent"
     CTE_F : "constante_flot"
     LPARENS : "("
     RPARENS : ")"
     LKEY : "{"
     RKEY : "}"
     LBR : "["
     RBR : "]"
     SUM : "+"
     SUB : "-"
     MUL : "*"
     DIV : "/"
     EQ : "="
     COLN:":"
     COMM: ","
     PTO: "."
     PTOCOM: ";"
     MOTHN : ">"
     LETHN : "<"
     NEQ : "!="


     %import common.ESCAPED_STRING   -> STRING
     %import common.SIGNED_NUMBER    -> NUMBER
     %import common.CNAME -> NAME
     %import common.LETTER
     %import common.WS_INLINE
     %import common.WS
     %ignore WS
     %ignore WS_INLINE
     %ignore " "

"""





def main():
     fileBuena = open('goodTest.py')
     fileMala = open('badTest.py')
     try:
          lilduck = fileBuena.read()
          print("Prueba GoodTest")
          test(lilduck)
          lilduck2 = fileMala.read()
          print("Prueba BadTest")
          test(lilduck2)
     finally:
          fileBuena.close()
          fileMala.close()
     


def test(test_lilduck1):
     #  sintaxis correcta  contenido de goodTest.py
     # test_lilduck1 ="""
     # program id : {
     #      print(id);
     # }  
     # """

     # sintaxis incorrecta falta  punto y comma y cerrar corchete  contenido de badTest.py
     # test_lilduck2 = """
     # program id : {
     #      print(id)
     # """

     parser = Lark(gramatica,start = "programa")
     try:
          #print(parser.parse(test_lilduck1).pretty())
          if(parser.parse(test_lilduck1)):
               print("Correct Syntax!")
               
     except Exception as ex:
          print("Syntax error in input!")
          print (ex)

if __name__ == '__main__':
     main()