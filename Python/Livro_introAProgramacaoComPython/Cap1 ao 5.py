"""Cap. 1 não há exercicios.

Cap. 2</p>
Exercício 2.1 Converta as seguintes expressões matemáticas para que possam ser calculadas usando o interpretador Python.

- 10 + 20 x 30</p>
- 4² / 30</p>
- (9^4 + 2) x 6 - 1</p>
"""

# @title
a,b,c = 10, 20, 30
d,e = 4, 2
f,g,h = 9, 6, 1

print("{} + {} x {} = {}\n{} / {} = {:.2f}\n{} x {} - {} = {}".format(a,b,c,a+b*c,d**e,c,d**e/c,f**d+e,g,h,(f**d+e)*g-h))

"""Exercício 2.2 Digite a seguinte expressão no interpretador:

10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2

Tente resolver o mesmo cálculo, usando apenas lápis e papel. Observe como a prioridade das operações é importante
"""

# @title
i=3
resultado = (a%i)*(a**e)+h-(a*d/e)
print(resultado)

"""Exercício 2.3 Faça um programa que exiba seu nome na tela."""

print('Bruno R C Coelho')

"""Exercício 2.4 Escreva um programa que exiba o resultado de 2a × 3b, onde a vale
3 e b vale 5
"""

a = 3
b = 5
print(2*a*3*b)

"""Exercício 2.5 Modifique o primeiro programa, listagem 2.7, de forma a calcular a
soma de três variáveis.
"""

x = 2
y = 3
z = 4
print(x+y+z)

"""Exercício 2.6 Modifique o programa da listagem 2.11, de forma que ele calcule um
aumento de 15% para um salário de R$ 750.
"""

salario = 750
aumento = 15
print (salario + (salario * aumento / 100))

"""Cap. 3

Os exercícios 3.1, 3.2, 3.3 e 3.5 por serem de multipla escolha não serão resolvidos nesse arquivo

Exercício 3.4 Escreva uma expressão para determinar se uma pessoa deve ou não
pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que
R$ 1.200,00
"""

salario = int(input('Digite o salario: '))
if salario > 1200:
  print(True)
else:
  print(False)

"""Exercício 3.6 Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3."""

materia_1 = int(input("Nota da matéria 1 :"))
materia_2 = int(input("Nota da matéria 2 :"))
materia_3 = int(input("Nota da matéria 3 :"))

media = (materia_1+materia_2+materia_3)/3
print(media>=7)

"""Exercício 3.7 Faça um programa que peça dois números inteiros. Imprima a soma
desses dois números na tela
"""

numero_um = int(input('Digite um número'))
numero_dois = int(input('Digite um número'))
print('A soma dos números é de:',(numero_um+numero_dois))

"""Exercício 3.8 Escreva um programa que leia um valor em metros e o exiba convertido em milímetros."""



"""Exercício 3.9 Escreva um programa que leia a quantidade de dias, horas, minutos
e segundos do usuário. Calcule o total em segundos.
"""



"""Exercício 3.10 Faça um programa que calcule o aumento de um salário. Ele deve
solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento
e do novo salário.
"""



"""Exercício 3.11 Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar."""



"""Exercício 3.12 Escreva um programa que calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada para a viagem
"""



"""Exercício 3.13 Escreva um programa que converta uma temperatura digitada em
°C em °F. A fórmula para essa conversão é:  C = 5 * ((F-32) / 9).
"""

fahr = int(input("Digite a temperatura em Fahrenheit (°F): "))
celcius = 5*((fahr-32)/9)
print("A temperatura em celcius é", round(celcius,2),"°C")

"""Exercício 3.14 Escreva um programa que pergunte a quantidade de km percorridos
por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais
o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R\$ 60 por dia e R$ 0,15 por km rodado.
"""



"""Exercício 3.15 Escreva um programa para calcular a redução do tempo de vida de
um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro,
calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
"""
