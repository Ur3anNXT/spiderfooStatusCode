#!/bin/python3

import subprocess

#Introduzco los datos
domain = input("Introduce un dominio: ")

#Ejecutamos el comando
data = subprocess.run('curl -I '+domain,shell=True, text=True, capture_output=True)
out = data.stdout

#Separamos el texto con espacios
outServer = out.split(" ")

#Seleccion el codigo de estado
server = outServer[1]

#imprimo el codigo de estado
print(server)