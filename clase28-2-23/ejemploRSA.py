def euclides_extendido(a, b):
    if a == 0:
        return b, 0, 1
    else:
        mcd, x, y = euclides_extendido(b % a, a)
        return mcd, y - (b // a) * x, x

p = int(input('ingrese el primer numero\n'))
q = int(input('ingrese el segundo numero\n'))
m = int(input('ingrese el mensaje a encriptar\n'))

n = p * q

phi = (p - 1) * (q - 1)
print('------------------------------------')
for i in range (1, phi):
    mcd, x, y = euclides_extendido(i,phi)
    if mcd == 1:
        print(i)

e = int(input('Ingrese un valor de la lista anterior\n'))

mcd, x, y = euclides_extendido(e, phi)
inv = 0

if  mcd == 1:
    for i in range(0,phi):
        if (e * i) % phi == 1:
            inv = i
    c = pow(m, e) % n
    print(f'mensaje encriptado {c}')
    p = pow(c,inv) % n
    print(f'mensaje desencriptado {p}')
    
else:
    print('No existe clave privada pq el mcd no es 1')

