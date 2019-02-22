#para ejecutar el codigo es importante estar el el directorio raiz y ejecutalo desde ahi
 #python /home/kjas/Escritorio/sistemasoperativos/4-so.py

import os
operacion1="sudo find . -type f -name *.sh  | xargs cp -t /home/kjas/Escritorio/sistemasoperativos/sh/"
operacion2="sudo find . -type f -name *.pdf | xargs cp -t /home/kjas/Escritorio/sistemasoperativos/pdf"
operacion3="sudo find . -type f -name *.jpg | xargs cp -t /home/kjas/Escritorio/sistemasoperativos/jpeg"


os.system(operacion1)
os.system(operacion2)
os.system(operacion3)
os.system("tar -cf /home/kjas/Escritorio/sistemasoperativos/paquete.tar /home/kjas/Escritorio/sistemasoperativos/jpeg/ /home/kjas/Escritorio/sistemasoperativos/sh/ /home/kjas/Escritorio/sistemasoperativos/pdf/")
