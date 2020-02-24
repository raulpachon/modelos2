myString = input("ingrese una palabra: ")

# En este caso imprime "Es Palindroma"
if myString == ''.join(reversed(myString)):
    print("Es Palindroma")
else:
    print("No es Palindroma")

