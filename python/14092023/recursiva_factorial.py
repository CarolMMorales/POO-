def factorial_recursivo(numero_factorial):

    if numero_factorial == 0 or numero_factorial == 1:
        return 1
    else:
        numero_factorial * factorial_recursivo(numero_factorial - 1)


def factorial_iterativa(numero_factorial):

    resultado_factorial = 1;
    numero = 1
    while numero <= numero_factorial:
        resultado_factorial = resultado_factorial * numero
    
    return resultado_factorial


print(f"factorial de {4} es {factorial_recursivo(4)} ")