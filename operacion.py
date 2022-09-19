from abc import ABC, abstractmethod

class Operacion():
    @abstractmethod
    def __init__(self, nivel: int, index: int = -1, nombre: str  = "") :
        self.index: int = index
        self.nombre = nombre
        self.nivel  = nivel 
        self.isClosed = False