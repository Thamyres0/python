
a = float(input('Primeiro lado: '))
b = float(input('Segundo  lado: '))
c = float(input('Terceiro lado: '))

# Testando se é triângulo

if (a + b < c) and (a + c < b) and (b + c < a):
    print("Nao é um triangulo")

elif (a == b) and (a == c):
    print(" triangulo Equilatero")

elif (a == b) or (a == c) or (b == c):
    print(" triangulo Isósceles")

else:
    print("  triangulo Escaleno")
