"""
Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
	a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
	b) Evite usar funções prontas, como, por exemplo, reverse;
"""

def inverte(palavra):
    tamanho = len(palavra)
    palavra_invertida = []
    while tamanho > 0:
        palavra_invertida += palavra[tamanho-1]
        tamanho -= 1

    print(''.join(palavra_invertida))
    
inverte('palavra')