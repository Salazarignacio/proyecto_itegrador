def decimal_sistema(num, base):
    num_convertido=""
    numero=num
    while num>0:
        ult_digito=num%base
        num_convertido=str(ult_digito)+num_convertido
        num=num//base
    
    sistema = ""
    if base == 8:
        sistema = "octal"
    elif base == 2:
        sistema = "decimal"
    print(f"{numero} en sistema {sistema} seria {num_convertido}")   

def numero_letra(n):
    n = str(n)
    if n == "10":
        n = 'A'
    elif n == '11':
        n = 'B'
    elif n == '12':
        n = 'C'
    elif n == '13':
        n = 'D'
    elif n == '14':
        n = 'E'
    elif n == '15':
        n = 'G'
    return n



def decimal_hexa(num):
    numero_convertido = ""
    numero = num
    a_letra = ""
    while numero >= 16:
        a_letra = numero_letra(numero % 16)
        numero_convertido = a_letra + numero_convertido
        numero = numero // 16
    a_letra = numero_letra(numero % 16)
    numero_convertido = a_letra + numero_convertido
    print(numero_convertido)


decimal_hexa(6699)
