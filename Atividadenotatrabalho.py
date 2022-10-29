
TrabalhoUm = float(input("digite a nota para o primeiro trablho: "))
TrabalhoDois = float(input("digite a nota para o segundo trabalho: "))
TrabalhoTres = float(input("digite a nota para o terceiro trabalho: "))
TrabalhoQuatro = float(input("digite a nota para o quarto trabalho: "))

ProvaUm = float(input("digite a nota para o primeira prova: "))
ProvaDois = float(input("digite a nota para o segunda prova: "))
ProvaTres = float(input("digite a nota para o terceira prova: "))
ProvaQuatro = float(input("digite a nota para o quarto prova: "))

notaFinal = (TrabalhoUm + TrabalhoDois + TrabalhoTres + TrabalhoQuatro + ProvaUm + ProvaDois + ProvaTres + ProvaQuatro)

print("a nota anual do aluno foi: ", notaFinal)

if (notaFinal >= 60):
    print("aluno aprovado")
elif (notaFinal <40):
    print("aluno reprovado")
elif (notaFinal < 60 or notaFinal <=40):
    print("aluno em recuperação")
