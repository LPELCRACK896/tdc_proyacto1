class Stack():
    """
    Stack data structure implementation
    """

    def __init__(self):
        """
        constructor
        """
        self.items = []

    def isEmpty(self):
        """
        checkear si el stack esta vacio
        """
        return self.items == []

    def push(self, item):
        """
        insertar un elemento en el stack
        """
        self.items.append(item)

    def pop(self):
        """
        elimina y devuelve el elemento en el top del stack
        """
        return self.items.pop()

    def peek(self):
        """
        devuelve el ultimo elemento del stack 
        """
        return self.items[len(self.items)-1]

    def size(self):
        """
        devuelve el tamano del stack
        """
        return len(self.items)