import requests

def cuenta_caracteres():
    f1 = open("texto.txt", "w+")
    r = requests.get('http://progra.usm.cl/apunte/_static/texto.txt')
    for i in r.text:
        f1.write(str(i))
    f1.close()
    f = open("texto.txt", "r")
    list = []
    may = 0
    min = 0
    esp = 0
    por = 0
    while True:
        char = f.read(1)
        list.append(char)
        if not char:
            break
    for i in range(0,len(list)-1):
        if((64 < int(ord(list[i]))) and int((ord(list[i])) < 91)):
            may += 1
        elif ((96 < int(ord(list[i]))) and int((ord(list[i])) < 123)):
            min += 1
        else:
            esp += 1
    por = (min*100)/(min+may)
    print ("Mayusculas: "+ str(may))
    print ("Minusculas: " + str(min))
    print ("Especiales: " + str(esp))
    print ("Porcentaje de minusculas: " + str(por)+"%")