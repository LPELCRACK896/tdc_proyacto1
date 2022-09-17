from automata import Automata
from camino import Camino

class AFN(Automata):
    
    def __init__(self, estado_inicial, alfabeto = [], estados = [], estados_de_aceptacion = [], transitions = {}):
        super().__init__(estado_inicial, alfabeto, estados, estados_de_aceptacion)
        self.transitions: dict = transitions if transitions else {estado: {caracter: [] for caracter in self.alfabeto} for estado in self.estados}#Trancisiones que se realizan entre (representa las aristas), Vertical:  // None indica que no hay trancision
        self.hasTransitionE: bool = 'ε' in self.alfabeto 
        self.cerraduras_de_estados = { estado : set() for estado in self.estados }
        self.caminos = []
        
        self.create_cerradura_de_estados()

    def build_AFN_step_by_step(self):
        pass
    
    def check_cadena(self, cadena):
        aprueba = True
        cont = 0
        while aprueba and cont!=len(cadena):
            aprueba = cadena[cont] in self.alfabeto
            cont += 1
        return aprueba

    def define_transition_matrix(self, transtions):
        self.transitions = transtions
    
    def create_cerradura_de_estados(self):
        # Sin trancisiones epsilon l
        if not self.hasTransitionE:
            self.cerraduras_de_estados = {state: [state] for state in self.estados}
            return
        #Con transiciones epsilon
        revisados = []
        estado_i = 0
        cerradura_est = { estado : {estado} for estado in self.estados }
        while not all(stt in revisados for stt in self.estados):
            if not self.estados[estado_i] in revisados:
                revisados += self.create_cerradura_un_estado(self.estados[estado_i], cerradura_est, [self.estados[estado_i]], [self.estados[estado_i]])[1]
            revisados = self.clean_duplicates(revisados)
            estado_i += 1
        self.cerraduras_de_estados = cerradura_est
    
    def create_cerradura_un_estado(self, estado, dicc_cerraduras: dict, rastro: list, predecesores: list):        
        estados_a_donde_puede_ir_con_epsilon = self.transitions.get(estado).get('ε')#A donde puede ir el estado actual con epsilon    
        revisados:list = rastro[:]
        if estados_a_donde_puede_ir_con_epsilon:
            estados_a_donde_puede_ir_con_epsilon = set(estados_a_donde_puede_ir_con_epsilon)
            for estado_d in estados_a_donde_puede_ir_con_epsilon:
                rastro_est_d:list = rastro[:]
                if not estado_d in rastro:
                    rastro_est_d.append(estado_d)
                    prec_est_d = predecesores[:]
                    if not estado_d in prec_est_d: prec_est_d.append(estado_d)
                    cerr_estado_i, rastro_est_d = self.create_cerradura_un_estado(estado_d, dicc_cerraduras, rastro_est_d, prec_est_d)
                    revisados.extend(rastro_est_d)
                    estados_a_donde_puede_ir_con_epsilon = estados_a_donde_puede_ir_con_epsilon.union(cerr_estado_i)                          
        else:
            estados_a_donde_puede_ir_con_epsilon = {estado}    
        for estado_pred in predecesores:
            dicc_cerraduras[estado_pred] = dicc_cerraduras.get(estado_pred).union(estados_a_donde_puede_ir_con_epsilon)
        
        return estados_a_donde_puede_ir_con_epsilon, revisados
    
    def recorrido_AFN(self, cadena: str):
        if not self.check_cadena(cadena):
            print("Cadena invalida")
            return
        self.create_cerradura_de_estados()
        camino = Camino(f"Camino cadena: {cadena}", cadena, self.cerraduras_de_estados, self.transitions, self.estado_inicial)
        camino.setup_tree()
        self.caminos = camino.caminos_enlistado
        return self.caminos