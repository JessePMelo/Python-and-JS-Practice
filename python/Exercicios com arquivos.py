# 1 Crie um programa que leia o conteúdo de um arquivo de texto e imprima no console.
with open ('texto/texto_exercicio-4.1.txt',mode='r',encoding='utf-8') as arquivo:
    texto = arquivo.read()
print(texto)

#2 Crie um programa que receba uma lista de strings e escreva cada item da lista em um arquivo de texto (cada string em uma linha).
lista = ['caderno','papel','caneta','borracha','lapis']
with open('texto/texto_exercicio-4.2.txt',mode='w',encoding='UTF-8') as arquivo2:
    for i in range(len(lista)):
        arquivo2.write(lista[i]+'\n')

3# Crie um programa que leia um arquivo CSV (arquivo separado por vírgulas) e imprima o conteúdo de cada linha.
import csv
with open('texto/dados.csv',mode='r',encoding='utf-8') as arquivocsv:
    tabela = csv.reader(arquivocsv)
    for linha in tabela:
        print(linha)

#4 Faça um programa que leia um arquivo de texto e conte o número de palavras no arquivo.
with open ('texto/texto_exercicio-4.4.txt',mode='r',encoding='UTF-8') as arquivo3:
    texto = arquivo3.read()
    texto.strip()
    palavra = 0
    for caracter in texto:
        if caracter == " ":
            palavra += 1
    print(f'O texto possui {palavra} palavras')

#5 Crie um programa que crie um arquivo de texto e escreva a soma de números gerados aleatoriamente entre 1 e 1000.
import random
numero  = random.randint(1,1000)
soma = 0
lista = []
for i in range (numero):
    numero2 = random.randint(1,1000)
    lista.append(numero2)
    soma+= numero2
with open('texto/texto_exercicio-4.5.txt',mode='w',encoding='utf-8') as arquivo4:
    arquivo4.write(f'Os numero gerados foram: {lista}\nA soma foi:{soma}')