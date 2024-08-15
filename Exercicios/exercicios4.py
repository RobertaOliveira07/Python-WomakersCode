# 1. Faça um programa, com uma função que necessite de três
# argumentos, e que forneça a soma desses três argumentos.

def soma_tres_argumentos(a, b, c):
    """
    Função que recebe três argumentos e retorna a soma deles.

    :param a: Primeiro número
    :param b: Segundo número
    :param c: Terceiro número
    :return: Soma dos três números
    """
    return a + b + c

# Testando a função
resultado = soma_tres_argumentos(5, 10, 15)
print(f'A soma dos três argumentos é: {resultado}')


# 2. Reverso do número. Faça uma função que retorne o reverso de um
# número inteiro informado. Por exemplo: 127 -> 721.

def reverso_numero(numero):
    """
    Função que retorna o reverso de um número inteiro informado.

    :param numero: Número inteiro a ser revertido
    :return: Número inteiro reverso
    """
    # Verifica se o número é negativo
    negativo = numero < 0
    # Converte o número para string e remove o sinal de negativo
    numero_str = str(abs(numero))
    # Reverte a string
    reverso_str = numero_str[::-1]
    # Converte a string revertida de volta para inteiro
    reverso = int(reverso_str)
    # Se o número original era negativo, adiciona o sinal de negativo
    if negativo:
        reverso = -reverso
    return reverso

# Testando a função
numero = 127
resultado = reverso_numero(numero)
print(f'O reverso do número {numero} é: {resultado}')

# 3. Escreva um script que pergunta ao usuário se ele deseja converter 
# uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para 
# cada opção, crie uma função.

def celsius_para_fahrenheit(celsius):
    """
    Converte uma temperatura de Celsius para Fahrenheit.

    :param celsius: Temperatura em graus Celsius
    :return: Temperatura em graus Fahrenheit
    """
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    """
    Converte uma temperatura de Fahrenheit para Celsius.

    :param fahrenheit: Temperatura em graus Fahrenheit
    :return: Temperatura em graus Celsius
    """
    return (fahrenheit - 32) * 5/9

