import socket
from conect import *
import bcrypt
import threading
import sqlite3
import hashlib

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5000)
print('connecting to {} port {}'.format(*server_address))
socket.connect(server_address)

#def recibir(sock, addr):
print("Ingresando a la cuenta de usuario")
while socket.recv(4096):
    datos = socket.recv(4096)
    print(datos)
    if datos.decode('utf-8').find('login'):
        datos = datos[10:]
        target = datos.decode()
        data = target.split()
        email = data[0]
        password = data[1]
        #login(email,password)
    #else:
#    respuesta = "error"
#        temp=llenado(len(respuesta))
#        socket.sendall(bytes(temp+respuesta,'utf-8'))
        val = 0
    #def login(email,password):
        consulta = "select email, pass from usuario"
        respuesta = consultar(consulta)
        enchash = hashlib.md5(password.encode())
        pass2=enchash.hexdigest()
        print("hola")
        for i in respuesta:
            mail = i[0]
            passw = i[1]
            print(passw)
            print(pass2)
            if mail == email and passw==pass2:
                val=1
                print("Ha ingresado con éxito a su cuenta")
                respuesta2='login'+mail+passw
                temp=llenado(len(respuesta2))
                socket.sendall(bytes(temp+respuesta2,'utf-8'))
            else:
                respuesta2 = "login" + "no_existe_usuario"
                temp=llenado(len(respuesta2))
                socket.sendall(bytes(temp+respuesta2,'utf-8'))
    else:
        respuesta2 = "servicio incorrecto"
        temp=llenado(len(respuesta2))
        socket.sendall(bytes(temp+respuesta2,'utf-8'))
#print(respuesta2)
#temp=llenado(len(respuesta2))
#s.sendall(bytes(temp+respuesta2,'utf-8'))

#if (val!=1):
#    print("Contraseña incorrecta")
