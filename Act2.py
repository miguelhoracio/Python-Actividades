import math

def desviacion_estandar(lista):
    sum = 0.0
    for i in range(0, len(lista)):
        sum += lista[i]
    prom = sum/len(lista)
    sum = 0.0
    for i in range(0, len(lista)):
        sum += pow(lista[i]-prom, 2)
    tot = math.sqrt(sum/len(lista))
    return tot.__str__()