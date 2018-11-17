#!/usr/bin/env python 
# -*- coding: utf-8 -*-
__autor__ = u'Juan Beresiarte'

from math import sqrt

try:
	input = raw_input
except NameError:
	pass

def Tpitagoras(Hipotenusa=None, Cateto1=None, Cateto2=None):
	if Hipotenusa == None:
		return sqrt(Cateto1**2 + Cateto2**2)
	elif Cateto1 == None:
		return sqrt(Hipotenusa**2 - Cateto2**2)
	else:
		return sqrt(Hipotenusa**2 - Cateto1**2)

# _______________________________________________,
# Este modulo depende del modulo math            |
# En caso de no tener la libreria ingresar:      |
#    Python - pip install math                   |
#    Python3 - pip3 install math                 |
# _______________________________________________|
