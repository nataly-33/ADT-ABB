
class Nodo:

    def __init__(self, valor):
        self._valor = valor
        self._izq = None
        self._der = None

    def getDato(self):
        return self._valor_

    def setDato(self, dato):
        self._valor_ = dato

    def getHijoIzquierdo(self):
        return self._hijoIzquierdo_

    def setHijoIzquierdo(self, hijoIzquierdo):
        self._hijoIzquierdo_ = hijoIzquierdo

    def getHijoDerecho(self):
        return self._hijoDerecho_

    def setHijoDerecho(self, hijoDerecho):
        self._hijoDerecho_ = hijoDerecho

class ABB:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(valor, self.raiz)

    def _insertar(self, valor, nodo):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar(valor, nodo.izquierda)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar(valor, nodo.derecha)

    def isVacio(self):
        return self._raiz_ == None

    def isHoja(self, nodoRaiz):
        return nodoRaiz.getHijoIzquierdo() == None and nodoRaiz.getHijoDerecho() == None

    def _buscar(self, valor, nodo):
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor and nodo.izquierda is not None:
            return self._buscar(valor, nodo.izquierda)
        elif valor > nodo.valor and nodo.derecha is not None:
            return self._buscar(valor, nodo.derecha)
        else:
            return False

    def recorridoInOrden(self):
        self._recorridoInOrdenRecursivo(self.raiz_)
    
    def __recorridoInOrdenRecursivo(self, nodoRaiz):
        if nodoRaiz is not None:
            self.__recorridoInOrdenRecursivo(nodoRaiz.getHijoIzquierdo())
            print(nodoRaiz.getDato(), end=" ")
            self.__recorridoInOrdenRecursivo(nodoRaiz.getHijoDerecho())

    def recorridoPostOrden(self):
        self._recorridoPostOrdenRecursivo(self.raiz_)
    
    def __recorridoPostOrdenRecursivo(self, nodoRaiz):
        if nodoRaiz is not None:
            self.__recorridoPostOrdenRecursivo(nodoRaiz.getHijoIzquierdo())
            self.__recorridoPostOrdenRecursivo(nodoRaiz.getHijoDerecho())
            print(nodoRaiz.getDato(), end=" ")

    def recorridoPreOrden(self):
        self._recorridoPreOrdenRecursivo(self.raiz_)
    
    def __recorridoPreOrdenRecursivo(self, nodoRaiz):
        if nodoRaiz is not None:
            print(nodoRaiz.getDato(), end=" ")
            self.__recorridoPreOrdenRecursivo(nodoRaiz.getHijoIzquierdo())
            self.__recorridoPreOrdenRecursivo(nodoRaiz.getHijoDerecho())


