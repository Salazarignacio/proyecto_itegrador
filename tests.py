
def decimal_sistema(num, base):
    num = int(num)
    num_convertido=""
    while num>0:
        ult_digito=num%base
        num_convertido=str(ult_digito)+num_convertido
        num=num//base
    return  num_convertido

def valor_hexadecimal(c):
    """
    Devuelve el valor numérico de un dígito hexadecimal (0–9, A–F).
    Lanza ValueError si el caracter no es válido.
    """
    c = c.upper()  # Para aceptar tanto 'a' como 'A'
    if '0' <= c <= '9':
        return int(c)
    elif c == 'A':
        return 10
    elif c == 'B':
        return 11
    elif c == 'C':
        return 12
    elif c == 'D':
        return 13
    elif c == 'E':
        return 14
    elif c == 'F':
        return 15
    else:
        raise ValueError(f"'{c}' no es un dígito hexadecimal válido")

def hexadecimal_decimal(hex_str):
    """
    Convierte una cadena hexadecimal (por ejemplo "1A3F") a su valor decimal.
    Recorre la cadena de derecha a izquierda, sumando cada dígito * 16^posición.
    """
    hex_str = hex_str.strip()        # Quitamos posibles espacios al inicio o al final
    resultado = 0
    multiplicador = 1                # 16^0 al inicio

    # Recorremos desde el último carácter hasta el primero
    for c in reversed(hex_str):
        valor = valor_hexadecimal(c)
        resultado += valor * multiplicador
        multiplicador *= 16
    
    return resultado

""" Binario """
def hexadecimal_binario(num):
    decimal = hexadecimal_decimal(num)
    binario = decimal_sistema(decimal, 2)
    
    return binario

""" Decimal """
def hexadecimal_octal(num):
    decimal = hexadecimal_decimal(num)
    octal = decimal_sistema(decimal, 8)
    
    return octal


print(hexadecimal_binario("FFF"))
print(hexadecimal_binario("800"))
print(hexadecimal_binario("1F"))
