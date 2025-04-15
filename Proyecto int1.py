def decimal_a_binario(decimal):    
    binario=""
    while decimal>0:
        ult_digito=decimal%2
        binario=str(ult_digito)+binario
        decimal=decimal//2
    return binario

decimal=int(input("Ingrese numero decimal: "))
binario=decimal_a_binario(decimal)

print(f"{decimal} en binario seria {binario}")
