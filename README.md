![alt text](https://github.com/gabrielacorona/compilador-concha/blob/main/Logo.jpeg)
# Compilador Concha
'Concha' language is a high-level programming language that can be used for object oriented programming. The main characteristic of this language is that the syntax expressions are in spanish so that any spanish speaker can understand and learn the language.

## Main Objective
Democratize the process of learning a programming language by removing the language barrier as most popular programming languages use english words for their syntax.

## Primer avance
In this first revision we implemented the Lexical/Syntactical analysis of our language, introducing the Tokens and Grammar used to parse the syntax of any program written in Concha in the file 'concha.py' . Additionally, the railroad diagrams are attached in this repository that display graphically the BNF grammar we designed for our programming language.

## Example of program written in Concha
```python
programa miPrimerPrograma : var ab, bb, bc : entero;
{
     cadena ab;
     entero myArr[30];
     ab = "hola";
     myArr[2] = 3;
     si(2 != 2){
          ab = 2*2;
     } sino {
          escribir(2 * 3);
     };
     por(entero a = 4; a < 4 ; a = a + 1){
          ab = a + 3;
     }
     saludarConEdad(22, "Caro");
}

funcion saludarConEdad(entero edad, cadena nombre){
     escribir("hola", nombre, "tienes ", edad, "años");
}