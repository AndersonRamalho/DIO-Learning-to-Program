# DESAFIO Twitter  

# Entrada
# A entrada é uma linha de texto T com quantidades variadas de caracteres.

# Saída
# A saída é dada em uma única linha. 
# Ela deve ser "TWEET" (sem as aspas) se a linha de texto T tem até 140 caracteres. 
# Se T tem mais de 140 caracteres, a saída deve ser "MUTE".

# Código:

# Se não definir o tipo de input, por padrão é caracterizado como String
T = input()

# Se a quantidade de caracteres for menor ou igual a 140, está certo
if len(T) <= 140:
  print("TWEET")

# Se tiver mais de 140 caracteres, está errado, e vai para a segunda opção
else:
  print("MUTE")
