from abc import ABC, abstractmethod

class Automata(ABC):
    @abstractmethod
    def __init__(self, estado_inicial, alfabeto = [], estados = [], estados_de_aceptacion = [] ) :
        """Constructor de automata. Se reserva el caracter 'ε' para la trancision vacia
            0 1 2 <- Simbolo de entrada
        A | Estado resultante 
        B |
        C |
        ^ Estados de los que viene
        Args:
            estado_inicial (_type_): _description_
            alfabeto (list, optional): _description_. Defaults to [].
            estados (list, optional): _description_. Defaults to [].
            isAFD (bool, optional): _description_. Defaults to True.
            estados_de_aceptacion (list, optional): _description_. Defaults to [].

        Returns:
            _type_: _description_
        """
        if not estado_inicial in estados:
            print("No es posible establecer el estado inicial dado los estados descritos para el automata")
            return
        if not all(item in estados for item in estados_de_aceptacion):
            print("No es posible crear la lista de aceptacion dado los estados descritos para el automata")
            return
        
        self.alfabeto: list = self.clean_duplicates(alfabeto) #Aceptado como trancisiones (nombre de arista, digamos)
        self.estados: list = self.clean_duplicates(estados) #Estados (vertices)
        self.transitions: dict = {estado: {caracter: None for caracter in self.alfabeto} for estado in self.estados} #Trancisiones que se realizan entre (representa las aristas), Vertical:  // None indica que no hay trancision
        self.estado_inicial = estado_inicial
        self.estados_de_aceptacion: list = [item for item in estados_de_aceptacion if item in self.estados]
        return  
    
    def clean_duplicates(self, lista):
        return list(set(lista))