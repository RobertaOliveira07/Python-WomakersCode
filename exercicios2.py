# 1.Faça um Programa que peça dois números e imprima o maior deles.


'''numero1 = int(input("Digite seu numero:"))
numero2 = int(input("Digite seu numero:"))

if numero1 > numero2:
    print(f"O maior numero é: {numero1}")
elif numero2 > numero1:
    print(f"O maior numero é: {numero2}")
else:
    print("Os dois numeros sao iguais")'''
    
# 2. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

'''turno = input("Digite o turno em que você estuda (M-matutino, V-vespertino, N-noturno): ") .upper()

if turno == "M" :
    print("matutino")
elif turno == "V" :
    print("vespertino")
elif turno == "N" :
    print("noturno")
else:
    print("valor inválido")'''
    
# 3. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido
    
'''nota = float(input("Digite uma nota de 0 a 10: "))
  
while nota < 0 or nota > 10:
    print("Valor inválido! Por favor, digite uma nota entre 0 e 10.")
    nota = float(input("Digite uma nota entre 0 e 10: "))


print(f"Você digitou uma nota válida: {nota}")'''

# 4. Implemente um programa que classifique um aluno com base em sua pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é reprovado.


'''nota = float(input("Digite uma nota entre 0 e 10: "))


while nota < 0 or nota > 10:
    print("Valor inválido! Por favor, digite uma nota entre 0 e 10.")
    nota = float(input("Digite uma nota entre 0 e 10: "))


if nota >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")'''
    
# 5. Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno. equilátero: todos os lados com o mesmo valor isósceles: dois lados com o mesmo valor escaleno: todos os lados com medidas distintas.



'''lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))


if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    # Classifica o triângulo
    if lado1 == lado2 == lado3:
        print("O triângulo é equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
else:
    print("Os valores fornecidos não podem formar um triângulo.")'''
    
#6. Crie um programa que solicite ao usuário um login e uma senha. O programa deve permitir o acesso apenas se o usuário for "admin" e a senha for "admin123", caso contrário imprima uma mensagem de erro.


'''login = input("Digite o login: ")
senha = input("Digite a senha: ")


if login == "admin" and senha == "admin123":
    print("Acesso concedido.")
else:
    print("Erro: login ou senha incorretos.")'''
    
#7. Desenvolver um programa que solicite a idade do usuário e identifique se ele é uma criança, um adolescente, adulto ou idoso

idade = int(input("Digite a sua idade: "))

# Classifica a pessoa com base na idade
'''if idade >= 0 and idade <= 12:
    print("Você é uma criança.")
elif idade >= 13 and idade <= 17:
    print("Você é um adolescente.")
elif idade >= 18 and idade <= 64:
    print("Você é um adulto.")
elif idade >= 65:
    print("Você é um idoso.")
else:
    print("Idade inválida. Por favor, digite uma idade válida.")'''
    
# 8. Criar um programa em Python que solicite três números ao usuário, utilize estruturas condicionais para determinar o maior entre eles e apresente o resultado.


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Determina o maior número usando estruturas condicionais
if numero1 >= numero2 and numero1 >= numero3:
    maior = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    maior = numero2
else:
    maior = numero3

# Exibe o resultado
print(f"O maior número é: {maior}")
