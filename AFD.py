from automata import Automata

class AFD(Automata):

    def __init__(self, estado_inicial, alfabeto=[], estados=[], estados_de_aceptacion=[]):
        if 'ε' in alfabeto: 
            print("No se permite transiciones vacias en un automata determinista")
            return
        super().__init__(estado_inicial, alfabeto, estados, estados_de_aceptacion)
    
    def emulate_AFD(self, cadena: str):
        if self.isAFD:
            cont_r = 0
            for row in self.matriz:
                cont_c = 0
                for column in row:
                    if not column:
                        print(f"No se ha definido la trancision para el estado {self.estados[cont_r]} con input {self.alfabeto[cont_c]}")
                        print(self.matriz)
                        return
                    cont_c +=1 
                cont_r += 1
        
        estado_actual = self.estado_inicial
        res_str = ""
        vertices = [estado_actual]
        for input in cadena:
            res_str += estado_actual
            estado_actual = self.matriz[self.estados.index(estado_actual)][self.alfabeto.index(input)]
            vertices.append(estado_actual)
            res_str += f"-({input})->"+estado_actual+"\n"
        print(res_str)
        return vertices, estado_actual in self.estados_de_aceptacion
    
    def build_AFD_step_by_step(self):
        desdeCero = input("¿Desea definir todas las trancisiones (sobreescribe las que ya esten hecha si hay alguna)?(S/N)").upper()=="S"
        cont_r = 0
        if not self.isAFD:
            print("Se esta llamando ")
        for row in self.matriz[:]:
            cont_c = 0
            for column in row:
                if desdeCero:
                    if not column:
                        estado_final = None
                        estado_inicial = self.estados[cont_r]
                        alf_input = self.alfabeto[cont_c]
                        while not estado_final:
                            ef = input(f"Ingrese el estado al que trancisiona el estado \"{estado_inicial}\" al ingresar {alf_input}: ")
                            if ef in self.estados: estado_final = ef
                            else: print("No es un estado valido....")
                        self.matriz[cont_r][cont_c] = estado_final
                else:
                    if not column:
                        estado_final = None
                        estado_inicial = self.estados[cont_r]
                        alf_input = self.alfabeto[cont_c]
                        while not estado_final:
                            ef = input(f"Ingrese el estado al que trancisiona el estado \"{estado_inicial}\" al ingresar {alf_input}: ")
                            if ef in self.estados: estado_final = ef
                            else: print("No es un estado valido....")
                        self.matriz[cont_r][cont_c] = estado_final
                cont_c +=1 
            cont_r += 1
    
    def set_transition(self, estado_inicial, caracter_input, estado_final):
        if not (estado_inicial in self.estados and caracter_input in self.alfabeto and estado_final in self.estados):
            print("No es posible actualizar el estado")
            return
          
        #Determinista
        if self.isAFD:
            self.matriz[self.estados.index(estado_inicial)][self.alfabeto.index(caracter_input)] = estado_final
            return 

