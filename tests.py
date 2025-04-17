def binario_decimal(num):
    contador = 1
    decimal = 0
    while num >=1:
        cifra = num / 10
        cifra = round(cifra % 1 * 10)
        if cifra == 1:
            decimal += contador
        num = int(num / 10)
        contador *= 2
    return decimal

def decimal_sistema(num, num2):
    sistema=""
    numero=num
    while num>0:
        ult_digito=num%num2
        sistema=str(ult_digito)+sistema
        num=num//num2
    print(f"{numero} en sistema seria {sistema}")

decimal_sistema(12,8)

def octal_binario(num):
    num_bin = bin(int(str(num),8))[2:]# el comando [2:] par eliminar el prefijo que aparece al convertir a hexadecimal.
    print(f"El número {num} convertido a binario es: {num_bin}")

def binario_octal(num):
    decimal = binario_decimal(num)
    octal_binario(decimal)

octal_binario(287)