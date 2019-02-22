#include<iostream>
using namespace std;
int main(){
//char palabra[]={'H','o','l','a',' ','e','s','t','a',' ','e','s',' ','u','n','a',' ','c','a','d','e','n','a','\0'};
char auxiliar,palabra[]="esta es una cadena de prueba";
int largo=0;
 while (palabra[largo]!='\0') largo++;

 // if(palabra[5]=='\0')cout<<largo;
  char *der=&palabra[largo];
	char *izq=&palabra[0];
    	for(int i=0;i<(largo/2);i++){
       		auxiliar = *izq;
        	*izq=*der;
        	*der=auxiliar;
        	izq++;
        	der--;
    	}

    for(int i=1;i<=largo;i++)cout<<palabra[i];


}
