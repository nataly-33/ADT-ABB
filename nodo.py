class Nodo:
    """
    Clase que representa un nodo en un árbol binario de búsqueda (ABB).
    """

    def __init__(self, valor):
        """
        Constructor que inicializa un nodo con un valor y lo configura
        como un nodo hoja (sin hijos ni padre).
        
        Args:
            valor: El valor que contiene el nodo.
        """
        self._valor = valor
        self._izq = None
        self._der = None
        self._padre = None

    def get_valor(self):
        """
        Obtiene el valor del nodo.
        
        Returns:
            El valor del nodo.
        """
        return self._valor

    def get_izq(self):
        """
        Obtiene el hijo izquierdo del nodo.
        
        Returns:
            El nodo hijo izquierdo.
        """
        return self._izq

    def get_der(self):
        """
        Obtiene el hijo derecho del nodo.
        
        Returns:
            El nodo hijo derecho.
        """
        return self._der

    def get_padre(self):
        """
        Obtiene el nodo padre.
        
        Returns:
            El nodo padre.
        """
        return self._padre

    def set_valor(self, valor):
        """
        Establece el valor del nodo.
        
        Args:
            valor: El nuevo valor que se asignará al nodo.
        """
        self._valor = valor

    def set_izq(self, nodo):
        """
        Establece el hijo izquierdo del nodo.
        
        Args:
            nodo: El nodo que se asignará como hijo izquierdo.
        """
        self._izq = nodo

    def set_der(self, nodo):
        """
        Establece el hijo derecho del nodo.
        
        Args:
            nodo: El nodo que se asignará como hijo derecho.
        """
        self._der = nodo

    def set_padre(self, nodo):
        """
        Establece el nodo padre.
        
        Args:
            nodo: El nodo que se asignará como padre.
        """
        self._padre = nodo


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
class Nodo:
    """
    Clase que representa un nodo en un árbol binario de búsqueda (ABB).
    """

    def __init__(self, valor):
        """
        Constructor que inicializa un nodo con un valor y lo configura
        como un nodo hoja (sin hijos ni padre).
        
        Args:
            valor: El valor que contiene el nodo.
        """
        self._valor = valor
        self._izq = None
        self._der = None
        self._padre = None

    def get_valor(self):
        """
        Obtiene el valor del nodo.
        
        Returns:
            El valor del nodo.
        """
        return self._valor

    def get_izq(self):
        """
        Obtiene el hijo izquierdo del nodo.
        
        Returns:
            El nodo hijo izquierdo.
        """
        return self._izq

    def get_der(self):
        """
        Obtiene el hijo derecho del nodo.
        
        Returns:
            El nodo hijo derecho.
        """
        return self._der

    def get_padre(self):
        """
        Obtiene el nodo padre.
        
        Returns:
            El nodo padre.
        """
        return self._padre

    def set_valor(self, valor):
        """
        Establece el valor del nodo.
        
        Args:
            valor: El nuevo valor que se asignará al nodo.
        """
        self._valor = valor

    def set_izq(self, nodo):
        """
        Establece el hijo izquierdo del nodo.
        
        Args:
            nodo: El nodo que se asignará como hijo izquierdo.
        """
        self._izq = nodo

    def set_der(self, nodo):
        """
        Establece el hijo derecho del nodo.
        
        Args:
            nodo: El nodo que se asignará como hijo derecho.
        """
        self._der = nodo

    def set_padre(self, nodo):
        """
        Establece el nodo padre.
        
        Args:
            nodo: El nodo que se asignará como padre.
        """
        self._padre = nodo
