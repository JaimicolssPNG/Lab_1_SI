import os
import hashlib
from Cryptodome.Cipher import AES

Clave_Hash = hashlib.new("md5",b"SuperClaveSecreta")
Password = Clave_Hash.digest()

def Desencriptar(Mensaje):
    Mensaje = Mensaje
    PAD = "0"
    Descifrar = AES.new(Password, AES.MODE_ECB)
    Descifrado = Descifrar.decrypt(Mensaje).decode("utf-8")
    Indice_pad = Descifrado.find(PAD)
    Mensaje_Descifrado = Descifrado[:Indice_pad]
    return Mensaje_Descifrado

Archivo = open("mensajeseguro.txt")
while (True):
    Mensaje = Archivo.readline()
    print(Mensaje)
    Texto_Desencriptado = Desencriptar(Mensaje)
    print(Texto_Desencriptado)
        
    if not Mensaje:
        break
        
Archivo.close()
