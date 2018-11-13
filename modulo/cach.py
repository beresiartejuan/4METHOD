#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import choice
capchat = """
xD��&������U5����X
&�h[`��ڧ��Ie]�1�M
��bU�!���l��8G|�ohpy����]'n��|bM�� �����/接�=�bN���l�n�Xk����6w�wA����W�GN$�<�
��[�Y1F�� ��8G|�ohpy����]'n��|bM�� �����/接�=�bN���l�n�Xk����6w�wA����W�GN$�<�
��[�Y1F�� |�ohpy����]'n��|bM�� �����/接�=�bN���l�n�Xk����6w�wA����W�GN$�<�
��[�Y1F�� jljcjdnnjdcnjdncjdncjdncsjcnpeihihfrfibrfrfkjdbfjbdkjbfjbjkdfbvjdbjdfbvjfdf
"""
archivo = raw_input("Ingresa la ruta del archivo: ")
ciclos = int(raw_input("Cuantas veces quiere que se sobreescriba?: "))
contador = 1

while contador <= ciclos:
	p = capchat.join([choice(capchat) for i in range(20)])
	f = open(archivo, 'w')
	f.write(str(capchat + p))
	f.close()
	contador += 1
  
print "---- El archivo no se puede volver a recuperar ----"
