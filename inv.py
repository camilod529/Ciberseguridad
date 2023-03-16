a = int(input('Ingrese numero 1:\n'))
b = int(input('ingrese numero 2:\n'))

if a > b:
    a, b = b, a
print(a, b)
def euclides_extendido(a, b):
    if a == 0:
        return b, 0, 1
    else:
        mcd, x, y = euclides_extendido(b % a, a)
        return mcd, y - (b // a) * x, x
        
mcd, x, y = euclides_extendido(a,b)
if mcd == 1:
    for i in range (0,b):
        if (a * i ) % b == 1:
            print(f'el inverso multiplicativo es {i}')
else: 
    print('No existe el inverso multiplicativo')