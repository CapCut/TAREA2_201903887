from Nodo import Nodo

class ListaC_Doble_Enlazada:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacio(self):
        if self.primero == None:
            return True
        else:
            return False
            
    def Agregar_Inicio(self, dato):
        if self.vacio():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.Unir_Nodos()

    def Agregar_Final(self, dato):
        if self.vacio():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.Unir_Nodos()

    def Unir_Nodos(self):
        self.primero.anterior = self.ultimo
        self.ultimo.siguiente = self.primero

    def Recorrer_Inicio_hasta_Fin(self):
        print("Elementos de la lista: ")
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente

            if aux == self.primero:
                break

    def Recorrer_Fin_hasta_Inicio(self):
        print("Elementos de la lista: ")
        aux = self.ultimo
        while aux:
            print(aux.dato)
            aux = aux.anterior

            if aux == self.ultimo:
                break

    def Buscar_Nodos(self, dato):
        
        aux = self.primero

        while (aux != None):
            if(aux.dato == dato):
                print("Anterior: ", str(aux.anterior.dato))
                print("Actual: ", str(aux.dato))
                print("Siguiente: ", str(aux.siguiente.dato))
            
            if(aux.siguiente == self.primero):
                return
            aux = aux.siguiente