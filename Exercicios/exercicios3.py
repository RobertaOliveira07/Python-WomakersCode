'''1.Utilizando listas faça um programa que faça 5 perguntas para 
uma pessoa sobre um crime. As perguntas são:
""Telefonou para a vítima?""""Esteve no local do crime?
""""Mora perto da vítima?""""Devia para a vítima?""""Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
""Suspeita"",entre 3 e 4 como""Cúmplice""e 5 como""Assassino"". Caso contrário,ele será classificado como""Inocente"".'''

# Lista de perguntas

# Lista de perguntas
'''perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

# Lista para armazenar as respostas
respostas = []

# Fazer as perguntas e armazenar as respostas
for pergunta in perguntas:
    resposta = input(pergunta + " (sim/não): ").strip().lower()
    while resposta not in ["sim", "não"]:
        print("Resposta inválida! Por favor, responda com 'sim' ou 'não'.")
        resposta = input(pergunta + " (sim/não): ").strip().lower()
    respostas.append(resposta)

# Contar o número de respostas positivas
respostas_positivas = respostas.count("sim")

# Classificação da participação no crime
if respostas_positivas == 2:
    classificacao = "Suspeita"
elif 3 <= respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

# Exibir a classificação
print("Classificação:", classificacao)'''

# 2.Faça um Programa que peça as quatro notas de 5 alunos,calcule 
# e armazene numa lista a média de cada aluno,imprima o número de alunos 
# com média maior ou igual a 7.0.

# Lista para armazenar as notas dos alunos
'''notas_alunos = [
    [8, 7, 6, 9],  # Notas do aluno 1
    [5, 6, 7, 5],  # Notas do aluno 2
    [9, 8, 7, 10], # Notas do aluno 3
    [4, 6, 5, 7],  # Notas do aluno 4
    [6, 7, 8, 5]   # Notas do aluno 5
]

# Lista para armazenar as médias dos alunos
medias = []

# Calcular a média de cada aluno
for notas in notas_alunos:
    media = sum(notas) / len(notas)
    medias.append(media)

# Contar o número de alunos com média maior ou igual a 7.0
num_alunos_acima_7 = sum(1 for media in medias if media >= 7.0)

# Imprimir o resultado
print(f"Número de alunos com média maior ou igual a 7.0: {num_alunos_acima_7}")'''

# Crie um dicionário representando um carrinho de compras.Adicione 
# produtos(chaves)e quantidades(valores)ao carrinho.Calcule o total do carrinho de compra.

'''dicionario = {}
dicionario['maca'] = 'R$ 3,00'
dicionario['arroz'] = 'R$ 10,00'
dicionario['feijao'] = 'R$ 5,00'

total = 0

for preco in dicionario.values():
    # Remover o prefixo 'R$' e substituir a vírgula por um ponto
    preco_float = float(preco.replace('R$ ', '').replace(',', '.'))
    total += preco_float

print(f"Total do carrinho de compras: R${total:.2f}")'''

# 4.Crie um dicionário representando contatos(nome,telefone).Permita ao usuário 
# procurar por um contato pelo nome.

# Criação do dicionário de contatos
'''contatos = {
    'Ana': '1234-5678',
    'Bruno': '2345-6789',
    'Carla': '3456-7890',
    'Diego': '4567-8901'
}

# Função para procurar um contato pelo nome
def procurar_contato(nome):
    if nome in contatos:
        return f"{nome}: {contatos[nome]}"
    else:
        return f"Contato {nome} não encontrado."

# Interface de usuário para procurar um contato
nome_procurado = input("Digite o nome do contato que deseja procurar: ")
resultado = procurar_contato(nome_procurado)
print(resultado)'''

#5.Crie duas tuplas.Concatene-as para formar uma nova tupla.

# Criação das duas tuplas
'''tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

# Concatenação das tuplas
tupla_concatenada = tupla1 + tupla2

# Exibição da tupla concatenada
print("Tupla 1:", tupla1)
print("Tupla 2:", tupla2)
print("Tupla concatenada:", tupla_concatenada)'''

#6.Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o 
# nome do usuário de trás para frente utilizando somente letras maiúsculas.
# Dica:lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas 
# ou minúsculas.

# Solicita o nome do usuário
'''nome = input("Digite o seu nome: ")

# Converte o nome para maiúsculas e inverte a ordem das letras
nome_invertido = nome.upper()[::-1]

# Exibe o nome invertido
print("Nome invertido:", nome_invertido)'''







