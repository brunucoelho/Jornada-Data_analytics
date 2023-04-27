#Exercício 3.1
#Escreva uma função chamada right_justify, que receba uma string chamada s como parâmetro e exiba a string com espaços suficientes à frente para que a última letra da string esteja na coluna 70 da tela: >>> right_justify('monty')                                                                 monty

def right_justify(str):
    texto = str
    print(' '*(70-len(texto))+texto)

#Exercício 3.2
#Um objeto de função é um valor que pode ser atribuído a uma variável ou passado como argumento. Por exemplo, do_twice é uma função que toma um objeto de função como argumento e o chama duas vezes:
#def do_twice(f):
#f()
#f()
#Aqui está um exemplo que usa do_twice para chamar uma função chamada print_spam duas vezes:
#def print_spam():
#print('spam')
#do_twice(print_spam)

def do_twice(f, valor):
    f(valor)
    f(valor)

def print_twice(valor):
    print(valor)
    print(valor)

def do_four(f, valor):
    do_twice(f, valor)
    do_twice(f, valor)

do_twice(print, 'spam')
print('-'*7)

do_four(print, 'spam')

#Exercício 3.3
#Escreva uma função que desenhe uma grade como a seguinte:

#Dica: para exibir mais de um valor em uma linha, podemos usar uma sequência de valores separados por vírgula: print('+', '-')
#Por padrão, print avança para a linha seguinte, mas podemos ignorar esse comportamento e inserir um espaço no fim, desta forma: python print('+', end='') print('-') A saída dessas instruções é + -. Uma instrução print sem argumento termina a linha atual e vai para a próxima linha.