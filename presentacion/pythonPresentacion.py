#funciones presentacion en python

def factorialRec(bn):
    if(n==0): 
        return 1;
    else:
        return n*factorialRec(n-1);
        
def cuadrado(n):
    return n*n

def infinito(n):
    return infinito + 1

def tres(n):
    return 3

def sumar(lista):
    if len (lista)==0:
        return 0
    return lista[0] + sumar(lista[1:])
    
def invertir(lista):
    if len (lista) == 1:
        return lista[0]
    invertir (lista[0])++lista[1]
    
def igualLista(lista):
    if lista1 == lista2:
        return true

def listaOrdenada(lista):
    if len (lista) == 1:
        return true
    if lista[0]<=lista[1] and listaOrdenada[1:]:
        return true
    
def mostrarUbicación(lista,elemento):
    for i in range(0,len(lista)):
        if(lista[i] == elemento):
            return i
    
def mayor(lista):
    if len (lista) ==1:
        return lista[0]
    if lista[0]>mayor(lista[1]):
        return lista[0]
    return mayor(lista[1:])

def contarpares(lista):
    if len (lista) == 0:
        return 0
    else:
        return len ([x for x in (lista) if x % 2 == 0])

def cuadrados(lista):
    if len (lista) == 0:
        return 0
    else:
        return [x*x for x in lista]
    
def divisible(n):
    if x % y == 0:
        return true
 
def divisibles(n):
    return [y for y in [1:] if x divisible y]
    
def esPrimo(n):
    return len (divisibles n) <=2
    
def primos(lista):
    primos n = [x for x in [1..n] if esPrimo x]
        