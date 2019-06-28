from Act1 import *
from Act2 import *
from Act3 import *
from Act4 import *
from Act5 import *
from Act7 import *
from Act8 import *
from Act9 import *
from Act10 import *
from Act11 import *

print ("Actividad 1")
print ("El producto mas caro es: " + producto_mas_caro(productos))
print ("El valor total en bodega es : " + valor_total_bodega(productos))
print ("Producto con mas ingresos es : " + producto_con_mas_ingresos(itemes, productos)+"\n")

print ("Actividad 2")
print ("La desviacion estandar es: " + desviacion_estandar([1.3, 1.3, 1.3])+"\n")

print ("Actividad 3")
print ("El grado del polinomio es: " + grado(r))
print ("El grado del polinomio es: " + evaluar(p, 3))
print ("La suma de los polinomios es : "+ sumar_polinomios(r, p))
print ("La derivada del polinomio es : "+ derivar_polinomio(r)+"\n")

print ("Actividad 4")
print ("Ordenar por palabra mas corta:  " + s.__str__())
print ("Ordenar por palabra mas larga:  " + list(reversed(s)).__str__()+"\n")

print ("Actividad 5")
print("El numero de letras es el siguiente: " + contar_letras('El elefante avanza hacia Asia')+"\n")

print ("Actividad 7")
print("Son anagramas?: " + son_anagramas('torpes', 'postre')+"\n")

print ("Actividad 8")
print("Es vocal?: " + es_vocal('A'))
print("Es consonante?: " + es_consonante('A')+"\n")

print ("Actividad 9")
aprobo()
print ("\n")

print ("Actividad 10")
paso()
print ("\n")

print ("Actividad 11")
cuenta_caracteres()
print ("\n")
