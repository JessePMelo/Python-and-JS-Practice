#1 Crie uma função que, dado um número inteiro n, retorne uma lista contendo os primeiros n números fibonacci.
class Fibonacci:
    def __init__(self,posicaoFibonacci:int):
        self.posicao = posicaoFibonacci
        listaFibonacci = []
        indice0 = 0
        indice1 = 1

        while len(listaFibonacci) < self.posicao:
            numero = indice0 + indice1
            listaFibonacci.append(numero)

            indice0 = indice1
            indice1 = numero
        print (f'Lista fibonnaci até a posição {len(listaFibonacci)}: {listaFibonacci}')

#2 Crie uma classe Livro com os atributos título, autor e ano de publicação. Crie um método que imprima as informações do livro no formato "Título - Autor - Ano".
class Livro:
    def __init__(self, autor, titulo, ano):
        self.autor = autor
        self.titulo = titulo
        self.ano = ano

    def __str__(self):
        return (f'{self.titulo} - {self.autor} - {self.ano}')   

#3 Faça um programa que, dado um número de meses, calcule o saldo de uma conta bancária com juros compostos. Utilize uma classe para representar a conta e um método para calcular o saldo.
class Conta:
    def __init__(self, nConta,saldo:int):
        self.nConta = nConta
        self.saldo = saldo

    def calcSaldo (self,qtdMeses:int, jurosMensal:float):
        self.qtdMeses = qtdMeses
        self.jurosMensal = jurosMensal

        m = self.saldo * ( 1 + self.jurosMensal ) ** self.qtdMeses
        print(f'O saldo seria de {m:.2f}')

fibonacci=Fibonacci(10)
livro = Livro("Marcio Fernandes","Felicidade da lucro","2015")
print(livro)
conta = Conta('1',1000)
conta.calcSaldo(12,0.005)
