def calculadoraImc(n1, n2, operador):
    if (operador == '+'):
        imc = n1 + n2
    elif(operador == '-'):
        imc = n1 - n2
    elif(operador == '*'):
        imc = n1 * n2
    elif(operador == '/'):
        imc = n1 / n2
    else : 
        return "Resultado = 0" 
    
    return imc

    print(calcudoraImc(4 , 3 , '+'))

