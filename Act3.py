p = [1, 2, 1]
q = [4, -17]
r = [-1, 0, 0, -5, 0, 3]
s = [0] * 40 + [5] + [0] * 39 + [2]

def grado(poly):
    grado = len(poly)-1
    return grado.__str__()

def evaluar(p,x):
    sum = p[0]
    for i in range(1, len(p)):
        sum += pow(p[i]*x, i)
    return sum.__str__()

def sumar_polinomios(a,b):
    c = []
    if len(a) > len(b):
        for i in range(0, len(a)):
            if i < len(b):
                c.append(a[i]+b[i])
            if i >= len(b):
                c.append(a[i])
    else:
        print("El primer array debe ser mayor que el segundo")
    return c.__str__()

def derivar_polinomio(r):
    c = []
    for i in range(1, len(r)):
        c.append((r[i])*i)
    return c.__str__()