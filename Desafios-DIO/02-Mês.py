# Desafio
# Leia um valor inteiro entre 1 e 12, inclusive. 
# A Resposta deve ser o mês referente ao número digitado, em Inglês

# Entrada
# A entrada contém um único valor inteiro.

# Saída
# Imprima por extenso o nome do mês correspondente ao número da entrada.

# Código:

# Entrada definida para número inteiro
month = int(input())

# Criação de um dicionário, para relacionar o número com o Mês
months_dict = {
1:"January", 
2:"February",
3:"March",
4:"April",
5:"May",
6:"June",
7:"July",
8:"August",
9:"September",
10:"October",
11:"November",
12:"December"
}

# Exibe o mês correspondente ao número digitado
print(months_dict[month])
