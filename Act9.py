def aprobo():
    file1 = open("calificaciones.txt", "r")
    boys = []

    for i in range(0,4):
        boys.append(file1.readline())
        boys[i] = boys[i].split(":")
        boys[i][6] = boys[i][6].rstrip('\n')
    for j in range(0,4):
        suma = 0.0
        for k in range(1,6):
            suma += float(boys[j][k])
        print ("Promedio de " + boys[j][0] + " es: " + str(suma / 5))