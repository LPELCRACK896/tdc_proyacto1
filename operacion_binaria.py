from webbrowser import Opera
from operacion import Operacion

class OperacionB(Operacion):
    def __init__(self, nivel, termino, termino_secundario, operador_superior, operador = None,  index: int = -1, nombre: str = ""):
        super().__init__(nivel, index, nombre)
        self.termino= termino
        self.termino_secundario = termino_secundario
        self.operador: str = operador
        self.operador_superior = operador_superior