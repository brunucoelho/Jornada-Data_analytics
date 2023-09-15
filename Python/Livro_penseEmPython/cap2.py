##Exercicio 2.1
    #1. Aparece o erro de sintaxe. SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
    #2. As duas variáveis, x e y, recebem o valor de 1.
    #3. Nada, o interpretador ocorre normal.
    #4. Ocorre erro. SyntaxError: incomplete input

##Exercício 2.2
#1. O volume de uma esfera com raio r é . Qual é o volume de uma esfera com raio 5?

import math
raio = 5
volume = (4/3) * math.pi * raio**3
print('O volume da esfera de raio {} é de {:.2f}'.format(raio, volume))

#2. Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional Qual é o custo total de atacado para 60 cópias?

copias = 60
livros = (24.95*0.6)
transporte = (3 + copias*0.75)
custo_total = (copias*livros + transporte)
print('O custo total de atacado foi de R${:.2f}'.format(custo_total))

#3. Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro),então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?

certo_passo = 2*(8*60+15)
passo_mrapido = 3*(7*60+12)
total_passos = certo_passo+passo_mrapido

minutos = total_passos//60
segundo = total_passos%60

hrdesaida = 6*60+52
chegada = (hrdesaida+minutos)//60 #desconsideramos os segundos
print('A hora de chegada foi as {}h e {}s'.format(chegada,segundo))