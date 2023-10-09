# Desenvolva um programa em Python que apure o resultado de uma votação para determinar 
# o personagem favorito do desenho “The Simpsons”. Suponha que existam 2 candidatos cujos códigos são:

# 1 - Bart
# 2 - Homer
 
# Considere que existe uma função que recebe e escreve em um arquivo .txt 
# ou em uma lista/vetor os votos de 5 pessoas. Um voto é representado 
# pelo código de identificação do candidato.

# Na sequência, uma função para leitura deverá ser implementada, a qual deverá apresentar, como resultado:

#o nome e a quantidade de votos do candidato mais votado
# o nome e a quantidade de votos do menos votado
# quantidade de votos nulos (um voto nulo é um voto cujo código de identificação é um valor diferente de 1 e 2). 

# LISTAS E ABERTURAS DE ARQUIVO

listaBart = []
listaHomer = []
listaNulos = []
contagemBart = open('urnaBart.txt', 'w', encoding='utf-8')
contagemHomer = open('urnaHomer.txt', 'w', encoding='utf-8')
contagemNulos = open('urnaNulos.txt', 'w', encoding='utf-8')

# FUNÇÕES DO PROGRAMA

def votos():
    for i in range(5):
        programa = input("Digite o seu personagem favorito: [1] Bart [2] Homer")
        if programa == "1":
            listaBart.append(programa)
        elif programa == "2":
            listaHomer.append(programa)
        else:
            listaNulos.append(programa)

def executar():
    if quantBart > quantHomer:
        print(f"Bart é o personagem mais querido dos Simpsons com {quantBart} votos. Homer recebeu {quantHomer} votos. Votos nulos foram {quantNulos}.")
    elif quantHomer > quantBart:
        print(f"Homer é o personagem mais querido dos Simpsons com {quantHomer} votos. Bart recebeu {quantBart} votos. Votos nulos foram {quantNulos}.")
    elif quantHomer == quantBart:
        print(f"Bart e Homer ficaram empatados com {quantHomer} votos. Votos nulos foram {quantNulos}.")
    else:
        print(f"A maioria dos votos foram nulos, com total de {quantNulos}. Pesquisa anulada.")

# EXECUTANDO O PROGRAMA - As listas só foram criadas após a execução completa do programa.

votos()

# PASSANDO A LISTA PARA ARQUIVO - Somente após a função votos() ser executada que as listas puderam ser transformadas em arquivos.

contagemBart.writelines("\n".join(listaBart))
contagemHomer.writelines("\n".join(listaHomer))
contagemNulos.writelines("\n".join(listaNulos))
        
# FECHANDO O ARQUIVO PARA ESCREVER.

contagemBart.close()
contagemHomer.close()
contagemNulos.close()

# ABRINDO PARA LEITURA E CONTANDO AS STRINGS - Arquivos reabertos somente para leitura.

contagemBart = open('urnaBart.txt', 'r', encoding='utf-8')
contagemHomer = open('urnaHomer.txt', 'r', encoding='utf-8')
contagemNulos = open('urnaNulos.txt', 'r', encoding='utf-8')

lendoBart = contagemBart.read()
lendoHomer = contagemHomer.read()
lendoNulos = contagemNulos.read()

# Na contagem de strings, as quebras de linhas também foram contabilizadas, 
# por isso foi utilizado o replace para substituir os \n por strings vazias

quantBart = len(lendoBart.replace("\n", ""))
quantHomer = len(lendoHomer.replace("\n", ""))
quantNulos = len(lendoNulos.replace("\n", ""))

# Fechando o arquivo.

contagemBart.close()
contagemHomer.close()
contagemNulos.close()

# Executando lógica da contagem.

executar()