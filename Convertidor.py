""" Convertidor de sistemas numericos """

""" Funcion que convierte un numero binario dado por el usuario a sistema decimal """
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


""" Esta funcion convierte un numero decimal dado por el usuario a sistema binario """    
def decimal_binario(num):
    print("Esta funcion convierte de DECIMAL a BINARIO")
    binario=""
    numero=num
    while num>0:
        ult_digito=num%2
        binario=str(ult_digito)+binario
        num=num//2
    print(f"{numero} en binario seria {binario}")    


""" Esta funcion convierte un numero decimal dado por el usuario a sistema octal """    
def binario_octal(num):
    print("Esta funcion convierte de BINARIO a OCTAL")

""" Esta funcion convierte un numero decimal dado por el usuario a sistema octal """    
def binario_hexagesimal(num):
    print("Esta funcion convierte de BINARIO a OCTAL")

""" Esta funcion es la que le pide los datos al usuario y luego decide a que funcion llamar segun los datos ingresados """

# convertir de octal a hexadecimal 
def octal_hexadecimal(num):
    num_hexa = hex(int(str(num),8))[2:].upper() # el comando [2:] par eliminar el prefijo que aparece al convertir a hexadecimal.
    print(f"el  número hexadecimal es {num_hexa}")

#convertir octal a binario
def octal_binario(num):
    num_bin = bin(int(str(num),8))[2:]# el comando [2:] par eliminar el prefijo que aparece al convertir a hexadecimal.
    print(f"El número {num} convertido a binario es: {num_bin}")

def num_to_decimal(num, type):
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


def convertir_numero(original, conversion,num):
    """ Convertimos el texto a minusculas para validar entradas con mayusculas"""
    original = original.lower() 
    conversion = conversion.lower()
    if original == "binario" and conversion == "decimal":
        binario_decimal(num)
    elif original == "decimal" and conversion == "binario":
        decimal_binario(num)  
    elif original == "octal" and conversion == "hexadecimal":
        octal_hexadecimal(num)
    elif original == "octal" and conversion == "binario":
        octal_binario(num)
    elif original == "binario" and conversion == "octal":
        binario_octal(num)
    elif original == "binario" and conversion == "hexagesimal":
        binario_hexagesimal(num)
    elif original == "binario" and conversion == "decimal":
        num_to_decimal(num,original)
    print(f"El numero es {num}")

def comenzar():
    print("Este programa convierte el numero que se ingrese al sistema numerico deseado, por favor ingrese el numero que desea convertir: ")
    num = int(input())
    original = input(f"Se ingreso el numero {num}, por favor indique en que sistema numerico esta expresado(Decimal,Binario, Octal o Hexagesimal): ").lower()
    convertir = input(f"Por favor ingrese el sistema numerico al que desea convertir su numero: (Decimal,Binario, Octal o Hexagesimal) ").lower()
    """ Se le puede agregar una funcion que valide las entradas del usuario """
    convertir_numero(original, convertir, num)



comenzar()






