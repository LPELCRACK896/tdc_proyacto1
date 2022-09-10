from sre_parse import State
from automata import Automata


class AFN(Automata):
    
    #'ε' in alfabeto
    # self.indice_estado_e: int = self.estados.index('ε')
    # self.cerraduras_de_estados = { estado:None for estado in self.estados }
    def __init__(self, estado_inicial, alfabeto=[], estados=[], estados_de_aceptacion=[]):
        super().__init__(estado_inicial, alfabeto, estados, estados_de_aceptacion)
        self.matriz: list = [[[] for caracter in self.alfabeto] for estado in self.estados] #Trancisiones que se realizan entre (representa las aristas), Vertical:  // None indica que no hay trancision
        self.indice_estado_e: int = self.alfabeto.index('ε') if 'ε' in self.alfabeto else -1
        self.cerraduras_de_estados = { estado:None for estado in self.estados }

    def set_transition(self, estado_inicial, caracter_input, estado_final):

        if not (estado_inicial in self.estados and caracter_input in self.alfabeto and estado_final in self.estados):
            print("No es posible actualizar el estado")
            return
          
        #En caso no sea determinista

        #En caso no tenga trancision definida aun
        if not self.matriz[self.estados.index(estado_inicial)][self.alfabeto.index(caracter_input)]:
            self.matriz[self.estados.index(estado_inicial)][self.alfabeto.index(caracter_input)] = [estado_final]
            return
        
        #En caso ya tenga una trancision definida
        self.matriz[self.estados.index(estado_inicial)][self.alfabeto.index(caracter_input)].append(estado_final)
        return   
    
    def cerradura_de_estados(self):
        # Sin trancisiones epsilon 
        if self.indice_estado_e==-1:
            self.cerradura_de_estados = {state: [state] for state in self.estados}
            return
        #Con transiciones epsilon
        revisados = []
        estado_i = 0
        cerradura_est = {}
        while not self.estados == revisados:
            if not self.estados[estado_i] in revisados:
                revisados = self.cerradura_un_estado(self.estados[estado_i], cerradura_est, [self.estados[estado_i]])
            estado_i += 1


    def cerradura_un_estado(self, estado, dicc_cerraduras, rastro):
        for estado in rastro:
            if dicc_cerraduras.get(estado):
                dicc_cerraduras.get(estado).add(estado)
            else:
                dicc_cerraduras[estado] = {estado}
        
        estados_trn = self.cerradura_de_estados[self.estados.index(estado)][self.indice_estado_e]
        
        if estados_trn:
            pass
        