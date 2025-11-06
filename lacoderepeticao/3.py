x = int(input("Quantas médias calcular: "))
vezes= 0
while vezes < x:
    nota1 = float(input("Insira sua primeira nota: "))
    nota2 = float(input("Insira sua segunda nota: "))
    frequencia = float(input("Insira sua frequencia: "))
    media = (nota1 + nota2)/ 2
if media  >= 6 and frequencia >= 75:
    print("Aprovado")
    print(f"sua media foi: {media}")
    print("sua media foi %.2f" % media)
    print(f"frquencia: {frequencia}")
elif media >= 6 and frequencia < 75:
    print("Reprovado")
    print(f"sua media foi: {media}")
    print(f"frequencia: {frequencia}")
else:
    print("Aluno reprovado nota e falta")
    print(f"sua media foi{media}")
    print(f"frequencia: {frequencia}")
    vezes += 1