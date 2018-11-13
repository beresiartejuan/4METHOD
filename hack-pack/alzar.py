#!/usr/bin/env python
import sys
from random import choice

try:
	valores = str(argv[0])
	longitud = int(argv[1])
except Exception as e:
	print("- Termino 1: Valores")
	print("- Termino 2: Longitud")

p = ""
p = p.join([choice(valores) for i in range(longitud)])
print(p)
