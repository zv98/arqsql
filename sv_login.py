import socket
from conect import *
import bcrypt
import threading
import sqlite3
import hashlib


def iniciar(sock,cont,serv):
    largo = len(cont+serv)
    temp = str((largo).zfill(5))
    respuesta = temp + serv + cont
    print(respuesta)
    sock.sendall(respuesta.encode())
#def recibir(sock, addr):
print("Ingresando a la cuenta de usuario")
#while socket.recv(4096):
def login(datos):
    #datos = socket.recv(4096)
    #print(datos)
    #if datos.decode('utf-8').find('login'):
    #datos = datos[10:]
    print("login")
    print(datos)
    target = datos.decode()
    data = target.split()
    email = data[0]
    password = data[1]
    #login(email,password)
#else:
#    respuesta = "error"
#        temp=llenado(len(respuesta))
#        socket.sendall(bytes(temp+respuesta,'utf-8'))
    #val = 0
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
            #val=1
            print("Ha ingresado con éxito a su cuenta")
            respuesta2='login'+mail+passw
            temp=llenado(len(respuesta2))
            iniciar(sock,"iniciando sesion","login")
            #socket.sendall((temp+respuesta2).encode())
        else:
            respuesta2 = "login" + "no_existe_usuario"
            temp=llenado(len(respuesta2))
            iniciar(sock,"datos incorretos","login")
            #socket.sendall((temp+respuesta2).encode())
#else:
#    respuesta2 = "servicio incorrecto"
#    temp=llenado(len(respuesta2))
#    socket.sendall(bytes(temp+respuesta2,'utf-8'))
#print(respuesta2)
#temp=llenado(len(respuesta2))
#s.sendall(bytes(temp+respuesta2,'utf-8'))

#if (val!=1):
#    print("Contraseña incorrecta")
if __name__ == "__main__":
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', 5000)
        print('connecting to {} port {}'.format(*server_address))
        sock.connect(server_address)
    except:
        print("Error de conexion")
    iniciar(sock,"login","sinit")
    s, m = escuchar(sock)
    if s == "sinit" and m[:2] == "OK":
        print("servicio iniciado")
    else:
        print("no se pudo iniciar el servicio")
    while True:
        print("escuchando")
        s, m = escuchar(sock)
        print(s,m)
        if s == 'login':
            login(m,sock)
    print("cerrando")
    sock.close()
