from automata import Automata

class AFD(Automata):

    def __init__(self, estado_inicial, alfabeto=[], estados=[], estados_de_aceptacion=[]):
        if 'ε' in alfabeto: 
            print("No se permite transiciones vacias en un automata determinista")
            return
        super().__init__(estado_inicial, alfabeto, estados, estados_de_aceptacion)
    
    def emulate_AFD(self, cadena: str):
        cont_r = 0
        for row in self.transitions:
            cont_c = 0
            for column in self.transitions.get(row):
                if not self.transitions.get(row).get(column):
                    print(f"No se ha definido la trancision para el estado {row} con input {column}")
                    print(self.transitions)
                    return
                cont_c +=1 
            cont_r += 1
        
        estado_actual = self.estado_inicial
        res_str = ""
        vertices = [estado_actual]
        for input in cadena:
            res_str += estado_actual
            estado_actual = self.transitions.get(estado_actual).get(input)
            vertices.append(estado_actual)
            res_str += f"-({input})->"+estado_actual+"\n"
        print(res_str)
        return vertices, estado_actual in self.estados_de_aceptacion
    
    def build_AFD_step_by_step(self):
        for estado in self.transitions.copy():
            print(f"Define tranciones de : {estado}")
            for alf in self.alfabeto:
                right_next_state = False
                nxt_state = None
                while not right_next_state:
                    nxt_state = input(f"\tEstado tras ingresar \"{alf}\": ")
                    if nxt_state in self.estados:
                        right_next_state = True
                    if not right_next_state:
                        print("Por favor ingrese algún estado valido. Algunos estados validos son: ")
                        print(self.estados)
                self.transitions.get(estado)[alf] = nxt_state
    
    def set_transition(self, estado_inicial, caracter_input, estado_final):
        if not (estado_inicial in self.estados and caracter_input in self.alfabeto and estado_final in self.estados):
            print("No es posible actualizar el estado")
            return
        self.transitions.get(estado_inicial)[caracter_input] = estado_final

