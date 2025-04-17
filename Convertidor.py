"""################## DE BINARIO A: ##################"""

def binario_decimal(num):
    contador = 1
    numero = num
    decimal = 0
    while num >=1:
        cifra = num / 10
        cifra = round(cifra % 1 * 10)
        if cifra == 1:
            decimal += contador
        num = int(num / 10)
        contador *= 2
    print(f"BASE BINARIO: {numero} - BASE DECIMAL: {decimal}")
    return decimal
    
def binario_octal(num):
    decimal = binario_decimal(num)
    octal = decimal_sistema(decimal,8)
    print(octal)
    return octal
    
def binario_hexadecimal(num):
    decimal = binario_decimal(num)
    hexadecimal = decimal_hexadecimal(decimal)
    print(hexadecimal)
    return hexadecimal


""" ################## DE DECIMAL A: ##################"""
    
""" Binario y Octal """
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
        n = 'G'
    return n

def decimal_hexadecimal(num):
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
 

"""################## DE OCTAL A: ##################"""

# convertir de octal a hexadecimal 
def octal_hexadecimal(num):
    num_hexa = hex(int(str(num),8))[2:].upper() # el comando [2:] par eliminar el prefijo que aparece al convertir a hexadecimal.
    print(f"el  número hexadecimal es {num_hexa}")

#convertir octal a binario
def octal_binario(num):
    num_bin = bin(int(str(num),8))[2:]# el comando [2:] par eliminar el prefijo que aparece al convertir a hexadecimal.
    print(f"El número {num} convertido a binario es: {num_bin}")

#convertir octal a decimal
def octal_decimal(num, type):
    base = detectar_base(type)
    decimal = int(num, base)
    print(f"el número {type} convertido a decimal es: {decimal}")


def detectar_base(name):
    name = name.lower()  # para hacerlo insensible a mayúsculas
    if name == "binario":
        return 2
    elif name == "octal":
        return 8
    elif name == "hexadecimal":
        return 16
    else:
        print("El sistema numerico ingresado es incorrecto")  # por si el tipo no es válido

"""################## DE HEXADECIMAL A: ##################"""

""" Decimal """

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

""" Binario """
def hexadecimal_binario(num):
    decimal = hexadecimal_decimal(num)
    decimal_sistema(decimal, 2)
    print("Esta funcion convierte de hexa a binario")

""" Decimal """
def hexadecimal_octal(num):
    decimal = hexadecimal_decimal(num)
    decimal_sistema(decimal, 8)
    print("Esta funcion convierte de hexa a octal")





"""################## FUNCION PRINCIPAL ##################"""
""" Esta funcion es la que le pide los datos al usuario y luego decide a que funcion llamar segun los datos ingresados """

def convertir_numero(original, conversion,num):
    """ Convertimos el texto a minusculas para validar entradas con mayusculas"""
    original = original.lower() 
    conversion = conversion.lower()

    """ DE BINARIO A """
    if original == "binario":
        if conversion == "decimal":
            binario_decimal(num)
        elif conversion == "octal":
            binario_octal(num)
        elif conversion == "hexadecimal":
            binario_hexadecimal(num)
            
    """ DE DECIMAL A """
    if original == "decimal":
        if conversion == "binario":
            decimal_sistema(num, 2)
        elif conversion == "octal":
            decimal_sistema(num, 8)
        elif conversion == "hexadecimal":
            decimal_hexadecimal(num)

    """ DE OCTAL A """
    if original == "octal":
        if conversion == "binario":
            octal_binario(num)
        elif conversion == "decimal":
            octal_decimal(num)
        elif conversion == "hexadecimal":
            octal_hexadecimal(num)

    """ DE HEXADECIMAL A """
    if original == "hexadecimal":
        if conversion == "decimal":
            hexadecimal_decimal(num)
        elif conversion == "binario":
            hexadecimal_binario(num)
        elif conversion == "octal":
            hexadecimal_octal(num)
        

def comenzar():
    print("Este programa convierte el numero que se ingrese al sistema numerico deseado, por favor ingrese el numero que desea convertir: ")
    num = int(input())
    original = input(f"Se ingreso el numero {num}, por favor indique en que sistema numerico esta expresado(Decimal,Binario, Octal o Hexadecimal): ").lower()
    convertir = input(f"Por favor ingrese el sistema numerico al que desea convertir su numero: (Decimal,Binario, Octal o Hexadecimal) ").lower()
    """ Se le puede agregar una funcion que valide las entradas del usuario """
    convertir_numero(original, convertir, num)



comenzar()






