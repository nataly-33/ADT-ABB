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
