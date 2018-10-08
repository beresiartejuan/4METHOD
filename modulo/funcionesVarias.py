def EliminarEspaciosVaciosListas(lista):
	number = 0
	for i in lista:
		if i == "" or i == " ":
			lista.pop(number)
		number += 1
	return lista
def ficheroExistente(ruta):
	try:
		open(ruta, "r")
		return True
	except Exception:
		return False
def buscarArchivo(nombre, directorio="/home"):
	import os
	total = 0
	lista = []
	if directorio != "/home":
		if(not os.path.isdir(directorio)):
        	print(directorio,"no se reconoce como directorio")
        	print("No se pudo realizar la busqueda.")
       		return 0
    for root, dir, ficheros in os.walk(directorio):
    	for fichero in ficheros:
        	if(buscar in fichero.lower()):
            	print(root+"/"+fichero)
            	lista.add(str(root+"/"+fichero))
            	total += 1
   	print("Hay " + total + " archivos encontrados.")
   	print("Fin")
    return lista
