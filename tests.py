def letra_numero(l):
    salida = ""
    for i in range(len(l)):
        if l[i] == "A":
            salida += '10'
        elif l[i] == 'B':
            salida += '11'
        elif l[i] == 'C':
            salida += '12'
        elif l[i] == 'D':
            salida += '13'
        elif l[i] == 'E':
            salida += '14'
        elif l[i] == 'F':
            salida += '15'
        else:
            salida += l[i]
    return salida


def hexadecimal_decimal(num):
    numero = int(letra_numero(num))
    num = numero
    print(num)
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
    return convertido

hexadecimal_decimal("101112")