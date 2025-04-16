def binario_decimal(num):
    contador = 1
    decimal = 0
    while num >=1:
        cifra = num / 10
        cifra = cifra % 1 * 10
        cifra = round(cifra)
        if cifra == 1:
            decimal += contador
        num = int(num / 10)
        contador *= 2
    return decimal

binario_decimal(111)