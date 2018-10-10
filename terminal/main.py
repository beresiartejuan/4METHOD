#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# archivo de ejemplo para crear asistente
# Inicializar asistente en español
import ManagerAsistent as archivo
asistente = archivo.Asistente(nombre="", usuario="", genero="",
	data={ xml = False, db = False, conf = True}, 
	data_dir="config.conf", #Direccion de el archivo
	comandos="comands.cmd", #Ruta de archivo
	respuesta_automatica="Escribe otra vez el texto, no lo logre comprender."
	)

asistente.play(True)
# Si se cambia a false no sucedera nada
# Solo se guardara la configuración
# 