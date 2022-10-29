#m programa para calcular as notas obtidas pelo aluno do ensino médio

bimestreUm = float(input("digite a nota para o primeiro bimestre: 0 a 25"))
bimestreDois = float(input("digite a nota para o segundo bimestre: 0 a 25 "))
bimestreTres = float(input("digite a nota para o terceiro bimestre: 0 a 25 "))
bimestreQuatro = float(input("digite a nota para o quarto bimestre: 0 a 25"))

notaFinal = (bimestreUm + bimestreDois + bimestreTres + bimestreQuatro)

if (notaFinal >= 60):
    print("aluno aprovado")
elif (notaFinal < 60 or notaFinal >= 40):
    print("aluno em recuperação")
elif (notaFinal < 40):
    print("aluno reprovado")

