import urllib, urllib.request
print("================================")
print("------DobleHtMl-----------------")
print("================================ \n")
url = input("Ingrese algun url: ")
nombre = input("Ruta o nombre: ")
with urllib.request.urlopen(url) as html_handler:
	html = str(html_handler.read(), 'utf-8')
	with open(nombre, "w") as file_handler:
		print("Copiando pagina web en tu escritorio...")
		file_handler.write(html) 
		print("Pagina web copiada con exito!")