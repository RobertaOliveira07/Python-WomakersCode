def soma(num1,num2): #definição da função soma
    calculo = num1+num2
    print(f'O resultado da soma é: {calculo}')
    
def subtratacao():
    sub = 10-2
    print(f'O resultado da subtração é {sub}')
    multiplicacao(num1,num2) # chamada de função dentro de uma função
    
def multiplicacao ():
    mult = 10*2
    print(f'O resultado da multiplicação é {mult}')

num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))    
soma(num1,num2) #chamada da função

subtratacao(num1,num2)
multiplicacao(num1,num2) # chamada de função dentro de uma função
