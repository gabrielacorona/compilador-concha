
# LittleDuck2020
# Herramienta que se está usando : Lark
# https://github.com/lark-parser/lark
# }

from lark import Lark

gramatica = """
     programa : PROGRAMA ID COLN vars bloque
               | PROGRAMA ID COLN bloque
     vars : VAR varaux COLN tipo PTOCOM
     varaux : ID COMM varaux
            | ID
     tipo : INT | FLOT | STR
     bloque : LKEY bloqaux RKEY
     bloqaux : estatuto bloqaux | estatuto 
     estatuto : declaracion
               | asignacion 
               | condicion 
               | escritura
               | ciclo
     ciclo : wh_loop
     wh_loop : WHILE cond_body bloque
     declaracion : tipo asignacion
     asignacion : ID EQ expresion PTOCOM
     escritura : PRINT LPARENS escaux RPARENS PTOCOM
     escaux : expresion COMM escaux | STRING COMM escaux | expresion | STRING
     expresion : exp MOTHN exp 
               | exp LETHN exp 
               | exp NEQ exp 
               | exp
     condicion : IF cond_body bloque cond_aux
     cond_body : LPARENS expresion RPARENS
     cond_aux : ELSE bloque PTOCOM
               | PTOCOM
     exp : termino
          | termino SUM exp
          | termino SUB exp
     termino : factor
             | factor MUL termino
             | factor DIV termino
     factor : SUM constante
            | SUB constante
            | constante
            | LPARENS expresion RPARENS
     constante : ID 
               | CONSTANTE_ENT
               | CONSTANTE_FLOT
     
     PROGRAMA : "programa"
     IF : "si"
     ELSE : "sino"
     VAR : "var"
     PRINT : "escribir"
     WHILE : "mientras"
     INT : "entero"
     STR : "cadena"
     FLOT : "flotante"
     LPARENS : "("
     RPARENS : ")"
     LKEY : "{"
     RKEY : "}"
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

     %import common.SIGNED_INT    -> CONSTANTE_ENT
     %import common.SIGNED_FLOAT    -> CONSTANTE_FLOT
     %import common.ESCAPED_STRING   -> STRING
     %import common.CNAME -> ID
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
          # print("Prueba BadTest")
          # test(lilduck2)
     finally:
          fileBuena.close()
          fileMala.close()


def test(test_lilduck1):
     parser = Lark(gramatica,start = "programa")
     try:
          if(parser.parse(test_lilduck1)):
               print("Correct Syntax!")
               
     except Exception as ex:
          print("Syntax error in input!")
          print (ex)

if __name__ == '__main__':
     main()