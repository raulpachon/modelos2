num= int(input("ingrese un numero entre 1 y 7"))
diccionario = {1:"lunes",2:"martes",3:"miercoles",4:"jueves",5:"viernes",6:"sabado",7:"domingo"}
if num<=7 and num>=1:
  print(diccionario.get(num))
else:
  print("entrada incorrecta")
