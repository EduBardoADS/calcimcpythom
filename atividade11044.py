#Crie um programa em python que solicite ao usuário o peso e a altura e calcule o índice de massa corpórea : IMC = peso/altura² e mostre em qual categoria o usuário se encontra, conforme a tabela abaixo:

#Categoria      |  IMC
#Abaixo do peso | <20
#Peso normal    | >= 20 e <25
#SObrepeso      | >= 30 e <40
#Obeso mórbido  | >= 40

peso = float(input("Digite o seu peso"))
altura = float(input("Digite a sua altura"))

imc = peso/(altura*altura) #ou imc = peso/altura**2

if imc < 20:
    print("Abaixo do peso")
elif imc >=20 and imc <25:
    print("Peso normal")
elif imc >=20 and imc <30:
    print("Sobre peso")
elif imc >=30 and imc <40:
    print("Obbeso")
else:
    print("Peso mórbido")
