import string

def encrypt(mensaje, clave):
    # Crea un diccionario con las letras en minusculas como claves
    # y las letras correspondientes de la clave como valores
    alfabeto = string.ascii_lowercase
    dict_cifrado = dict(zip(alfabeto, clave.lower()))

    # Ciframos el mensaje letra por letra
    Mensaje_cifrado = ""
    for letter in mensaje.lower():
        # Si la letra esta en el diccionario, la reemplazamos por su valor
        if letter in dict_cifrado:
            Mensaje_cifrado += dict_cifrado[letter]
        # Si no, agregamos la letra sin cambios
        else:
            Mensaje_cifrado += letter

    return Mensaje_cifrado

def decrypt(mensaje_cifrado, clave):
    # Creamos un diccionario con las letras de la clave como claves
    # y las letras en minusculas correspondientes como valores
    alfabeto = string.ascii_lowercase
    dict_cifrado = dict(zip(clave.lower(), alfabeto))

    # Desciframos el mensaje letra por letra
    mensaje = ""
    for letra in mensaje_cifrado.lower():
        # Si la letra esta en el diccionario, la reemplazamos por su valor
        if letra in dict_cifrado:
            mensaje += dict_cifrado[letra]
        # Si no, agregamos la letra sin cambios
        else:
            mensaje += letra

    return mensaje

clave = "QWERTYUIOPASDFGHJKLZXCVBNM"
mensaje = input('Ingrese un mensaje para cifrar\n')
mensaje_cifrado = encrypt(mensaje, clave)
print('Encriptado: ',mensaje_cifrado)
mensaje_desencriptado = decrypt(mensaje_cifrado, clave)
print('Desencriptado: ', mensaje_desencriptado)