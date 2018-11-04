#!/usr/bin/env python 
# -*- coding: utf-8 -*-
logo = """
         _
        | |
        | |
    _   | |
   | |  | |
   | |__| | <Python>
   |______| <Terminal 0.1>
"""

import os, pwd, time, getpass
try:
	import hashlib
except Exception as e:
	os.system("pip install hashlib")
	import hashlib

salir = False
nombre_usuario = pwd.getpwuid( os.getuid() )[ 0 ]
mensaje_personalisado = ""

if os.path.exists(".terminal"):
	con = open(".terminal/pass.txt").read()
	password = getpass.getpass("Ingrese su contraseña: ")
	password = hashlib.sha1(password)
	if con == password.hexdigest():
		pass
	else:
		print("no eres " + nombre_usuario  + ".")
		exit()
else:
	os.mkdir(".terminal")
	contrase = getpass.getpass("Ingrese su contraseña: ")
	contrase = hashlib.sha1(contrase)
	_a = open(".terminal/pass.txt", "w")
	_a.write(contrase.hexdigest())
	_a.close()
	pass

print(logo)

while not salir:
	print("-" * 29)
	input_user = raw_input(mensaje_personalisado)
	try:
		os.system(input_user)
	except Exception as e:
		print e
	if input_user == "exit":
		salir = True
