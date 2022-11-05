#Faça um Programa que leia em um vetor de 10 caracteres (letras ) e diga quantas consoantes foram lidas.

lista = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    lista[i] = input("digite uma letra para cada posição: ")

print(lista)

consoante = 0

for i in range(10):
    if not (lista[i] == str("a") or lista[i] == "e" or lista[i] == "i" or lista[i] == "o" or lista[i] == "u" ):
        print("consoante na posição " + str(1+1) +": ", lista[i])
        consoante=consoante+1

print("o numero total de consoantes é" , consoante)





















