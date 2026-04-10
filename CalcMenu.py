import math

while True:
    menu = input("Qual operação deseja? (soma, subtracao, multiplicacao, divisao, potencia, raiz): ")

    if menu == "soma":
        a = int(input("Digite o primeiro valor: "))
        b = int(input("Digite o segundo valor: "))
        resultado = a + b
        print(f"O resultado da soma é {resultado}.")

    elif menu == "subtracao":
        a = int(input("Digite o primeiro valor: "))
        b = int(input("Digite o segundo valor: "))
        resultado = a - b
        print(f"O resultado da subtração é {resultado}.")

    elif menu == "multiplicacao":
        a = int(input("Digite o primeiro valor: "))
        b = int(input("Digite o segundo valor: "))
        resultado = a * b
        print(f"O resultado da multiplicação é {resultado}.")

    elif menu == "divisao":
        a = int(input("Digite o primeiro valor: "))
        b = int(input("Digite o segundo valor: "))
        resultado = a / b
        print(f"O resultado da divisão é {resultado}.")

    elif menu == "potencia":
        a = int(input("Digite o primeiro valor (base): "))
        b = int(input("Digite o segundo valor (potência): "))
        resultado = a ** b
        print(f"O resultado da potência é {resultado}.")
        
    elif menu == "raiz":
        a = int(input("Digite o valor: "))
        resultado = math.sqrt(a)
        print(f"O resultado da raiz é {resultado}.")
        
    else:
        print("Resposta inválida.")
        continue

    sair = input("Cálculo concluído. Pressione Enter para calcular novamente ou digite 2 para sair: ")

    if sair == "2":
        break