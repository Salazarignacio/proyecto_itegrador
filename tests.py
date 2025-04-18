def octal_decimal(num):
    """
    Convierte una cadena con dígitos octales (0–7) a su valor decimal.
    Ejemplo: "17" → 1*8 + 7 = 15
    """
    octal_str = num.strip()     # Quitamos espacios al inicio y al final
    resultado = 0
    multiplicador = 1           # 8^0 al empezar

    # Recorremos de derecha a izquierda: el dígito de menor peso primero
    for c in reversed(octal_str):
        # Validamos que c sea entre '0' y '7'
        if '0' <= c <= '7':
            valor = int(c)
        else:
            raise ValueError(f"'{c}' no es un dígito octal válido")
        resultado += valor * multiplicador
        multiplicador *= 8

    print(f"el número {octal_str} convertido a decimal es: {resultado}")
    return resultado


octal_decimal("12")