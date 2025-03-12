#1Faça um programa que leia dois arquivos de texto e escreva um terceiro arquivo com as linhas dos dois arquivos intercaladas.
with open('texto/exemplo_manipulacao_lista_arquivos1.txt',mode='r',encoding='utf-8') as arquivo1:
    with open('texto/exemplo_manipulacao_lista_arquivos2.txt',mode='r',encoding='utf-8') as arquivo2:
        with open('texto/resolucao-exercicio_maipulacao_lista_arquivos-1.txt',mode='w',encoding='utf-8') as arquivo:
            texto1 = arquivo1.readlines()
            texto2 = arquivo2.readlines()
            
            if len(texto1) == len(texto2):
                for i in range(0,len(texto1)):
                    arquivo.write(texto1[i].strip() + '\n')
                    arquivo.write(texto2[i].strip() + '\n')
            
            else:
                if len(texto1) > len(texto2):
                    maior = texto1
                    menor = texto2
                else:
                    maior=texto2
                    menor=texto1
                
                for i in range(0,len(maior)):
                    if i < (len(menor)):
                        arquivo.write(maior[i].strip() + '\n')
                        arquivo.write(menor[i].strip() + '\n')                    
                    else:
                        arquivo.write(maior[i].strip() + '\n')

#2 Crie uma função que recebe um arquivo de texto e retorna o número de caracteres que uma palavra específica aparece nesse arquivo.
import re
with open('texto/texto_exemplo_manipulacao_listas_arquivos-2.txt',mode='r',encoding='utf-8') as frutas:
    texto_frutas = frutas.readline()
    palavra = str(input('Digite uma palavra: '))
    procura = re.search(rf'{palavra}',texto_frutas)
    if procura:
        print('Encontrou a palavra')
    else:
        print('Não encontrou')

#3 Faça um programa que leia um arquivo de texto contendo uma lista de números e escreva em um novo arquivo a soma dos números.
with open ('texto/texto_exemplo_manipulacao_listas_arquivos-3.txt', mode='r',encoding='utf-8') as file:
    texto = file.readlines()
    soma = 0
    for linha in texto:
        palavras = linha.split()
        for palavra in palavras:
            try:
                soma += float(palavra)
            except ValueError:
                continue

with open ('texto/resolucao-exercicio_maipulacao_lista_arquivos-3.txt',mode='w',encoding='UTF-8') as arquivo3:
    arquivo3.write(f'Soma é {soma}')
