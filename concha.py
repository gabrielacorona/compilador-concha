
# LittleDuck2020
# Herramienta que se está usando : Lark
# https://github.com/lark-parser/lark
# }

from lark import Lark

gramatica = """
     programa : PROGRAMA ID COLN prog_aux
                | PROGRAMA ID COLN prog_aux prog_aux_func
     prog_aux : vars bloque
                | bloque
     prog_aux_func : func prog_aux_func
                    | func
     vars : VAR varaux COLN tipo PTOCOM
     varaux : ID COMM varaux
            | ID
     tipo : INT | FLOT | STR
     bloque : LKEY bloqaux RKEY
     bloqaux : estatuto bloqaux | estatuto
     func : FUNCION ID LPARENS parms RPARENS bloque
     parms : tipo ID COMM parms
            | tipo ID 
     estatuto : call_func
               | declaracion
               | asignacion 
               | condicion 
               | escritura
               | ciclo
     call_func : ID LPARENS call_func_aux RPARENS PTOCOM
     call_func_aux : accepted_params COMM call_func_aux
                    | accepted_params
     accepted_params : constante | STRING
     ciclo : wh_loop | for_loop
     for_loop : FOR LPARENS INT ID EQ exp PTOCOM expresion_comp PTOCOM asign_op RPARENS bloque 
     wh_loop : WHILE cond_body bloque
     declaracion : tipo ID PTOCOM
               | tipo ID arr_idx PTOCOM
     asignacion : asign_op PTOCOM
               | ID arr_idx EQ expresion PTOCOM
               | ID EQ STRING PTOCOM
     asign_op : ID EQ expresion 
     arr_idx : CORCH_LEFT CONSTANTE_ENT CORCH_RIGHT
     escritura : PRINT LPARENS escaux RPARENS PTOCOM
     escaux : expresion COMM escaux | STRING COMM escaux | expresion | STRING
     expresion : expresion_comp
               | exp
     expresion_comp : exp MOTHN exp 
               | exp LETHN exp 
               | exp NEQ exp 
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
     CORCH_LEFT : "["
     CORCH_RIGHT : "]"
     FOR : "por"
     FUNCION : "funcion"

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