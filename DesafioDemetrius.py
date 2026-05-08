import math     #Para fazer a raiz de delta

def bhaskara(a, b, c):  #Função para cálculo de báscara
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        return None     #Não há raízes reais quando delta é negativo
    sqrt_delta = math.sqrt(delta)
    valor_x1 = (-b + sqrt_delta) / (2 * a)
    valor_x2 = (-b - sqrt_delta) / (2 * a)
    return(valor_x1, valor_x2)      #Retorno dos valores das raízes reais

def valores_positivos(numero):  #Função para printar valores de 0 ao resultado positivo (mais abaixo)
    if numero % 2 == 0:     #Resultados pares
        for i in range(0, numero + 1):
            print(i, end=", ")
    else:                   #Resultados ímpares
        for i in range(1, numero + 1):
            print(i, end=", ")
        
def valores_negativos(numero):  #Função para printar valores do resultado negativo até 0 (mais abaixo)
    for i in range(numero, 1,):
        print(i, end=", ")

#Desenvolva uma aplicação que receba 3 valores do usuário (a, b e c) e faça uma função que calcule a formula de Bhaskara e retorne o valor de x1 e x2.
valor_a = int(input("Digite o valor de A: "))
valor_b = int(input("Digite o valor de B: "))   #f(x) = ax^2 + bx + c
valor_c = int(input("Digite o valor de C: "))

print(bhaskara(valor_a, valor_b, valor_c))  #Retorno da função Bhaskara, printada à tela

#Utilize os valores de x1 e x2 como atributos para uma função que realizará a soma deles e retorne o resultado
soma_x = lambda a, b : - (b / a)    #x1 + x2 = - (b / a)
somados = int(soma_x(valor_a, valor_b))
print(somados)

#Caso o resultado seja par e maior que zero, passe o valor como parâmetro para um função que retornará uma lista com os valores positivos de zero ao valor do resultado.
#Caso seja ímpar e maior que zero, passe o valor como parâmetro para um função que retornará uma lista com os valores positivos de um ao valor do resultado.
#Caso o resultado seja menor ou igual a zero, passe o valor como parâmetro para um função que retornará uma lista com os valores negativos do resultado até zero.
par_impar = lambda func : func % 2 == 0     #Função determinante de paridade
resultado = par_impar(somados)

if somados <= 0:    #Resultado negativo
    valores_negativos(somados)
else:   #Resultado positivo
    if resultado:   #Resultado par (variável "resultado" = True)
        valores_positivos(somados)
    else:   #Resultado ímpar (variável "resultado" = False)
        valores_positivos(somados)
        