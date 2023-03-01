import base64

entrada = input('Ingrese el valor a encriptar\n')

# Convertir la entrada a su representación en binario
binario = ''.join(format(ord(caracter), '08b') for caracter in entrada)

lista = [binario[i:i+6] for i in range(0, len(binario), 6)] 

if len(lista[len(lista) - 1]) < 6:
    lista[len(lista) - 1] += '0' * (6 - len(lista[len(lista) - 1]))

for valor in lista:
    bytesBinario = bytes(binario, 'ascii')
    base64Bytes = base64.b64encode(bytesBinario)
    base64String = base64Bytes.decode('ascii')
    print(base64String)

