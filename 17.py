num1 = int(input('Insira o primeiro numero'))
num2 = int(input('Insira o segundo numero'))
num3 = int(input('Insira o terceiro numero'))

if num1>num2 and num1>num3:
    print('O maior e ',num1)
elif num2>num1 and num2>num3:
    print('O maior e',num2)
elif num3>num1 and num3>num2:
    print('O maior e',num3 )
else:
    print('Os maiores numeros se repetem')

if num1<num2 and num1<num3:
    print('O menor e ',num1)
elif num2<num1 and num2<num3:
    print('O menor e',num2)
elif num3<num1 and num3<num2:
    print('O menor e',num3 )
else:
    print('Os menores numeros se repetem')