num = int(input('Digite um valor : '))
num1 = int(input('Digite outro valor : '))
print('Agora Escolha uma opção ')

valor = 0
opc = 0
while opc != 5:
    print('\n \033[30m[1]somar \n \033[31m[2]multiplicar \n \033[32m[3]maior \n \033[33m[4]novos números \n \033[34m[5]sair do programa \033[m \n')
    opc = int(input('Qual sua opção? '))
    if opc == 1:
        valor = num + num1
        print(num, '+', num1, "=", valor)
    elif opc == 2:
        valor = num * num1
        print(num, 'X', num1, "=", valor)
    elif opc == 3:
        if num > num1:
            print('O maior número e {}'.format(num))
        else:
            print('O maior número e {}'.format(num1))
    elif opc == 4:
        num = int(input('Digite um valor : '))
        num1 = int(input('Digite outro valor : '))

print ('Programa encerrado!!!')