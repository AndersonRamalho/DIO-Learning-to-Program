# Desafio
# Verificar se a partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

# Entrada
# A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. 
# Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.

# Saída
# Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor ou não.

# Código:

# Input inicial de valor inteiro
n = int(input())

# Chave de Repetição, enquanto n for maior que 0

while(n > 0):
    # Esse -= corresponde a subtração de 1 no valor de n definido no Input
    n -= 1
    # Vai ser realizado mais 01 input, com um espaço no meio, e o comando Split vai dividir em 02 a partir do espaço
    a, b = input().split()
    # Condicional Se a quantidade de caracteres de a for menor que b, irá dar falso
    if(len(a) < len(b)):
        print('nao encaixa')
    # Se não for menor, vai pra proxima condição  
    else:
    # Se subtratir a quantidade de caracteres de "a" da esquerda pra direita até ficar só a quantidade de caracteres de "b"
    # Vai verificar se "a"(subtraido os caracteres a mais) é igual a "b"
        if(a[len(a)-len(b)::] == b):
            print('encaixa')
        else:
            print('nao encaixa')


# a parte do código "[len(a)-len(b)::] quer dizer que o número inicial que ele vai considerar para pesquisar é 
# a partir da subtração da quantidade de caracteres de "a" menos "b"
