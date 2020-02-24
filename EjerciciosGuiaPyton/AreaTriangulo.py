base = float(input('ingrese el tamaño de la base del triangulo:'))
altura = float(input('ingrese el tamaño de la altura del triangulo:'))
print(f"la area del triangulo es : {(base*altura)/2}  unidades cudradas")
13. Escribir un programa que calcule el equivalente en pies de una longitud de x metros
sabiendo que 1 metro equivale a 39.27 pulgadas y 12 pulgadas equivalen a 1 pie

tiempo = int(input('ingrese un numero de metros:'))
print(f"la cantidad de pies equivalente a la cantidad de metros ingresados es: {(tiempo*39.27)/12} pies")

______________________________________

31 Escribir un programa que genere las tablas de multiplicar de un número introducido por el
teclado.

numero = int(input('ingrese un numero: '))
LIMITE = 12
contador = 1
print('su tabla de multiplicar es: ')
while contador <= LIMITE:
    resultado = contador * numero
    print("{} x {} = {}".format(numero, contador, resultado))
    contador = contador + 1
_____________________________
34. Escribir un programa que pida un número y si el que se introduce por el teclado es diferente
de cero (0) vuelva a solicitarlo, el programa debe mostrar en cada iteración cuanto es la
suma de los valores absolutos de los pares y de los impares.

numero = int(input('ingrese un numero entero: '))
contador = 0
while numero!=0:
    
    if numero%2==0 and numero<0:
        contador = contador + (-1)*numero
    elif numero%2==0 and numero>0:
        contador = contador + numero
    print("el acumulado de los numero pares ingresados es: ", contador)    
    numero = int(input('ingrese un numero entero: '))
 __________________________________

Escribir un programa que llene una lista con los veinte primeros números pares y calcule su
suma.
pri20=[(x)*2 for x in range(20)]
c=0
for i in (pri20):
   c=c+i
print(c)

_______________________
Escribir un programa que divida todos los elementos de una matriz M (3,4) por el elemento
situado en la posición 2,2 .

matriz=[[1.0,2.0,3.0,4.0], [11.0,22.0,31.0,41.0], [14.0,25.0,36.0,47.0]]
matriz1=matriz.copy()
muneroselect=matriz[1][1]
for i in range(3):
    for j in range(4):
        matriz[i][j]=matriz[i][j]/muneroselect
        print(matriz[i][j])
print('la operacion de la matriz por el elemto M(2,2) es \n',matriz)
_______________________

57.Escribir un programa que cuente las mayúsculas de una cadena de caracteres.

frase=(input("Introduce una frase para poder contar las mayusculas: "))
 
def contarMayus(frase):
	cont=0
	for i in frase:
		if i !=i.lower():
			cont+=1
 
print(cont)
____________________________________
62. Escribir un programa que compare dos cadenas de caracteres y nos diga si son idénticos o no.

myString = input("ingrese una palabra: ")

# En este caso imprime "Es Palindroma"
if myString == ''.join(reversed(myString)):
    print("Es Palindroma")
else:
    print("No es Palindroma")

Escribir un programa que transforme números entre 0 y 999 a números romanos (usar
funciones).
import math
Unidad=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
Decena=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
Centena=["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
def numromano():
  N=int(input("Ingresa numero entero entre 0 y 999\n"))
  u= N % 10
  d=int(math.floor(N/10))%10
  c=int(math.floor(N/100))
  if(N>=100): 
    print(Centena[c]+Decena[d]+Unidad[u])
  else:
    if(N>=10):
      print(Decena[d]+Unidad[u])
    else:
      print(Unidad[N])
numromano()
________________________
Escribir un programa que, mediante una función, calcule el resultado de restar el doble de unnumero a su cuadrado. 

 N=int(input("Ingrese un numero\n"))
def operar(N):
  res=N*N-2*N
  print("el resultado de restar el doble al cuadrado del numero ingresado es :",res)
operar(N)
# recursividad fibonacci
def fibo(n) :
    if n<=2:return 1
    return fibo(n-1)+fibo(n-2)
_____________________
# recursividad potencia
def pot(n,m) :
    if m==0: return 1
    if m==1: return n
    if return pot (m,m-1)*n
___________________________
