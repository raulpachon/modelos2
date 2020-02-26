archivo = open("prueba.txt", "r+")
archivo.seek(0)
print(archivo.read())
archivo.close()
