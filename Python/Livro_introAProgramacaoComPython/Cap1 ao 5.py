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

metro = int(input("Digite o valor do metro:"))
print('{} metros tem {} milimetros'.format(metro,metro*1000))

"""Exercício 3.9 Escreva um programa que leia a quantidade de dias, horas, minutos
e segundos do usuário. Calcule o total em segundos.
"""

dias = int(input("Quantos dias?"))
horas = int(input("Quantos horas?"))
minutos = int(input("Quantos minutos?"))
segundos = int(input("Quantos segundos?"))

conversao = (dias*24*60*60)+(horas*60*60)+(minutos*60)+(segundos)
print('{} dias, {} horas, {} minutos e {} seguntos. Possuem {} segundos.'.format(dias, horas, minutos, segundos, conversao))

"""Exercício 3.10 Faça um programa que calcule o aumento de um salário. Ele deve
solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento
e do novo salário.
"""

salario_2 = float(input("Digite o valor do salário "))
aumento = float(input("Digite a porcentagem do aumento "))
valor_aumentado = salario_2*(aumento/100)
print('O aumento foi de R${:.2f}, ficando o novo salário no valor de R${:.2f}'.format((valor_aumentado), salario_2+valor_aumentado))

"""Exercício 3.11 Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar."""

mercadoria = float(input('Digite o preço da mercadoria: '))
desconto = float(input("Digite o percentual de desconto: "))
valor_desconto = mercadoria * (desconto/100)
print('O desconto foi de R${:.2f}, ficando no valor de R${:.2f}'.format((valor_desconto/100)*mercadoria, mercadoria-valor_desconto))

"""Exercício 3.12 Escreva um programa que calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada para a viagem
"""

distancia = float(input('Qual a distância a ser percorrida?'))
veloc_media = float(input('Qual a velocidade média? (Km/h)'))

print('A distância será percorrida em {:.1f}h'.format(distancia/veloc_media))

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

km_carro_aluguado = float(input('Quantidade de Km percorrido?'))
dia_carro_alugado = float(input('Quantidade de dias que o carro foi alugado?'))
valor_total = km_carro_aluguado*0.15+dia_carro_alugado*60
print('O valor total do aluguel do carro foi de R${:.2f}'.format(valor_total))

"""Exercício 3.15 Escreva um programa para calcular a redução do tempo de vida de
um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro,
calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
"""

qtd_cigarros = int(input('Quantidade de cigarros por dia?'))
anos_fumante = int(input('Por quantos anos você foi fulmante?'))
perda_de_vida = qtd_cigarros*365*anos_fumante*10
dias_perdidos = perda_de_vida/60/24
print('Você perdeu {:.2f} dias de vida'.format(dias_perdidos))

"""Cap. 4</p>
Exercicio 4.1 não se aplica</p>
Exercício 4.2 Escreva um programa que pergunte a velocidade do carro de um
usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário
foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de
80 km/h
"""

velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
  multa = velocidade - 80
  print('O motorista foi multado. Com o valor de R${:.2f} de multa'.format(multa*5))

"""Exercício 4.3 Escreva um programa que leia três números e que imprima o maior
e o menor.
"""

numero_one = float(input(""))
numero_two = float(input(""))
numero_three = float(input(""))
lista = []
lista.append(numero_one)
lista.append(numero_two)
lista.append(numero_three)
print(max(lista))

"""Exercício 4.4 Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%."""

salario_fun = float(input("Qual o salário? "))
if salario_fun > 1250:
  print(f"O salario com aumento ficou R${salario_fun*1.1:.2f}")
else:
  print(f"O salario com aumento ficou R${salario_fun*1.15:.2f}")
  
"""Exercício 4.6 Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas. """

distancia_w = float(input('Qual a distancia? '))
if distancia_w <= 200:
  print(f'O preço da viagem é de R${distancia_w*0.5:.2f}')
else:
  print(f'O preço da viagem é de R${distancia_w*0.45:.2f}')

"""Exercício 4.8 Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada. """

number_one = int(input())
number_two = int(input())
operação = input('Qual operação você deseja realizar? ( +, -, * ou /) ')
if operação == '+':
  print(number_one + number_two)
elif operação == '-':
  print(number_one - number_two)
elif operação == '*':
  print(number_one * number_two)
else:
  print(number_one / number_two)

"""Exercício 4.9 Escreva um programa para aprovar o empréstimo bancário para
compra de uma casa. O programa deve perguntar o valor da casa a comprar, o
salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser
superior a 30% do salário. Calcule o valor da prestação como sendo o valor da
casa a comprar dividido pelo número de meses a pagar. """

valor_casa = float(input('Qual o valor da casa? '))
receita = float(input('Qual o salario do comprador? '))
anos_pag = int(input('Em quantos anos deseja quitar a casa? '))
prestacao = valor_casa/(12*anos_pag)
barramento = receita*0.3

if barramento < prestacao:
  print('Emprestimo não consedido')
else:
  print(f'O valor da prestação será de {prestacao}')

"""Exercício 4.10 Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir. <code>Preço por tipo e faixa de consumo</code>
|Tipo|Faixa(kWh)|Preço|
|--|--|--|
|Residêncial|Até 500</p>Acima de 500|R\$ 0,40 </p> R\$ 0,65 |
|Comercial|Até 1000</p>Acima de 1000|R\$ 0,55 </p> R\$ 0,60 |
|Industrial|Até 5000</p>Acima de 5000|R$ 0,40 </p> R\$ 0,65| """

