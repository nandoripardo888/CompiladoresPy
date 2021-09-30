from analisadorSintatico import *
import os


print("serão analisados todos os algoritmos que estão na pasta com estensão txt")
lista=[]
for diretorio, subpastas, arquivos in os.walk("./"):
    for arquivo in arquivos:
        if arquivo.endswith(".txt") and not(arquivo.endswith("_saida.txt")):
            lista.append(os.path.join(diretorio, arquivo))


print(lista)
for arq in lista:
    sintatico = AnalisadorSintatico(arq)
    sintatico.analise()
    print(sintatico.tabelaHASH.tabelaSimbolo)