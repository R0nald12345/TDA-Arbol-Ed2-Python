from ArbolBinarioBST.Nodo import Nodo

class Arbol:
    __raiz__ = None
    __n__ = 0

    def __init__(self):
        self.__raiz__ = None
        self.__n__ = 0;

    def insertar(self, x):
        self.__raiz__ = self.__insertarMask(self.__raiz__, x)

    def __insertarMask(self, nodo, x):
        if nodo is None:
            return Nodo(x)
        else:
            if x < nodo.getData():
                nodo.__hijoIzquierdo__ = self.__insertarMask(nodo.getHijoIzquierdo(), x)
            else:
                nodo.__hijoDerecho__ = self.__insertarMask(nodo.getHijoDerecho(), x)
        return nodo


    def inOrden(self):
        if self.__raiz__ is None:
            print("El arbol esta Vacio")
        else:
            self.__inOrdenMask(self.__raiz__)
        print("---------------------------------------")

    def __inOrdenMask(self, nodo):
        if nodo is not None:
            self.__inOrdenMask(nodo.getHijoIzquierdo()) # Izquierdo
            print(nodo.getData())       #Padre
            self.__inOrdenMask(nodo.getHijoDerecho()) #Derecho

    def preOrden(self):
        if self.__raiz__ is None:
            print("El arbol esta Vacio")
        else:
            self.__preOrdenMask(self.__raiz__)


    def __preOrdenMask(self, nodo):  #Padre, Izquierdo, Derecho
        if nodo is not None:
            print(nodo.getData())  # Padre
            self.__inOrdenMask(nodo.getHijoIzquierdo())  # Izquierdo
            self.__inOrdenMask(nodo.getHijoDerecho())  # Derecho


    #Post ORden = Izuiqerdo Derecho, Padre

    #Verificar Arbol Vacio
    def isVacio(self):
        if self.__raiz__ is None:
            print("El arbol esta vacio")
        else:
            print("El arbol no esta vacio")


    def isHoja(self, nodo):
        if(nodo.getHijoIzquierdo()is None  and nodo.getHijoDerecho() is None):
            print("El nodo es Hoja")
        else:
            print("El nodo no es hoja")