qnt_kwh = float(input('Qnt de kWh? '))
tipo_inst = input('Qual o tipo de instalação? \n( R para residências, I para indústrias e C para comércios) ')
if tipo_inst == 'R' or tipo_inst == 'r':
  if qnt_kwh <=500:
    print(f'A conta de energia será de R${qnt_kwh*0.4:.2f}')
  else:
    print(f'A conta de energia será de R${qnt_kwh*0.65:.2f}')
elif tipo_inst == 'C' or tipo_inst == 'c':
  if qnt_kwh <=1000:
    print(f'A conta de energia será de R${qnt_kwh*0.55:.2f}')
  else:
    print(f'A conta de energia será de R${qnt_kwh*0.6:.2f}')
elif tipo_inst == 'I' or tipo_inst == 'i':
  if qnt_kwh <=5000:
    print(f'A conta de energia será de R${qnt_kwh*0.4:.2f}')
  else:
    print(f'A conta de energia será de R${qnt_kwh*0.65:.2f}')
else:
  print('Digite um tipo de instalação válido')

"""Cap. 5 </p>
Exercício 5.1 Modifique o programa para exibir os números de 1 a 100 """

interacao = 1
while interacao <= 100:
  print(interacao)
  interacao += 1

"""Exercício 5.2 Modifique o programa para exibir os números de 50 a 100."""

interacao = 50
while interacao <= 100:
  print(interacao)
  interacao += 1

"""Exercício 5.3 Faça um programa para escrever a contagem regressiva do lançamento
de um foguete. O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela.
"""

cont_regressiva = 10
while cont_regressiva > 0:
  print(cont_regressiva)
  cont_regressiva -= 1
print('0 \n' 'Fogo!')

"""Exercício 5.4 Modifique o programa anterior para imprimir de 1 até o número
digitado pelo usuário, mas, dessa vez, apenas os números ímpares.
"""

cont_regressiva2 = int(input('Até qual número é a contagem? '))
contagemzero = 1
while contagemzero <= cont_regressiva2:
  print(contagemzero)
  contagemzero += 2

"""Exercício 5.5 Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3."""

multiplosdetres = 3
while multiplosdetres <= 30:
  print(multiplosdetres)
  multiplosdetres += 3

"""Exercício 5.6 Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2=4, ..."""

tabuada = int(input('Tabuada de: '))
sequencia = 1
while sequencia <= 10 :
  print(f'{tabuada}x{sequencia} = {tabuada*sequencia}')
  sequencia = (sequencia+1)

"""Exercício 5.7 Modifique o programa anterior de forma que o usuário também
digite o início e o fim da tabuada, em vez de começar com 1 e 10.
"""

tabuada2 = int(input('Tabuada de: '))
inicio = int(input('Inicio da tabuada: '))
final = int(input('Fim da tabuada: '))
while inicio <= final :
  print(f'{tabuada2}x{inicio} = {tabuada2*inicio}')
  inicio += 1

"""Exercício 5.8 Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e
subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles.

Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.
"""

termo_1 = int(input())
termo_2 = int(input())
ponto = 0
while ponto < termo_1*termo_2:
  ponto += termo_1
print(f'{termo_1} x {termo_2} =', ponto)

"""Exercício 5.9 Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20."""

"""Exercício 5.10 Modifique o programa da listagem 5.10 para que aceite respostas com letras maiúsculas e minúsculas em todas as questões."""

"""Exercicio 5.11 Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período."""

"""Exercício 5.12 Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte."""

"""Exercício 5.13 Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago."""

"""Exercício 5.14 Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite O (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética."""

"""Exercício 5.15 Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de códigos abaixo para obter o preço de cada produto:
| Código | Preço |
|--|--|
| 1 |0,50 |
| 2| 1,00|
| 3| 4,00|
| 5| 7,00|
| 9|8,00 |
Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro código deve gerar a mensagem de erro "Código inválido".

"""Exercício 5.16 Execute o programa (Listagem 5.14) para os seguintes valores: 501, 745, 384, 2,7 e 1. Exercício 5.17 O que acontece se digitarmos 0 (zero) no valor a pagar?"""

"""Exercicio 5.18 Modifique o programa para também trabalhar com notas de R$ 100."""

"""Exercado 5.19 Modifique o programa para aceitar valores decimais, ou seja, também contar moedas de 0,01, 0,02, 0,05, 0,10 e 0,50."""

"""Exercício 5.20 O que acontece se digitarmos 0,001 no programa anterior? Caso ele não funcione, altere-o de forma a corrigir o problema."""

"""Exercício 5.21 Reescreva o programa da listagem 5.14 de forma a continuar executando até que o valor digitado seja 0. Utilize repetições aninhadas."""

"""Exercício 5.22 Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida. Repita até que a opção saída seja escolhida."""

"""Exercício 5.23 Escreva um programa que leia um número e verifique se é ou não um número primo. Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número lido. Se o resto de uma dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1 não são primos e que 2 é o único número primo que é par."""

"""Exercício 5.24 Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos."""

"""Exercício 5.25 Escreva um programa que calcule a raiz quadrada de um número. Utilize o método de Newton para obter um resultado aproximado. Sendo n o número a obter a raiz quadrada, considere a base b=2. Calcule p usando a fórmula p=(b+(n/b))/2. Agora, calcule o quadrado de p. A cada passo, faça b=p e recalcule p usando a fórmula apresentada. Pare quando a diferença absoluta entre n e o quadrado de p for menor que 0,0001."""

"""Exercício 5.26 Escreva um programa que calcule o resto da divisão inteira entre dois números. Utilize apenas as operações de soma e subtração para calcular o resultado."""

"""Exercício 5.27 Escreva um programa que verifique se um número é palíndromo. Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos. Exemplos: 454, 10501 """
