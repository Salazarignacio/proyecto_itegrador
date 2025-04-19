# def letra_numero(l):
#     salida = ""
#     for i in range(len(l)):
#         if l[i] == "A":
#             salida += '10'
#         elif l[i] == 'B':
#             salida += '11'
#         elif l[i] == 'C':
#             salida += '12'
#         elif l[i] == 'D':
#             salida += '13'
#         elif l[i] == 'E':
#             salida += '14'
#         elif l[i] == 'F':
#             salida += '15'
#         else:
#             salida += l[i]
#     return salida


# def hexadecimal_decimal(num):
#     numero = int(letra_numero(num))
#     num = numero
#     print(num)
#     multiplicador = 1
#     convertido = 0
#     exp = int(len(str(num)))
#     exp2 = int(len(str(num))) - 1

#     for i in range(exp):
#         while numero >= 9:
#             numero = int(numero / 10)
#             multiplicador *= 10
#         convertido += numero * 16 ** exp2
#         exp2 -=1
#         numero = num - (multiplicador * numero)
#         num = numero
#         multiplicador = 1
#     print(convertido)
#     return convertido

# hexadecimal_decimal("1F")


def binario_octa():
    octal=""
    num=str(1100011)

    #Añadir 0 si el largo de la funcion no es multiplo de 3 para poder dividir el binario en secciones de 3
    while len(num)%3!=0:
        num="0"+num

    grupos = [num[i:i+3] for i in range(0, len(num), 3)]
    for i in grupos:
        if len(i)==3:
            octal=octal+str(binario_decimal(int(i)))
        else:
            while len(i)!=3:
                i="0"+i
                
            octal=octal+str(binario_decimal(int(i)))
    print (octal)



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
                
    

        
    
binario_octa()