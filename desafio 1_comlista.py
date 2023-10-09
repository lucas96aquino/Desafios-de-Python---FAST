# Desenvolva um programa em Python que apure o resultado de uma votação para
# determinar o personagem favorito do desenho “The Simpsons”. Suponha que
# existam 2 candidatos cujos códigos são:

# 1 - Bart
# 2 - Homer

# Considere que existe uma função que recebe e escreve em um arquivo .txt ou
# em uma lista/vetor os votos de 5 pessoas.
# Um voto é representado pelo código de identificação do candidato.

# Na sequência, uma função para leitura deverá ser implementada,
# a qual deverá apresentar, como resultado:

# o nome e a quantidade de votos do candidato mais votado
# o nome e a quantidade de votos do menos votado
# quantidade de votos nulos (um voto nulo é um voto cujo código de identificação
# é um valor diferente de 1 e 2).

# FUNÇÕES DO PROGRAMA

def voto():
  programa = int(input("Registre seu voto: [1] Bart [2] Homer: "))
  if programa == 1:
    listaBart.append(programa)
  elif programa == 2:
    listaHomer.append(programa)
  else:
    listaNulos.append(programa)

def executar():
  if len(listaHomer) > len(listaBart):
    print(f"O personagem mais votado foi Homer com {len(listaHomer)} votos e o menos votado foi Bart com {len(listaBart)} voto(s). Houve um total de {len(listaNulos)} voto(s) nulo(s).")
  elif len(listaBart) > len(listaHomer):
    print(f"O personagem mais votado foi Bart com {len(listaBart)} votos e o menos votado foi Homer com {len(listaHomer)} voto(s). Houve um total de {len(listaNulos)} voto(s) nulo(s).")
  else:
    print(f"Bart e Homer empataram com {len(listaHomer)} e {len(listaBart)} votos. Houve um total de {len(listaNulos)} votos nulo(s).")

# LISTAS

listaBart = []
listaHomer = []
listaNulos = []

# EXECUÇÃO

for i in range(5):
  voto()

executar()