def menu():
    """
    Exibe o menu para o usuário escolher a conversão desejada e chama a função de conversão apropriada.
    """
    print("Escolha a conversão desejada:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    
    escolha = input("Digite 1 ou 2: ")
    
    if escolha == "1":
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")
    elif escolha == "2":
        fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
        celsius = fahrenheit_para_celsius(fahrenheit)
        print(f"A temperatura em Celsius é: {celsius:.2f}°C")
    else:
        print("Escolha inválida. Por favor, digite 1 ou 2.")

# Executa o menu principal se o script for executado diretamente
if __name__ == "__main__":
    menu()


# 4. Crie um programa que leia quanto dinheiro uma pessoa tem na 
# carteira, e calcule quanto poderia comprar de cada moeda estrangeira. 
# Considere a tabela de conversão abaixo:
#Dólar Americano: R$ 4,91
#Peso Argentino: R$ 0,02
#Dólar Australiano: R$ 3,18
#Dólar Canadense: R$ 3,64
#Franco Suiço: R$ 0,42
#Euro: R$ 5,36
#Libra esterlina: R$ 6,21

def calcular_moedas(dinheiro):
    """
    Calcula quanto dinheiro pode ser convertido para cada moeda estrangeira com base nas taxas de conversão.

    :param dinheiro: Quantia em reais
    :return: Dicionário com a quantidade de cada moeda que pode ser comprada
    """
    taxas = {
        "Dólar Americano": 4.91,
        "Peso Argentino": 0.02,
        "Dólar Australiano": 3.18,
        "Dólar Canadense": 3.64,
        "Franco Suiço": 0.42,
        "Euro": 5.36,
        "Libra esterlina": 6.21
    }
    
    resultado = {}
    
    for moeda, taxa in taxas.items():
        resultado[moeda] = dinheiro / taxa
    
    return resultado

def main():
    print("Bem-vindo ao conversor de moedas!")
    
    try:
        reais = float(input("Digite quanto dinheiro você tem na carteira (em reais): R$ "))
        
        if reais < 0:
            print("O valor não pode ser negativo. Por favor, insira um valor válido.")
            return
        
        conversao = calcular_moedas(reais)
        
        print("\nCom R$ {:.2f}, você pode comprar:" .format(reais))
        for moeda, quantidade in conversao.items():
            print(f"{moeda}: {quantidade:.2f}")
    
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")

# Executa o programa principal se o script for executado diretamente
if __name__ == "__main__":
    main()

# 5. Crie uma função chamada contar_vogais que recebe uma string 
# como parâmetro. Implemente a lógica para contar o número de vogais 
# na string e retorne o total de vogais. Solicite ao usuário para inserir uma 
# frase e utilize a função para contar as vogais.

def contar_vogais(frase):
    """
    Conta o número de vogais em uma string.

    :param frase: A string na qual as vogais serão contadas
    :return: O número total de vogais na string
    """
    vogais = "aeiouAEIOU"
    contador = 0
    
    for caractere in frase:
        if caractere in vogais:
            contador += 1
    
    return contador

def main():
    print("Bem-vindo ao contador de vogais!")
    
    frase = input("Digite uma frase: ")
    
    # Chama a função contar_vogais para contar as vogais na frase fornecida
    total_vogais = contar_vogais(frase)
    
    print(f"A frase digitada tem {total_vogais} vogais.")

# Executa o programa principal se o script for executado diretamente
if __name__ == "__main__":
    main()

# 6. Vamos construir um jogo de forca. O programa escolherá 
# aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
#secreta será representada por espaços em branco, um para cada letra
#da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
#tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
#na palavra secreta, ela será revelada nas posições correspondentes. Se
#a letra não estiver na palavra, uma mensagem de erro deverá ser
#informada. Após um número máximo de erros, o jogador perde. O jogo
#continua até que o jogador adivinhe a palavra ou exceda o número máximo de tentativas.
#Dica: Você precisará importar uma biblioteca para resolver esse
#exercício

import random

def escolher_palavra():
    """
    Escolhe uma palavra aleatória de uma lista predefinida.

    :return: Palavra secreta
    """
    palavras = ['python', 'desenvolvimento', 'programacao', 'computador', 'algoritmo']
    return random.choice(palavras)

def mostrar_palavra(palavra_secreta, letras_adivinhadas):
    """
    Mostra a palavra secreta com as letras adivinhadas reveladas.

    :param palavra_secreta: Palavra secreta a ser adivinhada
    :param letras_adivinhadas: Letras adivinhadas pelo jogador
    :return: Palavra com letras adivinhadas reveladas
    """
    return ''.join([letra if letra in letras_adivinhadas else '_' for letra in palavra_secreta])

def jogo_forca():
    """
    Função principal do jogo da forca.
    """
    palavra_secreta = escolher_palavra()
    letras_adivinhadas = set()
    tentativas_restantes = 6
    letras_erradas = set()
    
    print("Bem-vindo ao jogo da forca!")
    
    while tentativas_restantes > 0:
        print(f"\nPalavra: {mostrar_palavra(palavra_secreta, letras_adivinhadas)}")
        print(f"Tentativas restantes: {tentativas_restantes}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        
        tentativa = input("Digite uma letra: ").lower()
        
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Entrada inválida. Por favor, digite uma única letra.")
            continue
        
        if tentativa in letras_adivinhadas or tentativa in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        if tentativa in palavra_secreta:
            letras_adivinhadas.add(tentativa)
            if all(letra in letras_adivinhadas for letra in palavra_secreta):
                print(f"\nParabéns! Você adivinhou a palavra: {palavra_secreta}")
                break
        else:
            letras_erradas.add(tentativa)
            tentativas_restantes -= 1
        
        if tentativas_restantes == 0:
            print(f"\nGame over! A palavra era: {palavra_secreta}")

if __name__ == "__main__":
    jogo_forca()




