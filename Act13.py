import requests

def ordenar():
    f1 = open("a.txt", "w+")
    r = requests.get('http://progra.usm.cl/apunte/_static/a.txt')
    for i in r.text:
        f1.write(str(i))
    f1.close()
    f2 = open("b.txt", "w+")
    r = requests.get('http://progra.usm.cl/apunte/_static/b.txt')
    for i in r.text:
        f2.write(str(i))
    f2.close()
    a = open("a.txt", "r")
    b = open("b.txt", "r")
    list = []
    while True:
        char = a.readline()
        list.append(char.rstrip('\n'))
        if not char:
            break
    while True:
        char2 = b.readline()
        list.append(char2.rstrip('\n'))
        if not char2:
            break
    f = open("d.txt", "w+")
    list.pop()
    list.remove('')
    list = map(int, list)
    list = sorted(list)
    for i in list:
        f.write(str(i)+"\n")
    f.close()
    print("El documento se ha creado correctamente")
