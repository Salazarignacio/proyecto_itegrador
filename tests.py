def hexadecimal_decimal(num):
    numero = num
    multiplicador = 1
    convertido = 0
    exp = int(len(str(num)))
    exp2 = int(len(str(num))) - 1

    for i in range(exp):
        while numero >= 9:
            numero = int(numero / 10)
            multiplicador *= 10
        convertido += numero * 16 ** exp2
        exp2 -=1
        numero = num - (multiplicador * numero)
        num = numero
        multiplicador = 1
    print(convertido)
    

hexadecimal_decimal(788)