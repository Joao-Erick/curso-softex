while True:
    print(' 1.Soma \n 2.Subtração \n 3.Multiplicação \n 4.Divisão \n 0.Sair')
    op = int(input('Escolha uma das opções acima: '))
    
    if (op == 0):
        break

    n1 = int(input('Digita um número: '))
    n2 = int(input('Digite outro número: '))

    if(op == 1):
        print('Soma: ', n1 + n2)
    elif(op == 2):
        print('Subtração: ', n1 - n2)
    elif(op == 3):
        print('Multiplicação: ', n1 * n2)
    elif(op == 4):
        print('Divisão: ', n1 / n2)
       
