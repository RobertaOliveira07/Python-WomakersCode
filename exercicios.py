# 1. Faça um Programa que peça dois números, realize as principais operações soma, subtração, multiplicação, divisão

'''numero1 = int(input('Digite o numero 01:'))
numero2 = int(input('Digite o numero 02:'))
soma = numero1+numero2
print(soma)'''

'''numero1 = int(input('Digite o numero 01:'))
numero2 = int(input('Digite o numero 02:'))
subtracao = numero1-numero2
print(subtracao)'''

'''numero1 = int(input('Digite o numero 01:'))
numero2 = int(input('Digite o numero 02:'))
multiplicacao = numero1*numero2
print(multiplicacao)'''

'''numero1 = int(input('Digite o numero 01:'))
numero2 = int(input('Digite o numero 02:'))
divisao = numero1/numero2
print(divisao)'''

# 2. Peça ao usuário para informar o ano de nascimento. Em seguida,calcule e imprima a idade atual

'''nascimento = int(input('Digite a data de nascimento'))
anoAtual = int(input('Em que ano estamos?'))
idade = anoAtual-nascimento
print(idade)'''

# 3. Faça um Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros.

'''def converter_km(kilometros):
    metros = kilometros * 1000
    centimetros = metros * 100
    milimetros = centimetros * 10
    return metros, centimetros, milimetros

kilometros = float(input("Digite a quantidade de quilômetros: "))
metros, centimetros, milimetros = converter_km(kilometros)

print(f"{kilometros} quilômetros equivalem a:")
print(f"{metros} metros")
print(f"{centimetros} centímetros")
print(f"{milimetros} milímetros")'''

#4. Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. Calcule e imprima o consumo médio em km/l.

'''litros = float(input("Digite quantos litros de combustivel foram gastos?:"))
distancia = float(input("Digite quantos km voce percorreu:"))
consumo_medio = litros / distancia
print(f"Você consumiu {consumo_medio:.2f} km/l")'''

#5. Escreva um programa que calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso de avião, carro e ônibus.Levando em consideração: ● avião = 600 km/h ● carro = 100 km/h ●ônibus = 80 km/h

'''def calcular_tempo_viagem(distancia, velocidade):
    return distancia / velocidade

distancia = float(input("Digite a distância do percurso em quilômetros: "))

velocidade_aviao = 600
velocidade_carro = 100
velocidade_onibus = 80

tempo_aviao = calcular_tempo_viagem(distancia, velocidade_aviao)
tempo_carro = calcular_tempo_viagem(distancia, velocidade_carro)
tempo_onibus = calcular_tempo_viagem(distancia, velocidade_onibus)

print(f"Para uma distância de {distancia} km, o tempo de viagem será:")
print(f"Avião: {tempo_aviao:.2f} horas")
print(f"Carro: {tempo_carro:.2f} horas")
print(f"Ônibus: {tempo_onibus:.2f} horas")'''

# 6. Solicite ao usuário o peso em kg e a altura em metros. Calcule e imprima o Índice de Massa Corporal (IMC) usando a fórmula: IMC = peso / (altura x altura).

peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))
imc = peso / altura * altura

print(f"Seu IMC é:{imc: .2f} ")

#7. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.Calcule e mostre o total do seu salário no referido mês

'''ganho_hora = float(input("Digite quanto voce ganha por hora:"))
hora_trabalhada = float(input("Digite quantas horas voce trabalha no mes:"))

salario = ganho_hora * hora_trabalhada

print(f"Seu salário no mês será:{salario: .2f}")'''

#8. Solicite ao usuário o número de horas de exercício físico por semana. Calcule o total de calorias queimadas em um mês, considerando uma média de 5 calorias por minuto de exercício.

'''tempo_exercicio = float(input("Digite quantas horas voce fez exercicio fisico essa semana:"))

minutos_por_semana = tempo_exercicio * 60

calorias_por_minuto = 5

semanas_por_mes = 4

calorias_queimadas = minutos_por_semana * calorias_por_minuto * semanas_por_mes

print(f"Voce queimou {calorias_queimadas: .2f} no mes, parabens!")'''

#9. Faça um Programa que utilize 4 variáveis como preferir e no final print uma mensagem amigável utilizando as variáveis criadas. Exemplos de variáveis: nome, idade, lugar, profissão .... Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo também e estou migrando de área. Lembrando que para o retorno vamos usar print com as variáveis criadas e este texto é somente um exemplo, utilizem a criatividade.

'''nome = (input("Digite seu nome:"))
idade = (input("Digite sua idade:"))
estado = (input("Digite seu estado:"))

mensagem = f"Prazer {nome} , me chamo Roberta! voce disse que tem {idade} anos eu tenho 27 anos, eu vi que voce mora em {estado} , eu moro no rio de janeiro, é um prazer te conhecer!!"

input(mensagem)'''