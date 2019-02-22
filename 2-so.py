import os
import subprocess

lista =[]

i = subprocess.check_output("ifconfig | grep 'inet' | grep 'broadcast'|awk '{print $2}'", shell=True)
ip=str(i[0:len(i)-3])
ipp=ip[1:len(ip)]
print(ipp)
for x in range(1, 3):
    auxiliar="ping -c 2 "+str(ipp)+str(x)
    if(os.system(auxiliar)==1):
       lista.append(str(ipp)+str(x))
       
for i in lista:
    print("a ver")
    print(lista[i])
