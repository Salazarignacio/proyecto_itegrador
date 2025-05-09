def linea():
    print("-" * 50)  # Imprime una línea de 50 guiones

"""################## DE BINARIO A: ##################"""

def binario_decimal(num):
    num = int(num)
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
    
def binario_octal(num):
    num = int(num)
    decimal = binario_decimal(num)
    octal = decimal_sistema(decimal,8)
    return octal
    
def binario_hexadecimal(num):
    num = int(num)
    decimal = binario_decimal(num)
    hexadecimal = decimal_hexadecimal(decimal)
    return hexadecimal


""" ################## DE DECIMAL A: ##################"""
    
""" Binario y Octal """
def decimal_sistema(num, base):
    num = int(num)
    num_convertido=""
    while num>0:
        ult_digito=num%base
        num_convertido=str(ult_digito)+num_convertido
        num=num//base
    return  num_convertido
    # print(f"{numero} en sistema {sistema} seria {num_convertido} en binario")  

""" Hexadecimal """
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
        n = 'F'
    return n

def decimal_hexadecimal(num):
    num = int(num)
    numero_convertido = ""
    numero = num
    a_letra = ""
    while numero >= 16:
        a_letra = numero_letra(numero % 16)
        numero_convertido = a_letra + numero_convertido
        numero = numero // 16
    a_letra = numero_letra(numero % 16)
    numero_convertido = a_letra + numero_convertido
    return numero_convertido
 

"""################## DE OCTAL A: ##################"""

# convertir de octal a hexadecimal 
def octal_hexadecimal(num):
    num = int(num)
    num_hexa = hex(int(str(num),8))[2:].upper() # el comando [2:] par eliminar el prefijo que aparece al convertir a hexadecimal.
    return num_hexa

#convertir octal a binario
def octal_binario(num):
    num = int(num)
    num_bin = bin(int(str(num),8))[2:]# el comando [2:] par eliminar el prefijo que aparece al convertir a hexadecimal.
    return num_bin

#convertir octal a decimal
def octal_decimal(num):
    """
    Convierte una cadena con dígitos octales (0–7) a su valor decimal.
    Ejemplo: "17" → 1*8 + 7 = 15
    """
    octal_str = num     # Quitamos espacios al inicio y al final
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

"""################## DE HEXADECIMAL A: ##################"""

""" Decimal """

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
    hex_str = hex_str        # Quitamos posibles espacios al inicio o al final
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





"""################## FUNCION PRINCIPAL ##################"""
""" Esta funcion es la que le pide los datos al usuario y luego decide a que funcion llamar segun los datos ingresados """

# def convertir_numero(original, conversion,num):
#     """ DE BINARIO A """ 
#     if original == "binario" :   
#         if conversion == "decimal":            
#             print(f"El número {num} en sistema {original} seria {binario_decimal(num)} en sistema {conversion}")
#         elif conversion == "octal":            
#             print(f"El número {num} en sistema {original} seria {binario_octal(num)} en sistema {conversion}")
#         elif conversion == "hexadecimal":            
#             print(f"El número {num} en sistema {original} seria {binario_hexadecimal(num)} en sistema {conversion}")
            
#     """ DE DECIMAL A """
#     if original == "decimal":
#         if conversion == "binario":            
#             print(f"El número {num} en sistema {original} seria {decimal_sistema(num, 2)} en sistema {conversion}")
#         elif conversion == "octal":            
#             print(f"El número {num} en sistema {original} seria {decimal_sistema(num, 8)} en sistema {conversion}")
#         elif conversion == "hexadecimal":            
#             print(f"El numero {num} en sistema {original} seria {decimal_hexadecimal(num)} en sistema {conversion}")

#     """ DE OCTAL A """
#     if original == "octal":
#         if conversion == "binario":            
#             print(f"El número {num} en sistema {original} seria {octal_binario(num)} en sistema {conversion}")
#         elif conversion == "decimal":            
#             print(f"El número {num} en sistema {original} seria {octal_decimal(num)} en sistema {conversion}")
#         elif conversion == "hexadecimal":            
#             print(f"El número {num} en sistema {original} seria {octal_hexadecimal(num)} en sistema {conversion}")

#     """ DE HEXADECIMAL A """
#     if original == "hexadecimal":
#         if conversion == "decimal":            
#             print(f"El número {num} en sistema {original} seria {hexadecimal_decimal(num)} en sistema {conversion}")
#         elif conversion == "binario":            
#             print(f"El número {num} en sistema {original} seria { hexadecimal_binario(num)} en sistema {conversion}")
#         elif conversion == "octal":            
#             print(f"El número {num} en sistema {original} seria { hexadecimal_octal(num)} en sistema {conversion}")
        


