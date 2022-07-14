"""
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
escreva um programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: 
	Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""

def fib(numero):
    ultimo = 0
    penultimo = 1
    termo = 0
    lista = []

    if  numero == 0:
        print("Pertence a sequência de Fibonacci!")
    else:
        while termo <= numero:
            termo = ultimo + penultimo
            penultimo = ultimo
            ultimo = termo
            lista.append(termo)
        
        if numero in lista:
            print('Pertence a sequência de Fibonacci!')
        else:
            print("Não pertence a sequência de Fibonacci!")

numero = int(input("Digite um número inteiro para verificar se pertence a sequência de Fibonacci: "))

fib(numero)