from automata import Automata


class AFN(Automata):
    
    #'ε' in alfabeto
    # self.indice_estado_e: int = self.estados.index('ε')
    # self.cerraduras_de_estados = { estado:None for estado in self.estados }
    def __init__(self, estado_inicial, alfabeto=[], estados=[], estados_de_aceptacion=[]):
        super().__init__(estado_inicial, alfabeto, estados, estados_de_aceptacion)
        self.transitions: dict = {estado: {caracter: [] for caracter in self.alfabeto} for estado in self.estados}#Trancisiones que se realizan entre (representa las aristas), Vertical:  // None indica que no hay trancision
        self.indice_estado_e: int = self.alfabeto.index('ε') if 'ε' in self.alfabeto else -1
        self.cerraduras_de_estados = { estado:None for estado in self.estados }

    def build_AFN_step_by_step(self):
        pass

    def console_use_define_mult_transition(self):
        pass

    def console_use_define_single_transition(self):
        pass
    
    def define_transition_matrix(self):
        pass

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
            revisados = self.clean_duplicates(revisados)
            estado_i += 1
        self.cerradura_de_estados = cerradura_est
    def cerradura_un_estado(self, estado, dicc_cerraduras: dict, rastro: list):
        for estado_r in rastro:
            if dicc_cerraduras.get(estado_r):
                dicc_cerraduras.get(estado_r).add(estado)
            else:
                dicc_cerraduras[estado] = {estado}
            print('a')
        estados_a_donde_puede_ir_con_epsilon = self.transitions.get(estado).get('ε')#A donde puede ir el estado actual con epsilon
        revisados:list = rastro
        for estado_d in estados_a_donde_puede_ir_con_epsilon:
            if not estado in rastro:
                rev:list = rastro
                rev.append(estado_d)
                revisados.extend(self.cerradura_de_estados(estado_d, dicc_cerraduras, rev))
            print('b')
        return revisados
    
    def recorrido_AFN(self):
        pass
