/*
Este es un programa que lee un arreglo de 10 elementos enteros y obtiene la diferencia
entre dos elementos consecutivos del arreglo.
*/

include <iostream>
#include <cmath>
using namespace std;
int main()
{
    int a[10];
    int * ap=a;
    int i, dif, may=0,pos;
    cout<<"\nIntroduzca 10 valores enteros\n\n";
    for(i=0;i<10;i++)
    {
        cout<<" dato "<<i<<" : ? ";
        cin>>*(ap+i);
    }
    for(i=0;i<9;i++)
    {
        dif=abs((ap+ i)-(ap+(i+1)));
        if(dif>may)
        {
            may=dif;
            pos=i;
        }
    }
    cout<<"La diferencia mayor es "<<may<<" entre el dato "<<pos<<" y "<<pos+1<<endl;
    return 0;
}
