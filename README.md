# SEMINARIO DE TRADUCTORES DE LENGUAJES 2
***Alumno:*** Ricardo David López Arellano  
***Profesor:*** MICHEL EMANUEL LOPEZ FRANCO 

A continuación se muestran las fases desarrolladas a lo largo del curso para la creación de un compilador básico creado en el lenguaje de programación C++.

## Analizador Léxico
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Módulo 1 Analizador léxico
El léxico de un lenguaje de programación u otro lenguaje usado en la informática, está constituido 
por todas las palabras y símbolos que lo componen. En los lenguajes de programación el léxico 
lo constituyen todos los elementos individuales del lenguaje, denominados frecuentemente como 
“tokens”.
Tiene como propósito, agrupar un texto ingresado en diferentes tipos de patrones que conforman 
las unidades léxicas como identificadores, palabras reservadas, operadores y símbolos, entre otros.
Dichas unidades son representadas internamente con un número, los cuales son llamados cuando se 
comienza a analizar la cadena de entrada.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Para la codificación de la primera parte del compilador se establecieron 23 tokens; según el tipo de símbolo se le asignó un número internamente con el fin de conocer el estado que cada uno tenía en el autómata creado (siguiente Caracter, siguiente Estado, Aceptación).
A su vez a cada token se le asigna una cadena que será la mostrada en la impresión de pantalla para reconocer las unidades léxicas.  

*Reconoce los siguientes símbolos:*

•Identificadores= letra (letra|digito)* 

•Entero= digito+ 

•Real= entero.entero

•Operador de adición: + | -

•Operador de multiplicación: * | /

•Operador de asignación: =

•Operador relacional: < | > | <= | >= | != | ==
•Operador And: &&

•Operador Or: ||

•Operador Not: !

•Parentesis: ( , )

•Llave: { , }

•Punto y coma: ;

•Además de las siguientes palabras reservadas: if, while, return, else, int, float

![Captura1](https://user-images.githubusercontent.com/75290686/186078769-e2d80094-ab56-4292-833d-a2db6beb730b.PNG)

![Captura2](https://user-images.githubusercontent.com/75290686/186078834-bc2ad2ed-83b5-44a1-a435-2c2bca16c92f.PNG)

![Captura3](https://user-images.githubusercontent.com/75290686/186078906-4b785d08-79ed-4c93-8538-863a437f6837.PNG)

## Analizador Sintáctico
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Módulo 2 Analizador sintáctico
El analizador sintáctico es la siguiente fase de un compilador, después del analizador léxico.
Su principal función consiste en la descomposición y transformación de las entradas en un 
formato utilizable para su posterior procesamiento. Se analiza una cadena de instrucciones 
en un lenguaje de programación y luego se descompone en sus componentes individuales. 
Este utiliza los tokens obtenidos del analizador léxico que sirven como caracteres de 
entrada para el analizador sintáctico.
Tiene como propósito, manejar la gramática de los datos de entrada, realiza un análisis 
sintáctico de éstos y como regla general crea un árbol de sintaxis (árbol de análisis), y esto 
se puede utilizar para el procesamiento posterior de los datos, por lo tanto, el analizador es 
el software que comprueba, procesa y reenvía las instrucciones del código fuente.

### _Mini analizador sintáctico_:
La creación de este submódulo hace uso del analizador sintáctico LR, el cual se basa en una pila de enteros que es la que va guardando el estado y las reglas con forme se va analizando la cadena hasta que se llega a un estado de aceptación.

Generar un algoritmo para analizar los Ejercicios 1 y 2 del archivo

#### Ejercicio 1 hola+mundo

https://user-images.githubusercontent.com/75290686/196600124-ecb2fbf0-4ad5-4943-85c9-3246cda1fbbf.png

##### Ejercicio 2 a+b+c+d+e+f

https://user-images.githubusercontent.com/75290686/196600232-9b1b9350-1a97-4c1e-8c9a-80f6b87b8f85.png
https://user-images.githubusercontent.com/75290686/196600389-66303109-fe68-4796-b631-c074ceac14db.png
