#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = "Juan Beresiarte"

try:
    from PIL import Image
except Exception as e:
    import os

    os.system("pip install Pillow")
    os.system("clear")
    from PIL import image

caracter_terminacion = "11111111"


def modificar_color(color_original, bit):
    color_binario = obtener_representacion_binaria(color_original)
    color_modificado = cambiar_ultimo_bit(color_binario, bit)
    return binario_a_decimal(color_modificado)


def obtener_lista_de_bits(texto):
    lista = []
    for letra in texto:
        representacion_ascii = obtener_representacion_ascii(letra)
        representacion_binaria = obtener_representacion_binaria(representacion_ascii)
        for bit in representacion_binaria:
            lista.append(bit)
    for bit in caracter_terminacion:
        lista.append(bit)
    return lista


def obtener_lsb(byte):
    return byte[-1]


def obtener_representacion_binaria(numero):
    return bin(numero)[2:].zfill(8)


def binario_a_decimal(binario):
    return int(binario, 2)


def caracter_desde_codigo_ascii(numero):
    return chr(numero)


def leer(ruta_imagen):
    imagen = Image.open(ruta_imagen)
    pixeles = imagen.load()

    tamano = imagen.size
    anchura = tamano[0]
    altura = tamano[1]

    byte = ""
    mensaje = ""

    for x in range(anchura):
        for y in range(altura):
            pixel = pixeles[x, y]

            rojo = pixel[0]
            verde = pixel[1]
            azul = pixel[2]

            byte += obtener_lsb(obtener_representacion_binaria(rojo))
            if len(byte) >= 8:
                if byte == caracter_terminacion:
                    break
                mensaje += caracter_desde_codigo_ascii(binario_a_decimal(byte))
                byte = ""

            byte += obtener_lsb(obtener_representacion_binaria(verde))
            if len(byte) >= 8:
                if byte == caracter_terminacion:
                    break
                mensaje += caracter_desde_codigo_ascii(binario_a_decimal(byte))
                byte = ""

            byte += obtener_lsb(obtener_representacion_binaria(azul))
            if len(byte) >= 8:
                if byte == caracter_terminacion:
                    break
                mensaje += caracter_desde_codigo_ascii(binario_a_decimal(byte))
                byte = ""

        else:
            continue
        break
    return mensaje


def ocultar_texto(mensaje, ruta_imagen_original, ruta_imagen_salida="salida.png"):
    print("Ocultando mensaje...".format(mensaje))
    imagen = Image.open(ruta_imagen_original)
    pixeles = imagen.load()

    tamano = imagen.size
    anchura = tamano[0]
    altura = tamano[1]

    lista = obtener_lista_de_bits(mensaje)
    contador = 0
    longitud = len(lista)
    for x in range(anchura):
        for y in range(altura):
            if contador < longitud:
                pixel = pixeles[x, y]

                rojo = pixel[0]
                verde = pixel[1]
                azul = pixel[2]

                if contador < longitud:
                    rojo_modificado = modificar_color(rojo, lista[contador])
                    contador += 1
                else:
                    rojo_modificado = rojo

                if contador < longitud:
                    verde_modificado = modificar_color(verde, lista[contador])
                    contador += 1
                else:
                    verde_modificado = verde

                if contador < longitud:
                    azul_modificado = modificar_color(azul, lista[contador])
                    contador += 1
                else:
                    azul_modificado = azul

                pixeles[x, y] = (rojo_modificado, verde_modificado, azul_modificado)
            else:
                break
        else:
            continue
        break

    if contador >= longitud:
        print("Mensaje escrito correctamente")
    else:
        print(
            "Advertencia: no se pudo escribir todo el mensaje, sobraron {} caracteres".format(
                math.floor((longitud - contador) / 8)
            )
        )

    imagen.save(ruta_imagen_salida)


op = raw_input("Quieres leer o desifrar un mensaje: ")
if op[0] == "l":
    ruta = raw_input("Ingrese el nombre o ruta de la imagen: ")
    mensaje = leer(ruta)
    print("El mensaje oculto es:")
    print(mensaje)
elif op[0] == "d":
    ruta = raw_input("Ingrese el nombre o ruta de la imagen: ")
    mensa = raw_input("mensaje a esconder: ")
    ocultar_texto(mensa, ruta)
else:
    print(
        """
Opciones:
	-desifrar -> d
	-leer     -> l

		"""
    )
# Este archivo sirve para ocultar mensajes dentro de las imagenes.
# Las imagenes no cambian en nada cuando se les coloca un mensaje oculto en ellas.
# Si no tienes pillow se instala solo, al principio.
