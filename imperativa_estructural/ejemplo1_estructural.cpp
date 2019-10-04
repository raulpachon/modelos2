/*este programa es un ejemplo de programacion estructurada 
el programa determina el valor total a pagar a un conjunto de trabajadores, deacuerdo 
con el numero de horas trabajas y las siguientes condiciones:
si la cantidad de horas trabajadas es mayor a 40 horas la tarifa se incrementa 
en un 15% para las horas extras. 

*/
#include <iostream>

using namespace std;


int main(){
	int n;
	float h, tar;
	cout<<"\n  ingrese el numero de trabajadores : \n \n ";
	cin>>n;
	 float sueldos[n];
	cout<<"\n  ingrese la tarifa de la hora de trabajo: \n \n $";
	cin>>tar;
	
	for(int i=0 ; i<n;i++){
	cout<<"\n  ingrese las horas trabajadas"<<" por el trabajador #"<<(i+1)<<" : \n \n ";
	cin>>h;
	
	if(h>40){
		sueldos[i]=(40*tar)+((h-40)*tar*1.15);
		
	}else{
		sueldos[i]=h*tar;
	}
	}
	
	for(int i=0 ; i<n;i++){
	cout<<"\n el salario del trabajador #"<<(i+1)<<" es de $ "<<sueldos[i]<<endl<<endl;
   } 
  return 0;
}

