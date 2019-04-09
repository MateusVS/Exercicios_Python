nota1 = int(input('Informe o valor da primeira nota: '))
nota2 = int(input('Informe o valor da segunda nota: '))

media=(nota1+nota2)/2

if media>=7<10:
    print('Aprovado')
elif media<7:
    print('Reprovado')
elif media==10:
    print('Aprovado com Distinção')