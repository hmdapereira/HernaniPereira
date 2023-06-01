def potencia2(n):
    return n ** 2

print(potencia2(int(input("Numero: "))))

def quociente_resto(x, y):
    quociente = x // y
    resto = x % y
    return (quociente, resto)
