from nodo import Nodo

class ArbolBinarioBusqueda:
    """
    Clase que representa un árbol binario de búsqueda (ABB).
    """

    def __init__(self):
        """
        Constructor que inicializa un árbol vacío con la raíz en None.
        """
        self._raiz = None

    def get_raiz(self):
        """
        Obtiene la raíz del árbol binario.
        
        Returns:
            El nodo raíz del árbol.
        """
        return self._raiz

    def set_raiz(self, nodo):
        """
        Establece la raíz del árbol binario.
        
        Args:
            nodo: El nodo que se asignará como la raíz del árbol.
        """
        self._raiz = nodo

    def esta_vacio(self):
        """
        Verifica si el árbol está vacío.
        
        Returns:
            True si el árbol está vacío, False en caso contrario.
        """
        return self._raiz is None

    def altura(self, nodo=None):
        """
        Calcula la altura del árbol binario. La altura se define como la longitud
        del camino más largo desde la raíz hasta una hoja.
        
        Args:
            nodo: El nodo desde el cual comenzar a calcular la altura. Si es None,
                  se empieza desde la raíz del árbol.

        Returns:
            La altura del árbol.
        """
        if nodo is None:
            nodo = self._raiz
        if nodo is None:
            return 0
        return 1 + max(self.altura(nodo.get_izq()), self.altura(nodo.get_der()))
