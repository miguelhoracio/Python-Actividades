import requests

def paso():
    f = open("puntajes.txt", "w+")
    r = requests.get('http://progra.usm.cl/apunte/_static/puntajes.txt')
    for i in r.text:
        f.write(str(i))
    f.close()
    file1 = open("puntajes.txt", "r")
    aprobado = 0
    for i in range(0,999):
        if int(file1.readline()) > 764:
            aprobado += 1
    print ("Aprobados: "+ str(aprobado))
    print ("Reprobados: " + str(1000-aprobado))
