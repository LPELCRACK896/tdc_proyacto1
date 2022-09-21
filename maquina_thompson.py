from AFN import AFN
class MaquinaThompson():

    def __init__(self,  termino_1, termino_2, operador, nombre, ultimo_estado_global, alfabeto) -> None:
        self.alfabeto = alfabeto
        self.nombre = nombre
        self.termino_1 = termino_1
        self.termino_2 = termino_2
        self.operador = operador
        self.ultimo_estado_global = ultimo_estado_global
        self.estado_final = None
        self.ultimo_estado_propio = None
        self.total_estados = None
        self.estados_nuevos = None
        self.afn = None
        self.createAFN()
    
    def createAFN(self):
        if self.operador: 
            if self.operador == '*': self.createClausura()
            elif self.operador == '|': self.createDisyuncion()
            elif self.operador == '.': self.createConcatenacion()
            else: print(f"Error en operador {self.operador}")
        else: self.createSymbol()
    
    def updateTrans(self, dicc: dict, estado: str, trans, nuevoEstado):
        if dicc.get(estado).get(trans):
            if not nuevoEstado in dicc.get(estado).get(trans):
                dicc.get(estado).get(trans).append(nuevoEstado)
        else:
            dicc.get(estado)[trans] = [nuevoEstado]
        return dicc
    
    def createSymbol(self):
        self.estados_nuevos = 2
        self.total_estados = self.estados_nuevos
        estados = [ f'q{r}'for r in range(self.ultimo_estado_global+1, self.ultimo_estado_global+self.total_estados+1)]
        self.estado_final = estados[1]
        self.afn = AFN(estados[0], [self.termino_1], estados, [estados[1]], {
            estados[0]: { alf: [estados[1]] if alf==self.termino_1 else None for alf in self.alfabeto },
            estados[1]: { alf: None for alf in self.alfabeto }
        }   )
    
    def createDisyuncion(self):
        self.estados_nuevos = 2
        self.total_estados = self.estados_nuevos + self.termino_1.total_estados + self.termino_2.total_estados
        estados = [ f'q{r}'for r in range(self.ultimo_estado_global+1, self.ultimo_estado_global+self.estados_nuevos+1)]
        self.estado_final = estados[-1]
        estado_inicial = estados[0]
        trans_nvs  = {estado: {alf: None for alf in self.alfabeto} for estado in estados}
        self.updateTrans(trans_nvs, estados[0], 'ε', self.termino_1.afn.estado_inicial)
        self.updateTrans(trans_nvs, estados[0], 'ε', self.termino_2.afn.estado_inicial)
        trans = self.termino_1.afn.transitions |  self.termino_2.afn.transitions 
        trans = trans | trans_nvs
        self.updateTrans(trans, self.termino_1.estado_final, 'ε', estados[1])
        self.updateTrans(trans, self.termino_2.estado_final, 'ε', estados[1])
        estados.extend(self.termino_1.afn.estados)
        estados.extend(self.termino_2.afn.estados) 

        self.afn = AFN(estado_inicial, self.alfabeto, estados, [self.estado_final], trans)
        
    def createConcatenacion(self):
        self.estados_nuevos = 0
        self.total_estados = self.estados_nuevos + self.termino_1.total_estados + self.termino_2.total_estados
        self.estado_final = self.termino_2.estado_final
        estados = self.termino_1.afn.estados
        estados.extend(self.termino_2.afn.estados)
        trans = self.termino_1.afn.transitions |  self.termino_2.afn.transitions 
        self.updateTrans(trans, self.termino_1.estado_final, 'ε', self.termino_2.afn.estado_inicial)
        
        self.afn = AFN(self.termino_1.afn.estado_inicial, self.alfabeto, estados, self.termino_2.afn.estados_de_aceptacion, trans)
    
    def createClausura(self):
        self.estados_nuevos = 2
        self.total_estados = self.estados_nuevos + self.termino_1.total_estados
        estados = [ f'q{r}'for r in range(self.ultimo_estado_global+1, self.ultimo_estado_global+self.estados_nuevos+1)]
        estado_inicial = estados[0]
        self.estado_final = estados[1]
        trans_nvs  = {estado: {alf: None for alf in self.alfabeto} for estado in estados}
        self.updateTrans(trans_nvs, estado_inicial, 'ε', self.termino_1.afn.estado_inicial)
        self.updateTrans(trans_nvs, estado_inicial, 'ε', self.estado_final)
        trans_nvs  =  self.termino_1.afn.transitions | trans_nvs 
        self.updateTrans(trans_nvs, self.termino_1.estado_final, 'ε', self.termino_1.afn.estado_inicial)       
        self.updateTrans(trans_nvs, self.termino_1.estado_final, 'ε', self.estado_final)
        estados.extend(self.termino_1.afn.estados)

        self.afn = AFN(estado_inicial, self.alfabeto, estados, [self.estado_final], trans_nvs)