# -*- coding: utf-8 -*-
"""OK_EstruturaSequencial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1suGJ19AGFja4ftS_MkMQLAy--YAfqRUB

# Lista de exercícios 📚 ||  Python <img src="https://img.icons8.com/dusk/512/python.png" alt="drawing" width="40"/>

_________________________________________________________________________

Exercicios feitos por mim para aplicação dos conhecimentos adquiridos nos estudos. Estou seguindo o RoadMap Python, <https://roadmap.dunossauro.live/>. Fornecido pelo [@dunossauro](https://linktr.ee/dunossauro). A lista pode ser encontrada em [wikiPython](https://wiki.python.org.br/ListaDeExercicios).
_________________________________________________________________________

1. Faça um Programa que mostre a mensagem "Alo mundo" na tela
"""

print("Alo mundo")

"""2. Faça um Programa que peça um número e então mostre a mensagem ```O número informado foi [número].```"""

x = input('Digite um número inteiro:')
print(f'O número informado foi {x}.')

"""3. Faça um Programa que peça dois números e imprima a soma."""

x, y = int(input('Digite o 1º número inteiro:')), int(input('Digite o 2º número inteiro:'))
soma = x+y
print (f'A soma dos números informados é {soma}')

"""4. Faça um Programa que peça as 4 notas bimestrais e mostre a média."""

nota1= int(input("Digite a 1ª nota: "))
nota2= int(input("Digite a 2ª nota: "))
nota3= int(input("Digite a 3ª nota: "))
nota4= int(input("Digite a 4ª nota: "))
media = [nota1, nota2, nota3, nota4]
soma_notas= sum(media)
qnt = len(media)
print("A média é", soma_notas/qnt)

"""5. Faça um Programa que converta metros para centímetros."""

medida_metro = float(input("Digite o comprimento em metros para ser convertido em cm: "))
medida_cm = medida_metro*100

print("A nova medida é", medida_cm, "cm.")

"""6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área."""

import math
raio = float(input("Qual o raio do circulo (cm)? "))
area_circulo = math.pi*(raio**2)
print("A área do circulo é ",round(area_circulo, 2),"cm²")

"""7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário."""

lado_q = int(input("Digite o comprimento do lado do quadradro (cm): "))
area_qdd = lado_q*lado_q
dobro_area = area_qdd*2
print("A área do quadrado é de",area_qdd, "cm² e o dobro da área e de", dobro_area, "cm²")

"""8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês."""

preco_hr = float(input("Quanto você ganha por hora?: "))
horas_mes = int(input("Quantas horas trabalhada no mês?"))
salario = preco_hr*horas_mes
print("O seu salário esse mês será de R$",salario,)

"""9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""

fahr = int(input("Digite a temperatura em Fahrenheit (°F): "))
celcius = 5*((fahr-32)/9)
print("A temperatura em celcius é", round(celcius,2),"°C")

"""10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit."""

celcius_2 = float(input("Digite a temperatura em Celsius (°C): "))
fahr_2 = ((celcius_2)*9)/5+32
print("A temperatura em fahrenheit é", round(fahr_2,2),"°F")

"""11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
- o produto do dobro do primeiro com metade do segundo .
- a soma do triplo do primeiro com o terceiro.
- o terceiro elevado ao cubo.
"""

numint1= int(input("Digite um número inteiro: "))
numint2= int(input("Digite o segundo número inteiro: "))
numreal= float(input("Digite um número real: "))
produto = (2*numint1)*(numint2/2)
soma = (3*numint1)+(3*numint2)
cubo = numreal**3
print(produto)
print(soma)
print(cubo)

"""12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58"""

print(20*'-')
altura = float(input("Digite a altura da pessoa (m): "))
peso_ideal = (72.7*altura)-58
print("O peso ideal da pessoa é", round(peso_ideal,2),"Kg")

"""13.Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
- ``` Para homens: (72.7*h) - 58```
- ```Para mulheres: (62.1*h) - 44.7 ```
"""

altura_2 = float(input("Digite a altura da pessoa (m): "))
peso_ideal_homem = (72.7*altura_2)-58
peso_ideal_mulher = (62.1*altura_2)-44.7
print("O peso ideal da pessoa é", round(peso_ideal_homem,2),"Kg. Caso ela seja homem,\ne", round(peso_ideal_mulher,2),"Kg, se for mulher")

"""14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas"""

peso_peixe = int(input("Quantos Kg de peixe foi pescado? "))
if peso_peixe>50:
  peso_a_mais = peso_peixe - 50
  multa = peso_a_mais * 4
  print("O valor de multa será de R$", round(multa,2))
else:
  print("Não pagará multa")

"""15.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
- _salário bruto._
- _quanto pagou ao INSS._
- _quanto pagou ao sindicato._
- _o salário líquido._

Calcule os descontos e o salário líquido, conforme a tabela abaixo:

 Salário Bruto   | R$ (reais)
---------        | ------:
- IR (11%)       |
- INSS (8%)      |  
- Sindicato (5%) |  
= Salário Liquido|

Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

valor_hora = float(input("Quanto você ganha por hora trabalhada? "))
hrs_mes = int(input("Quantas hrs trabalhadas no mês? "))
salario_bruto= valor_hora*hrs_mes
impostoRD = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05
salario_liquido = salario_bruto-impostoRD-inss-sindicato

print("Salário bruto de R$", round(salario_bruto,2),"""\n
- imposto de renda de R$""", round(impostoRD,2),"\n- INSS de R$", round(inss,2),"""\n- Sindicato de R$"""
, round(sindicato,2),"\n= Salário liquído de R$", round(salario_liquido, 2))

"""16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total."""

area_pintada = float(input("Quantos metros quadrados a ser pintado? "))
litro = area_pintada/3
lata = litro/18
preco_tinta = 80*lata

print("Você vai precisar de", round(lata,2), "latas(s) de tinta. O preço total é de R$", round(preco_tinta,2))

"""17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

area_pintada2 = float(input("Quantos metros quadrados a ser pintado? "))
litro2 = area_pintada2/6
lata2 = litro2/18
preco_tinta2 = 80*lata2
galao = litro2/3.6
preco_galao = 25*galao

lata3 = ((area_pintada2*1.1)/6)/18
galao2 = lata3/3.6
preco_total = (lata3*80) + (galao2*25)


print("-- Comprando apenas latas de 18L -- \nVocê vai precisar de", round(lata2,2), "latas(s) de tinta. O preço total é de R$", round(preco_tinta2,2))

print('-- Comprando apenas galões de 3,6L -- \nVocê vai precisar de', round(galao,2), 'galão(ões) de tinta. O preço total é de R$', round(preco_galao,2))

print('-- Comprando latas e galões de 18L e 3,6L, respectivamente -- \nVocê vai precisar de', round(lata3,2),'latas(s), e',round(galao2,2), 'galão(ões) de tintas. O preço total é de R$', round(preco_total,2))

"""18.Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

tam_mb = int(input("Insira o tamanho do arquivo (em MB)"))
veloc_mbps = int(input("Insira a velocidade do link de internet (em Mbps)"))

tempo = tam_mb/(veloc_mbps/8) #resultado em segundo

tempo_min = tempo/60


print('\nO dowload será feio em', tempo_min,'minutos')

#Fim do programa
