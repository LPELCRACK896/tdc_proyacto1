
class NodoCamino():

    def __init__(self, indice: int, nombre: str, numero_paso: int, anterior: int, cerraduras : set, recorrido: list) -> None:
        self.indice: int  = indice
        self.nombre: str = nombre
        self.numero_paso: int = numero_paso
        self.anterior:int = anterior
        self.siguientes: list = []
        self.cerraduras: set = cerraduras
        self.id = f'{indice}-{numero_paso}-{nombre}'
        self.input = None
        self.recorrido = recorrido
    
    def add_siguiente(self, indice_siguiente):
        self.siguientes.append(indice_siguiente)