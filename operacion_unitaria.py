from operacion import Operacion

class OperacionU(Operacion):
    def __init__(self, nivel, termino, operador, tipo_de_termino, operador_superior, index: int = -1, nombre: str = ""):
        super().__init__(nivel, index, nombre)
        self.termino = termino
        self.operador = operador
        self.tipo_de_termino = tipo_de_termino
        self.operador_superior = operador_superior



