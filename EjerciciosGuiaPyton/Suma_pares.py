numero = int(input('ingrese un numero entero: '))
contador = 0
while numero!=0:
    
    if numero%2==0 and numero<0:
        contador = contador + (-1)*numero
    elif numero%2==0 and numero>0:
        contador = contador + numero
    print("el acumulado de los numero pares ingresados es: ", contador)    
    numero = int(input('ingrese un numero entero: '))
 
