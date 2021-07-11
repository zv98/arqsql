#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import threading

from conect import *


#query de la consulta de un paciente mediante rut 
PORT = 5000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1',PORT))
server.listen(1000)

def limpiar(var):
        var = str(var)
        var = var.replace("[","")
        var = var.replace("(","")
        var = var.replace("]","")
        var = var.replace(")","")
        var = var.replace(",","")
        return var

def recibir(sock, addr):
    print("Start Create_dog")
    while True:
        email = sock.recv(4096)
        print(email)
        if email.decode('utf-8').find('cread'):
            #decodificar el email
            email = email[10:]
            target = email.decode()
            email = target.split()
            
        datos = sock.recv(4096)
        if datos.decode('utf-8').find('cread'):
            #decodificar el mensaje
            datos = datos[10:]
            target = datos.decode()
            data = target.split()
        
	#selecciona id del usuario 
        consulta0= f"SELECT idusuario FROM usuario where email='{email[0]}';"
        idusuario1 = consultar(consulta0)
        idusuario1 = limpiar(idusuario1)
        
        #ingresa a la mascota 
        consulta = f"INSERT INTO mascota (nombre, edad, raza, descripcion) VALUES ('{data[0]}','{data[1]}', '{data[2]}','{data[3]}');"
        respuesta = modificar(consulta)
        
        #selecciona id de la mascota 
        consulta0= f"SELECT idmascota FROM mascota where nombre = '{data[0]}' and edad = '{data[1]}' and raza = '{data[2]}' and descripcion = '{data[3]}';"
        idmascota1 = consultar(consulta0)
        idmascota1 = limpiar(idmascota1)

        #relaciona mascota con usuario
        consulta1 = f"INSERT INTO usuariomascota (idusuario, idmascota) VALUES ('{idusuario1[0]}', '{idmascota1[0]}');"
        respuesta1 = modificar(consulta1)
        
        if respuesta and respuesta1 == None:
            menj = "perro anadido con exito"
        else:
            menj = "no se añadio perrito"
        
        
    
        menj='supfu'+str(menj)
        #print(menj)
        temp=llenado(len(menj))  
        #print('tmp: ', temp)
        #print('tmp + respuesta:',temp+menj)
        sock.send(bytes(temp+menj,'utf-8'))


        #   crear mensaje de respuesta
        print("envia3")

    sock.close()
while True:
	sock, addr = server.accept()
	tarea = threading.Thread(target = recibir, args = (sock, addr))
	tarea.start()
