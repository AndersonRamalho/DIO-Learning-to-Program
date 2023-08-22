# Desafio DIO de criação de um sistema bancário versão 1.0

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

digite a opção desejada: """

saldo = float(0)
limite = float(500)
extrato = ""
numero_saques = 0
numero_depositos = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("\n============ Depósito ===========\n")
        valor_deposito = float(input("Digite o valor do depósito: R$ "))

        if valor_deposito <= 0:
            print("Valores zero ou negativos não são permitidos, tente novamente")
        else:
            saldo += valor_deposito
            numero_depositos += 1
            extrato += f"Depósito {numero_depositos}: R$ {valor_deposito:.2f}\n"

            print(f"Depósito realizado com sucesso, o saldo atualizado da sua conta é de R$ {saldo:.2f}\n")
            print("\n==============================\n")

    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques atingido, operação cancelada")
        else:    
            print("\n============ Sacar ===========\n")
            valor_saque = float(input("Digite o valor do saque: R$ "))

            if valor_saque <= 0:
                print("Valores zero ou negativos não são permitidos, tente novamente")
            elif valor_saque > saldo:
                print(f"Saque maior que saldo atual da conta de R$ {saldo:.2f}, tente novamente conforme saldo disponível")
            elif valor_saque > 500:
                print("Saque acima de R$ 500.00 não permitido em uma única transação, tente novamente")
            elif numero_saques >= LIMITE_SAQUES:
                print("Limite de saques atingido, operação cancelada")
            else:
                numero_saques += 1
                saldo -= valor_saque
                extrato += f"Saque {numero_saques}: R$ -{valor_saque:.2f}\n"
                print(f"Saque realizado com sucesso, saldo disponível atualizado é de R$ {saldo:.2f}\n")
                print("\n==============================\n")

    elif opcao == "e":
        print("\n===================== Extrato ==============\n")
        print(extrato)
        print(f"Seu Saldo atual é de R$ {saldo:.2f}\n")
        print("\n==============================\n")


    elif opcao == "q":
        print("Sessão Finalizada")
        break

    else:
        print("Operação inválida, tente novamente.")
