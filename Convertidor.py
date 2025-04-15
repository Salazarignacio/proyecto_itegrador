""" Convertidor de sistemas numericos """

""" Funcion que convierte un numero binario dado por el usuario a sistema decimal """
def binario_decimal(num):
    print("Esta funcion convierte de BINARIO a DECIMAL")


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

def convertir_numero(original, conversion,num):
    """ Convertimos el texto a minusculas para validar entradas con mayusculas"""
    original = original.lower() 
    conversion = conversion.lower()
    if original == "binario" and conversion == "decimal":
        binario_decimal(num)
    elif original == "decimal" and conversion == "binario":
        decimal_binario(num)  
    elif original == "binario" and conversion == "octal":
        binario_octal(num)
    elif original == "binario" and conversion == "hexagesimal":
        binario_hexagesimal(num)
    print(f"El numero es {num}")

def comenzar():
    print("Este programa convierte el numero que se ingrese al sistema numerico deseado, por favor ingrese el numero que desea convertir: ")
    num = int(input())
    original = input(f"Se ingreso el numero {num}, por favor indique en que sistema numerico esta expresado(Decimal,Binario, Octal o Hexagesimal): ").lower()
    convertir = input(f"Por favor ingrese el sistema numerico al que desea convertir su numero: (Decimal,Binario, Octal o Hexagesimal) ").lower()
    """ Se le puede agregar una funcion que valide las entradas del usuario """
    convertir_numero(original, convertir, num)



comenzar()






