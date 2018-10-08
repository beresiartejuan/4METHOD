class Cesar(object):
    def __init__(self, texto, opcion, clave=3):
        self.clave = clave # clave < 26 obligatoriamente
        self.texto = texto
        # 'e' -> encriptar
        # 'd' -> desencritar
        self.opcion = str(opcion)
        
        return self.getTraducirMensaje(self.opcion, self.texto, self.clave)

    def getTraducirMensaje(opcion, mensaje, llave):
        if opcion[0] == 'd':
            llave = -llave
        traducir = ''
 
        for simbolo in mensaje:
            if simbolo.isalpha():
                num = ord(simbolo)
                num += llave

                if simbolo.isupper():
                    if num > ord('Z'):
                        num -= 26
                    elif num < ord('A'):
                        num += 26
                    elif simbolo.islower():
                        if num > ord('z'):
                            num -= 26
                        elif num < ord('a'):
                            num += 26

                traducir += chr(num)
            else:
                traducir += simbolo
        return traducir