def mensaje(num, original, conversion, resultado):
    print(f"_NUMERO: {num}\n_SISTEMA NUMERICO: {original}\n_CONVERTIR A: {conversion}\n_RESULTADO: {resultado}\nEl número {num} en sistema {original} sería {resultado} en sistema {conversion}")

def convertir_numero(original, conversion, num):
    """ DE BINARIO A """ 
    if original == "binario":   
        if conversion == "decimal":            
            resultado = binario_decimal(num)
        elif conversion == "octal":            
            resultado = binario_octal(num)
        elif conversion == "hexadecimal":            
            resultado = binario_hexadecimal(num)
    
    """ DE DECIMAL A """
    if original == "decimal":
        if conversion == "binario":            
            resultado = decimal_sistema(num, 2)
        elif conversion == "octal":            
            resultado = decimal_sistema(num, 8)
        elif conversion == "hexadecimal":            
            resultado = decimal_hexadecimal(num)

    """ DE OCTAL A """
    if original == "octal":
        if conversion == "binario":            
            resultado = octal_binario(num)
        elif conversion == "decimal":            
            resultado = octal_decimal(num)
        elif conversion == "hexadecimal":            
            resultado = octal_hexadecimal(num)

    """ DE HEXADECIMAL A """
    if original == "hexadecimal":
        if conversion == "decimal":            
            resultado = hexadecimal_decimal(num)
        elif conversion == "binario":            
            resultado = hexadecimal_binario(num)
        elif conversion == "octal":            
            resultado = hexadecimal_octal(num)
    
    # Imprimir el resultado usando la función simplificada
    mensaje(num, original, conversion, resultado)





def validar_numero(num,original,convertir):

    if original=="binario":
        binario="01"
        for i in str(num):
            if i not in binario:
                return False      
        return True
    
    if original == "octal":
        octal=8
        for i in str(num):
            if int(i) >= octal:
                return False      
        return True      
    
    if original == "hexadecimal":
        hexadecimal="0123456789abcdef"
        for i in str(num).lower():
            if i not in hexadecimal:
                return False      
        return True
    
    if original == "decimal":
        decimal="0123456789"
        for i in str(num):
            if i not in decimal:
                return False      
        return True  
    
    """ Esta función chequea que el usuario ingrese un número válido 
        para el sistema numerico ingresado
    """


def validar_sistemas(original, convertir):
    opciones_validas = {"decimal","binario","octal","hexadecimal"}
    return original in opciones_validas and convertir in opciones_validas 

    """ Esta funcion chequea que el sistema numerico pasado por el usuario
        esté dentro de los permitidos. Devuelve true si ambos sistemas están
        dentro de las opciones válidas 
    """

def comenzar():
    print("Este programa convierte el numero que se ingrese al sistema numerico deseado, por favor ingrese el numero que desea convertir: ")
    num = input().strip().replace(" ", "")
    # replace para eliminar los espacios que sin pudo haber ingresado el usuario.
    # strip elimina los espacios del principio y el final

    while not num:
        num = input("Por favor ingrese un numero válido: ").strip().replace(" ", "")

    linea()
    original = input(f"Número ingresado: {num}\nPor favor indique en que sistema numerico esta expresado(Decimal,Binario, Octal o Hexadecimal): ").strip().replace(" ", "").lower()
    linea()
    convertir = input(f"Por favor ingrese el sistema numerico al que desea convertir su numero: (Decimal,Binario, Octal o Hexadecimal) ").strip().replace(" ", "").lower()

    while not validar_numero(num,original,convertir) or not validar_sistemas(original, convertir):
        print("X"*50)
        num=input(f"{num} o {original} o {convertir} no es un dato valido por favor ingrese un dato valido: Ingrese numero nuevamente ").strip().replace(" ", "")
        linea()
        original = input(f"Número ingresado: {num}\nPor favor indique en que sistema numerico esta expresado(Decimal,Binario, Octal o Hexadecimal): ").strip().replace(" ", "").lower()
        linea()
        convertir = input(f"Por favor ingrese el sistema numerico al que desea convertir su numero: (Decimal,Binario, Octal o Hexadecimal) ").strip().replace(" ", "").lower()
    """ Se le puede agregar una funcion que valide las entradas del usuario """
    
    linea()
    convertir_numero(original, convertir, num)
    linea()
    input("Presione Enter para salir del programa...")


comenzar()






