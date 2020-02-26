archivo = open("prueba.txt", "r+")
for x in range(255):
  caracter=chr(x)
  archivo.write(caracter)
archivo.close()
