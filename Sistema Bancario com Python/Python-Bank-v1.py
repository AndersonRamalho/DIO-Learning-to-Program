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
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor_deposito = float(input("Digite o valor do depósito: R$ "))

        if valor_deposito <= 0:
            print("Valores zero ou negativos não são permitidos, tente novamente")
        else:
            saldo += valor_deposito
            print(f"Depósito realizado com sucesso, o saldo atualizado da sua conta é de R$ {saldo}")
            retorno = input("deseja retornar para o menu? y/n ")
            
            if retorno == "n":
                nova_operacao = input("deseja repetir a operação? y/n ")
                
            

    elif opcao == "s":
        print("Sacar")

    elif opcao == "e":
        print("Extrato")

    elif opcao == "q":
        print("Sessão Finalizada")
        break

    else:
        print("Operação inválida, tente novamente.")
