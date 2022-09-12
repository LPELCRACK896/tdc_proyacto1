from AFN import AFN
from AFD import AFD

class Automatabuilder():
    
    def __init__(self, regex) -> None:
        self.operations = ['union', 'estrella',  'concat']
        self.simbolos_operations = {
            '|': 'or',
            '+': 'or',
            '.': 'concat',
            '*': 'star',
            '': 'concat',
        }
        self.afn: AFN= None
        self.afd: AFD = None
        self.regex = regex
        self.stack_regex = None
    '''
    Aqui voy a leer la regex y voy a guardar su interpretacion en una lista que tiene referencia de simbolos y otras expresiones

    Considerar incluir el concepto de nivel de prioridad como en el proyecto de lógica -> para dar distinta prioridad segun los parentesis
    '''
    def stack_operation_builder(self, regex) -> list:
        pass

    