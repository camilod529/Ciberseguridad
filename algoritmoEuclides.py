def euclides_extendido(a, b):
    if a == 0:
        return b, 0, 1
    else:
        mcd, x, y = euclides_extendido(b % a, a)
        return mcd, y - (b // a) * x, x

mcd, x, y = euclides_extendido(15, 49)
print("El máximo común divisor es:", mcd)
print("Los coeficientes son:", x, y)