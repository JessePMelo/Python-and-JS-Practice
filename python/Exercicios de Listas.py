# Utilizado PPO para melhor aproveitamento pratico.
#Exercicio Listas

class Exercicio_lista:
    def __init__(self):
        self.lista = []

    def __str__(self):
        return (f'Lista é: {self.lista}')
    
    #1 Crie uma lista de números inteiros
    def preencherLista(self):
        print("Crie uma lista de números inteiros. A lista para de ser preenchida quando digitar um número negativo.")
        negativo = False

        while not negativo:
            self.numero = int(input("Número: "))
            if self.numero < 0:
                negativo = True
            else:
                self.lista.append(self.numero)
    
    #2 mprima o maior número da lista.
    def maiorNumeroLista(self):
        self.maiorNumero = self.lista[0]
        for i in self.lista:
            if i > self.maiorNumero:
                self.maiorNumero = i
        print(f'Maior número: {self.maiorNumero}')

    #3 Imprima o menor número da lista.
    def menorNumeroLista(self):
        self.menorNumero = self.lista[0]
        for i in self.lista:
            if i < self.menorNumero:
                self.menorNumero = i
        print(f'Menor número: {self.menorNumero}')
    
    #4 Calcule a soma de todos os elementos da lista.
    def soma(self):
        self.somatoria = 0
        for i in self.lista:
            self.somatoria += i
        print(f'A soma dos números é: {self.somatoria}')

    #5 Calcule a média dos números.
    def media(self):
        if len(self.lista) > 0:
            self.somatoria = sum(self.lista)
            self.media = self.somatoria / len(self.lista)
            print(f'A média dos números é: {self.media}')
        else:
            print("A lista está vazia, não é possível calcular a média.")

    #6 Verifique se um número específico está na lista.
    def verificaNumero(self, numero:int):
        self.numeroVerificar = numero
        estaNaLista = False
        for i in self.lista:
            if self.numeroVerificar == i:
                estaNaLista = True
        if estaNaLista:
            print(f'O número {self.numeroVerificar} está na lista')
        else:
            print(f'O número {self.numeroVerificar} não está na lista')

    #7 lista de strings e ordene-a em ordem alfabética.
    def converteStringOrdena(self):
        self.listaStr = []
        for i in self.lista:
            self.listaStr.append(str(i))
        self.listaStrOrdenada = sorted(self.listaStr)
        print(f'Lista ordenada: {self.listaStrOrdenada}')

    #8 Faça um programa que leia uma lista de números e crie uma nova lista contendo apenas os números pares.
    def ordenaPares(self):
        numerosPares = []
        for i in self.lista:
            if i % 2 == 0:
                numerosPares.append(i)
        #print(f'Os numeros pares são {numerosPares}')

    #9 Faça um programa que receba uma lista de números e retorne a quantidade de números ímpares nela.
    def qtdImpares(self):
        numerosImpares = []
        for i in self.lista:
            if i % 2 !=0 :
                numerosImpares.append(i)
        print(f'Quantidade de numeros impares {len(numerosImpares)}')

    #10 Dada uma lista de números, crie um programa que remova o maior e o menor número da lista.
    def rmvMaiorMenor (self):
        #remove o menor
        self.lista.remove(min(self.lista))
        #remove o maior
        self.lista.remove(max(self.lista))
