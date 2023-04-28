#4.3 - Exercícios
#A seguir, uma série de exercícios usando TurtleWorld. Eles servem para divertir, mas também têm outro objetivo. Enquanto trabalha neles, pense que objetivo pode ser. As seções seguintes têm as soluções para os exercícios, mas não olhe até que tenha terminado (ou, pelo menos, tentado).
#1. Escreva uma função chamada square que receba um parâmetro chamado t, que é um turtle. Ela deve usar o turtle para desenhar um quadrado. Escreva uma chamada de função que passe bob como um argumento para o square e então execute o programa novamente.

import turtle

squirrel = turtle.Turtle()
squirrel.shape('turtle')
for i in range(4):
    squirrel.forward(50)
    squirrel.right(90)
squirrel.left(90)



#2. Acrescente outro parâmetro, chamado length, ao square. Altere o corpo para que o comprimento dos lados seja length e então altere a chamada da função para fornecer um segundo argumento. Execute o programa novamente. Teste o seu programa com uma variedade de valores para length.

def square(t, length):
    import turtle

    t = turtle.Turtle()
    t.shape()
    for i in range(4):
        t.fd(length)
        t.rt(90)
    t.lt(90)

#3. Faça uma cópia do square e mude o nome para polygon. Acrescente outro parâmetro chamado n e altere o corpo para que desenhe um polígono regular de n lados. Dica: os ângulos exteriores de um polígono regular de n lados são 360/n graus.

def polygon(t, length, n):
    import turtle

    t = turtle.Turtle()
    t.shape('turtle')
    for i in range(n):
        t.fd(length)
        t.rt(360/n)
    t.lt(length)


#4. Escreva uma função chamada circle que use o turtle, t e um raio r como parâmetros e desenhe um círculo aproximado ao chamar polygon com um comprimento e número de lados adequados. Teste a sua função com uma série de valores de r.Dica: descubra a circunferência do círculo e certifique-se de que length * n = circumference.

def circle(t,r):
    if r > 10:
        r = 10
        polygon(t, r*10, 15) #Aqui se chama a função polygon, caso for executar somente esse exercicio, deve colocar as duas funções (polygon e circle) no scrip.
    else:
        polygon(t, r*10, 15)
    
#5. Faça uma versão mais geral do circle chamada arc, que receba um parâmetro adicional de angle, para determinar qual fração do círculo deve ser desenhada. angle está em unidades de graus, então quando angle=360, o arc deve desenhar um círculo completo.
