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
