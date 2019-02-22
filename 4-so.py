#para ejecutar el codigo es importante estar el el directorio raiz y ejecutalo desde ahi
 #python /home/kjas/Escritorio/sistemasoperativos/4-so.py
from getpass import getpass
import paramiko
import subprocess
import os

operacion2="sudo find . -type f -name *.pdf | xargs cp -t /home/ubuntu/Desktop/pdf"
operacion3="sudo find . -type f -name *.jpg | xargs cp -t /home/ubuntu/Desktop/jpg"



os.system(operacion2)
os.system(operacion3)
os.system("tar -cf /home/ubuntu/Desktop/paqute.tar /home/ubuntu/Desktop/pdf /home/ubuntu/Desktop/jpg")


HOST = "10.0.0.12"
PUERTO = 22
USUARIO = 'kjas'
password="55568016"

print(HOST)
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(HOST, username="kjas", password="55568016")



sftp = ssh_client.open_sftp()
sftp.put('/home/ubuntu/Desktop/paqute.tar', '/home/kjas/Escritorio/paqute.tar')
sftp.close()
ssh_client.close()
