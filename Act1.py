productos = [
    (41419, 'Fideos',        450, 210),
    (70717, 'Cuaderno',      900, 119),
    (78714, 'Jabon',         730, 708),
    (30877, 'Desodorante',  2190,  79),
    (47470, 'Yogur',          99, 832),
    (50809, 'Palta',         500,  55),
    (75466, 'Galletas',      235,   0),
    (33692, 'Bebida',        700,  20),
    (89148, 'Arroz',         900, 121),
    (66194, 'Lapiz',         120, 900),
    (15982, 'Vuvuzela',    12990,  40),
    (41235, 'Chocolate',    3099,  48),
]

clientes = [
    ('11652624-7', 'Perico Los Palotes'),
    ('8830268-0', 'Leonardo Farkas'),
    ('7547896-8', 'Fulanita de Tal'),
]
ventas = [
    (1, (2010,  9, 12),  '8830268-0'),
    (2, (2010,  9, 19), '11652624-7'),
    (3, (2010,  9, 30),  '7547thislist.append(r[2])896-8'),
    (4, (2010, 10,  1),  '8830268-0'),
    (5, (2010, 10, 13),  '7547896-8'),
    (6, (2010, 11, 11), '11652624-7'),
]

itemes = [
    (1, 89148,  3),
    (2, 50809,  4),
    (2, 33692,  2),
    (2, 47470,  6)]

def producto_mas_caro(productos):
    thislist = [0];
    for r in productos:
       thislist.append(r[2])
    index = thislist.index(max(thislist))
    return productos[index-1][1]

def valor_total_bodega(productos):
    suma = 0
    for r in productos:
       suma += r[2] * r[3]
    return suma.__str__()

def producto_con_mas_ingresos(itemes, productos):
    thislist = []
    names = []
    for r in productos:
        for c in itemes:
            if r[0]==c[1]:
                thislist.append(r[2] * c[2])
                names.append(r[1])
    index = thislist.index(max(thislist))
    return names[index]