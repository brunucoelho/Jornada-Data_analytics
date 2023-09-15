##Exercicio 1.1
    #1. Aparece o erro de sintaxe. incomplete input
    #2. Erro. name '' is not defined
    #3. Soma da mesma forma
    #4. Erro. SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
    #5. Ocorre erro. SyntaxError: invalid syntax. Perhaps you forgot a comma?

##Exercicio 1.2
    #1. Quantos segundos há em 42 minutos e 42 segundos?

minutos, segundos = 42, 42
total_segundos = (60 *minutos) + (1 * segundos)
print('{} segundos'.format(total_segundos))

    #2. Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.

milha = 1.61
totalMilha = 10/milha
print('Em 10 Km, há {:.2f} milhas'.format(totalMilha))

    #3. Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora?

passomedio = total_segundos/totalMilha
print('O passo médio é de {:.0} minutos e {:.2f} segundos'.format(passomedio//60, passomedio%60))
print('A velocidade média é {} milha/h'.format(totalMilha/total_segundos*60*60))
