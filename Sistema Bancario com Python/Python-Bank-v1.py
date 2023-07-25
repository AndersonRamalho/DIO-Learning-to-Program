# Desafio DIO de criação de um sistema bancário versão 1.0

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

digite a opção desejada: 
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while true:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")

    elif opcao == "s":
        print("Sacar")

    elif opcao == "e":
        print("Extrato")

    elif opcao == "q":
        print("Sessão Finalizada")
        break

    else:
        print("Operação inválida, tente novamente.")


