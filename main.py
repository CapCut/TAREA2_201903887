from ListaC import ListaC_Doble_Enlazada

nuevo = [1, 2, 3, 4, 5, 6, 7]

lista = ListaC_Doble_Enlazada()

lista.Agregar_Final(nuevo[0])
lista.Agregar_Final(nuevo[1])
lista.Agregar_Final(nuevo[2])
lista.Agregar_Final(nuevo[3])
lista.Agregar_Final(nuevo[4])
lista.Agregar_Final(nuevo[5])
lista.Agregar_Final(nuevo[6])

"""lista.Recorrer_Fin_hasta_Inicio()"""
print("=" * 6)
lista.Recorrer_Inicio_hasta_Fin()
print("=" * 6)
x = int(input("Seleccione un número （￣︶￣）↗　: "))

if (x == None):
    pass
else:
    print("Anterior: ", str(x-1))
    print("Acutal: ", x)
    print("Siguinete: ", str(x+1))