def mcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
 
def inv(a, m):
    gcd, x, y = mcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
 

def encrypt(mensaje, clave):
    #C = (a*P + b) % 26
    return ''.join([ chr((( clave[0]*(ord(t) - ord('A')) + clave[1] ) % 26) + ord('A')) for t in mensaje.upper().replace(' ', '') ])
 
 
def decrypt(mensaje_encriptado, clave):
    #P = (a^-1 * (C - b)) % 26
    
    return ''.join([ chr((( inv(clave[0], 26)*(ord(c) - ord('A') - clave[1])) % 26) + ord('A')) for c in mensaje_encriptado ])
 
 

# declaring text and key
mensaje = input('Ingrese mensaje a encriptar\n')
clave = [17, 20]

# calling encryption function
Mensaje_encriptado = encrypt(mensaje, clave)

print('Mensaje encriptado: ', Mensaje_encriptado )

# calling decryption function
print('Mensaje desencriptado: ', decrypt(Mensaje_encriptado, clave) )
 
 
