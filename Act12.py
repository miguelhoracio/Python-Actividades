def existe_producto(p):
    exist = False
    file1 = open("productos.txt", "r")
    boys = []
    for i in range(0, 4):
        boys.append(file1.readline())
        boys[i] = boys[i].split("/")
        boys[i][2] = boys[i][2].rstrip('\n')
    for i in boys:
        if (int(i[0])==p):
            exist = True
    return str(exist)
