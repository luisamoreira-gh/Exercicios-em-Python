#Desafio de Sequência: Crie uma lista com os valores (23, 32, 64, 18, 9, 51, 67, 90)
lista1 = [23, 32, 64, 18, 9, 51, 67, 90]

lista_ordenada1 = sorted(lista1)  #Ordene-os em ordem crescente-
lista_invertida1 = sorted(lista1, reverse = True) #-e depois decrescente
print(lista_ordenada1)
print(lista_invertida1)

lista_soma1 = sum(lista1) #Imprima a soma de todos os valores usando a função sum
print(lista_soma1)

print(len(lista1))   #Imprima o tamanho da lista e o último valor sem usar índices fixos positivos
print(lista1[-1])

print("-------------------------------------------------------------")

#Edição Dinâmica: Crie uma lista vazia e adicione os elementos: "Lenovo", "Acer", "Samsung", "Asus" e "Dell"
lista2 = ["Lenovo", "Acer", "Samsung", "Asus", "Dell"]

lista2.pop(2)   #Remova o valor da posição 3

lista2.insert(2, "Apple")  #Adicione "Apple" na terceira posição e "Positivo" na última posição
lista2.append("Positivo")
print(lista2)

print("-------------------------------------------------------------")

#Cadastro por Sexo: Crie um programa que utilize dois dicionários: feminino e masculino
i = 0    #Contador de informações inseridas
feminino_idade = []
feminino_nome = []
masculino_idade = []
masculino_nome = []
início = str(input("Deseja iniciar os cadastros? (S ou N): "))

while início == "S":    #Receba o nome, sexo e idade de pelo menos 10 clientes
    sexo = str(input("Digite o sexo do usuário (F ou M): "))
    nome = str(input("Digite o nome do usuário: "))
    idade = int(input("Digite a idade do usuário: "))
    
    if sexo == "F":     #Se for do sexo feminino, armazene os dados no dicionário feminino; se masculino, no masculino
        feminino_idade.append(idade)
        feminino_nome.append(nome)
        i += 1      #Para cada nova pessoa cadastrada, +1
    elif sexo == "M":
        masculino_idade.append(idade)
        masculino_nome.append(nome)
        i += 1
    else:
        print("Sexo inválido. Tente novamente!")
    if i >= 10:
        início = str(input("Deseja continuar os cadastros? (S ou N): "))
        if início == "N":
            print(f"NOMES FEMININOS CADASTRADOS: {feminino_nome}")
            print(f"NOMES MASCULINOS CADASTRADOS: {masculino_nome}")
            print(f"IDADES FEMININAS CADASTRADAS: {feminino_idade}")
            print(f"IDADES MASCULINAS CADASTRADAS: {masculino_idade}")  #Ao final, exiba todos os dados cadastrados de forma organizada
            break
if início == "N":
    breakpoint
print("-------------------------------------------------------------")

#Conversor Binário: Crie um programa que receba um número decimal e o converta para binário
binario = []
numero1 = int(input("Digite o número desejado: "))
while numero1 >= 2:
    resto1 = numero1 % 2
    numero1 = numero1 // 2
    binario.append(resto1) 
binario.insert(0, int(numero1))

for i in range(len(binario)):
    print(binario[i], end = "")
print("")

#Conversor Octal: Implemente a lógica para transformar um número decimal em octal
octal = []
numero2 = int(input("Digite o número desejado: "))
while numero2 >= 8:
    resto2 = numero2 % 8
    numero2 = numero2 // 8
    octal.append(resto2) 
octal.insert(0, int(numero2))

for i in range(len(octal)):
    print(octal[i], end = "")
print("")

print("-------------------------------------------------------------")

#Ano de Nascimento: Peça o nome e a idade do usuário e calcule o seu ano de nascimento
from datetime import date
nome2 = str(input("Insira o nome do usuário: "))
idade2 = int(input("Insira a idade do usuário: "))

ano_atual = date.today().year
nascimento = int(ano_atual) - idade2
print(f"Olá {nome2}, você nasceu no ano de {nascimento}!")

#Tabuada de Soma: Crie uma variável que receba um valor inteiro de 0 a 9 e exiba a tabuada de soma completa desse valor
numero3 = int(input("Digite o número desejado: "))
for i in range(10):
    soma = numero3 + i
    print(f"{numero3} + {i} = {soma}")
    
print("-------------------------------------------------------------")

