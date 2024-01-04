"""Exercício 6.1 Modifique o programa da listagem 6.6 para ler 7 notas em vez de 5."""

notas = [0,0,0,0,0,0,0]
soma = 0
x = 0
while x < 5:
  notas[x] = float(input('Nota %d: ' %x))
  soma += notas[x]
  x += 1
x = 0
while x < 5:
  print('Nota %d: %6.2f' % (x,notas[x]))
  x += 1
print('Média: %5.2f' % (soma/x))

"""Exercício 6.2 Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras."""

lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 4, 8]
lista3 = l1+l2
print(lista3)

""" Exercício 6.3 Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos."""

lista_new = []
lista3 = lista1+lista2
for l in lista3:
  lista_new.append(l)
list(set(lista_new))

"""Exercício 6.4 O que acontece quando não verificamos se a lista está vazia antes de chamarmos o método pop?"""

"""Se não verificarmos que a lista está vazia antes de chamarmos o pop(),
o programa para com uma mensagem de erro, informando que tentamos retirar um elemento de uma lista vazia."""
# IndexError: pop from empty list

"""Exercício 6.5 Altere o programa da listagem 6.21 de forma a poder trabalhar com vários comandos digitados de uma só vez. Atualmente, apenas um comando pode ser inserido por vez. Altere-o de forma a considerar operação como uma string.
Exemplo: FFFAAAS significaria três chegadas de novos clientes, três atendimentos e, finalmente, a saída do programa."""

último = 10
ultimo is True
fila = list(range(1,último+1))
while True:
  print("\nExistem %d clientes na fila" % len(fila))
  print("Fila atual:", fila)
  print("Digite F para adicionar um cliente ao fim da fila,")
  print("ou A para realizar o atendimento. S para sair.")
  operacao = input("Operacao (F, A ou S):")
  for i, teste in enumerate(operacao):
    if operacao[i] == "A":
      if(len(fila))>0:
        atendido = fila.pop(0)
        print("Cliente %d atendido" % atendido)
      else:
        print("Fila vazia! Ninguém para atender.")
    elif operacao[i] == "F":
      último+=1 # Incrementa o ticket do novo cliente
      fila.append(último)
    elif operacao[i] == "S":
      break
    else:
      print("Operacao inválida! Digite apenas F, A ou S!")

"""Exercício 6.6 Modifique o programa para trabalhar com duas filas. Para facilitar seu trabalho, considere o comando A para atendimento da fila 1; e B, para atendimento da fila 2. O mesmo para a chegada de clientes: F para fila 1; e G, para fila 2"""

"""Exercício 6.7 Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta.
Exemplo:
(())
()()(()())
OK
())
Erro"""

"""Exercício 6.8 Modifique o primeiro exemplo (Listagem 6.23) de forma a realizar a mesma tarefa, mas sem utilizar a variável achou. Dica: observe a condição de saída do while."""

"""Exercício 6.9 Modifique o exemplo para pesquisar dois valores. Em vez de apenas p, leia outro valor v que também será procurado. Na impressão, indique qual dos dois valores foi achado primeiro."""

"""Exercício 6.10 Modifique o programa do exercício 6.9 de forma a pesquisar p e v em toda a lista e informando o usuário a posição onde p e a posição onde v foram encontrados."""

"""Exercício 6.11 Modifique o programa da listagem 6.15 usando for. Explique por que nem todos os while podem ser transformados em for."""

"""Exercício 6.12 Altere o programa da listagem 6.33 de forma a imprimir o menor elemento da lista."""

"""Exercício 6.13 Alista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [-10, -8, 0,1, 2, 5, -2, -4]. Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média."""

"""Exercício 6.14 O que acontece quando a lista já está ordenada? Rastreie o programa da listagem 6.44, mas com a lista L=[1,2,3,4,5]."""

"""Exercício 6.15 O que acontece quando dois valores são iguais? Rastreie o programa da listagem 6.44, mas com a lista L=[3,3,1,5,4]."""

"""Exercício 6.16 Modifique o programa da listagem 6.44 para ordenar a lista em ordem decrescente. L=[1,2,3,4,5] deve ser ordenada como L=[5,4,3,2,1]."""

"""Exercício 6.17 Altere o programa da listagem 6.53 de forma a solicitar ao usuário o produto e a quantidade vendida. Verifique se o nome do produto digitado existe no dicionário, e só então efetue a baixa em estoque."""

"""Exercício 6.18 Escreva um programa que gere um dicionário, onde cada chave seja um caractere, e seu valor seja o número desse caractere encontrado em uma frase lida.
Exemplo: O rato -> { "O": 1, "r":1, "a":1, "":1, "":1}"""
