from getpass import getpass
import paramiko
import subprocess

HOST = '10.0.0.17'
PUERTO = 22
USUARIO = 'ubuntu'
password="55568016"
print (HOST)

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(HOST, username="ubuntu", password="55568016")



sftp = ssh_client.open_sftp()
sftp.put('/home/kjas/Escritorio/4-so.py', '/home/ubuntu/Downloads/4-so.py')
sftp.close()




comando = 'echo %s | sudo -S python /home/ubuntu/Downloads/4-so.py' % password
entrada, salida, error = ssh_client.exec_command(comando)
print salida.read()
ssh_client.close()
