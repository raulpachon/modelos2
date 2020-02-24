matriz=[[1.0,2.0,3.0,4.0], [11.0,22.0,31.0,41.0], [14.0,25.0,36.0,47.0]]
matriz1=matriz.copy()
muneroselect=matriz[1][1]
for i in range(3):
    for j in range(4):
        matriz[i][j]=matriz[i][j]/muneroselect
        print(matriz[i][j])
print('la operacion de la matriz por el elemto M(2,2) es \n',matriz)

