from ArbolBinarioBST.Arbol import Arbol


arbol = Arbol()

arbol.insertar(100)
arbol.insertar(90)

arbol.insertar(120)

print("In Orden")
arbol.inOrden()

print("Pre Orden")
arbol.preOrden()

arbol.isVacio()