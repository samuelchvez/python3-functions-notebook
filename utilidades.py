def factorial(num):
    if num < 0:
        return -1
    else:
        resultado = 1

        for i in range(num):
            resultado *= (i + 1)

    return resultado

