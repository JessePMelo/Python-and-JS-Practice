# Utilizado PPO para melhor aproveitamento pratico.
#Exercicio Função

class ExercicioFuncao ():
    def __init__(self):
        pass

    #1 Crie uma função que receba um número e retorne o fatorial desse número.
    def fatorial(self, numero: int):
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        print(f'O fatorial de {numero} é {resultado}')


    #2 Crie uma função que receba dois números e retorne o maior divisor comum (MDC) entre eles.
    """
        Algoritmo de Euclides para cálculo do MDC (Máximo Divisor Comum):
        
        O algoritmo funciona da seguinte maneira:
        Primeiro, divide-se o maior número pelo menor e calcula-se o resto da divisão. 
        Se o resto for zero, o divisor da última divisão é o MDC. Caso o resto não seja zero, 
        substitui-se o maior número pelo menor e o menor número pelo resto, 
        e repete-se o processo até que o resto seja zero. 
        Quando o resto for zero, o divisor da última operação é o MDC.
        """
    def mdc(self, numero1: int, numero2: int):
            if numero1 < numero2:
                numero1, numero2 = numero2, numero1  
            
            while numero2 != 0:  
                resto = numero1 % numero2  # Calcula o resto da divisão
                numero1 = numero2  # O maior número se torna o número menor
                numero2 = resto  # O menor número se torna o resto

            # Quando numero2 for 0, o numero1 é o MDC
            print(f'O MDC é {numero1}')
    
    #3 Crie uma função que converta uma temperatura em Celsius para Fahrenheit.
    def c_para_f (self,grausC:float):
        grausF = (grausC * 9/5) + 32
        print(f'Graus Cº{grausC} em Fº{grausF}')

    #4 Crie uma função que calcule a soma de todos os múltiplos de 3 ou 5 abaixo de um número informado.
    def somaMultiplos(self,ateQueNumero:int):
        soma = int(0)
        lista_numeros = []
        for i in range(1,ateQueNumero):
             if i % 3 == 0 or i % 5 == 0:
                  lista_numeros.append(i)
                  soma += i
        
        print(f'Os numeros encontrados foras: {lista_numeros}\nSoma de todos os numeros multiplos de 3 e 5 com limite de {ateQueNumero} iniciando de 1: {soma}')

    #5Faça uma função que recebe uma lista de strings e retorne a string mais longa dessa lista.
    def maiorString(self,lista:list):
        maior =''
        for string in lista:
            if len(string) > len(maior):
                maior = string
        print(f'A maior string é "{maior}"')

x = ExercicioFuncao()
x.fatorial(5)
x.mdc(3,15)
x.c_para_f(25.8)
x.somaMultiplos(50)
x.maiorString(['abacaxi', 'bola', 'casa', 'elefante', 'futebol', 'girafa'])

