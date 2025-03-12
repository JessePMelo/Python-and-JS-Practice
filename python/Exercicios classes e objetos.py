#1  Crie uma classe chamada Carro com os atributos marca, modelo e ano. Adicione um método exibir_info que imprima as informações do carro.
class Carro:
    def __init__(self,marca:str,modelo:str,ano:int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_info(self):
        print(f'Marca:{self.marca}\tModelo:{self.modelo}\tAno:{self.ano}')

#2 Crie uma classe Aluno com os atributos nome, idade e notas. Adicione um método media que retorne a média das notas do aluno.
class Aluno:
    def __init__(self,nome:str,idade:int,notas:list[float]):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def media (self):
        mediaNotas = sum(self.notas)/len(self.notas)
        print(f' A media é: {mediaNotas}')

#3 Crie uma classe Pessoa com os atributos nome e idade. Adicione um método aniversario que aumenta a idade da pessoa em 1 ano.
class Pessoa:
    def __init__(self,nome:str,idade:int):
        self.nome = nome
        self.idade = idade

    def aniversario (self):
        self.idade += 1
        
#4 Crie uma classe Retangulo com os atributos largura e altura. Adicione métodos para calcular a área e o perímetro do retângulo.
class Retangulo:
    def __init__(self,altura:float, largura:float):
        self.altura = altura
        self.largura = largura
    
    def calcPerimetro(self):
        p =  (self.altura * 2) + (self.largura + 2)
        print(f'Perimetro : {p}')
    
    def calcArea (self):
        a = self.altura * self.largura
        print (f'Area: {a}')

#5 Crie uma classe ContaBancaria com os atributos titular e saldo. Adicione métodos para depositar e sacar valores, além de um método que exiba o saldo atual.
class contaBancaria:
    def __init__(self,titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def exibirSaldo(self):
        print(f'Saldo: {self.saldo}')

    def depositar (self,valor):
        self.saldo += valor
    
    def sacar (self,valorSacar):
        self.saldo -= valorSacar

c = Carro('Toyota','Etios',2017)
c.exibir_info()

a = Aluno('Lucas',31,[5,5,5])
a.media()

p = Pessoa('Carlos',55)
p.aniversario()
print(f'A idade é: {p.idade}')

r= Retangulo(4,6)
r.calcArea()
r.calcPerimetro()

co = contaBancaria('Jess',5000)
co.exibirSaldo()
co.depositar(100)
co.sacar(25)
co.exibirSaldo()

