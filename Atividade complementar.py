#Veja o algoritmo abaixo e escreva o programa para executa-lo

lados = ("a", "b", "c")

a= float(input( "primeiro lado: "))
b= float(input( "segundo lado: "))
c= float(input( "terceiro lado: "))

if (a < b+c) and (b < a+c) and ( c< a+b):
    print( "triangulo isosceles" )

elif (a == b) or (b == c) or (a == c):
    print( "triangulo equilatero" )

elif (c != a+b) or (b != c+a) or (a != b+c):
    print( "triangulo escaleno")

else:
    print("Não e possível formar um triângulo")

