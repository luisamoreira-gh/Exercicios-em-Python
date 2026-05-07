#EXERCISE 1 -- The Goal: Write a function that takes a list of items and removes duplicates while keeping the original order.
def lista_limpa(itens):
    visto = []      #Inside the function, use a new list to track "seen" items.
    for produto in itens:
        if produto not in visto:
            visto.append(produto)
    visto_alfabetico = sorted(visto)    #Bonus: Sort the final list alphabetically before returning it.
    return(visto_alfabetico)    #Return the deduplicated list.
        
lista_de_compras = ["Arroz", "Arroz", "Cuminho", "Chá preto", "Chá preto", "Chá preto", "Produto de limpeza", "Sabonete", "Lava-louças"]
print(lista_limpa(lista_de_compras))

print("-------------------------------------------------------------")

#EXERCISE 2 -- The Goal: Create a simple contact management system using a dictionary where the Key is a name and the Value is a phone number.
def add_contato(diretório, nome, número):   #The function should update the dictionary with the new name and number.
    if diretório in meus_contatos:
        if nome not in meus_contatos[diretório]:
            meus_contatos[diretório][nome] = número
            print("Número adicionado aos contatos")
        elif nome in meus_contatos[diretório]:
            substituindo = str(input("Essa pessoa já está nos seus contatos! Substituir mesmo assim? (S ou N): "))
            if substituindo.lower() == "s":
                meus_contatos[diretório][nome] = número
                print("Contato atualizado")
            else:
                breakpoint
        else:
            print("Diretório não encontrado")
        
def achar_contato(diretório, nome):     #Write a second function find_contact(directory, name)
    if diretório in meus_contatos:
        if nome not in meus_contatos[diretório]:
            print("Desculpe, esse número não existe")
        else:
            número = meus_contatos[diretório][nome]
            print(f"O número para contato de {nome} é {número}")
    else:
        print("Diretório não encontrado")

meus_contatos = {"Comida" : {}, "Amigos" : {}, "Família" : {}}  #Initialize an empty dictionary called my_contacts

início = int(input("Digite 1 para adicionar um contato, 2 para buscar um contato dentro de sua lista, ou 0 para terminar o processo: "))
while início != 0:
    if início == 1:
        Dir = str(input("Digite o diretório desejado: "))
        Nam = str(input("Digite o nome desejado: "))
        Num = input("Digite o número desejado: ")
        add_contato(Dir, Nam, Num)
        início = int(input("Digite 1 para adicionar um contato, 2 para buscar um contato dentro de sua lista, ou 0 para terminar o processo: "))
    elif início == 2:
        Dir = str(input("Digite o diretório desejado: "))
        Nam = str(input("Digite o nome desejado: "))
        achar_contato(Dir, Nam)
        início = int(input("Digite 1 para adicionar um contato, 2 para buscar um contato dentro de sua lista, ou 0 para terminar o processo: "))
    elif início > 2:
        print("Desculpe, esse código não existe.")
        início = int(input("Digite 1 para adicionar um contato, 2 para buscar um contato dentro de sua lista, ou 0 para terminar o processo: "))
    else:
        break
    
print("-------------------------------------------------------------")

#EXERCISE 3 -- The Goal: Analyze a string of text to see how many times each word appears.
def contar_palavras(frase):     #Task: Create a function count_words(sentence)
    lista_frase = frase.split()     #Use .split() to turn the string into a List of words.
    dicionario_frase = {}
    for palavra in lista_frase:     #Loop through the list and store the counts in a Dictionary.
        palavra = palavra.lower()   #Take a string input and convert it to lowercase.
        if palavra not in dicionario_frase:
            dicionario_frase[palavra] = 1
        else:
            dicionario_frase[palavra] += 1
    print(dicionario_frase)

frase_input = str(input("Digite a frase desejada: "))
contar_palavras(frase_input)    #Example Output: count_words("apple banana apple") should return {"apple": 2, "banana": 1}.

print("-------------------------------------------------------------")

#EXERCISE 4 -- The Goal: Manage more complex data by nesting dictionaries inside a list.
def calcular_valor_total(dicionário):   #Write a function calculate_total_value(warehouse) that iterates through the list.
    soma_total = 0
    for item in dicionário:
        preco = item["Preço"]
        estoque = item["Estoque"]
        valor_item = preco * estoque    #For each item, multiply price by stock.
        soma_total += valor_item
    print(f"Total do Depósito: R${soma_total}")   #Return the sum of all items in the warehouse.

deposito = [       #Task: Create a list of dictionaries called warehouse. Each dictionary should represent an item: {"name": "Laptop", "price": 800, "stock": 5}
    {"Nome" : "Laptop","Preço": 4000, "Estoque" : 5},
    {"Nome" : "Pulseira", "Preço": 25, "Estoque" : 40},
    {"Nome" : "Batata Chips", "Preço": 10, "Estoque" : 25}
]
calcular_valor_total(deposito)

print("-------------------------------------------------------------")

#EXERCISE 5 -- The Goal: Calculate student performance using a dictionary where values are Lists of numbers.
def analise_notas(dicionario):  #Task: Create a function analyze_grades(scoresheet)
    notas_finais = {}   #Return a new dictionary where the key is the student's name and the value is their average.
    for item in dicionario:
        provas = item["Notas"]
        aluno = item["Nome"]
        media_aluno = sum(provas) / len(provas) #The function should calculate the average for each student.
        notas_finais[aluno] = {}
        notas_finais[aluno]["Média"] = round(media_aluno, 2)
        if media_aluno >= 7:
            notas_finais[aluno]["Status"] = "Aprovado"      #Bonus: Add a "Status" (Pass/Fail) based on whether the average is above 7.0.
        else:
            notas_finais[aluno]["Status"] = "Reprovado"
    print(notas_finais)
        
boletim = [
    {"Nome": "Ana", "Notas": [1, 5, 4]},    
    {"Nome": "Bruno", "Notas": [9, 6, 3]},
    {"Nome": "Carla", "Notas": [2, 3, 8]},
    {"Nome": "Daniel", "Notas": [9, 9, 3]}
]
analise_notas(boletim)

print("-------------------------------------------------------------")

#EXERCISE 6 -- The Goal: Practice modifying list data based on specific conditions (very common in data cleaning).
def censurar_lista(frase, palavra):     #Task: Create a function censor_list(phrases, forbidden_word)
    palavras = frase.lower().split()
    censura = palavra.lower()
    lista_limpa = []
    for i in palavras:      #Loop through the list. If a string contains the forbidden word, replace that string with the word "CENSORED"
        if i == censura:
            lista_limpa.append("CENSURADO")
        else:
            lista_limpa.append(i)
    return " ".join(lista_limpa)    #Return the modified list.

frase_censurada = str(input("Digite a sua frase: "))    #Input: A list of strings and a single "forbidden" word.
palavra_censurada = str(input("Digite a palavra que deseja censurar: "))
print(censurar_lista(frase_censurada, palavra_censurada))
