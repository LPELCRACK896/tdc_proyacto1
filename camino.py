from nodo_camino import NodoCamino
from time import time

class Camino():
    def __init__(self, nombre: str, cadena_recorrida: str, cerradura_asociada: dict, transitions: dict, estado_inicial, estados_de_aceptacion) -> None:
        self.nombre = nombre
        self.cadena_recorrida = cadena_recorrida
        self.caminos_enlistado = []
        self.nodo_raiz: NodoCamino = NodoCamino(-1, 'root', -1, None, None, None)
        self.cerradura_asociada: dict = cerradura_asociada
        self.transitions = transitions
        self.largo: int = len(cadena_recorrida)
        self.estado_inicial = estado_inicial
        self.cerradura_inicial: set = cerradura_asociada.get(estado_inicial)
        self.hasResultDefined = None
        self.estados_de_aceptacion = estados_de_aceptacion
    
    def setup_tree(self):
        index = 0
        start_simulation = time()
        for estado in self.cerradura_inicial:
            self.nodo_raiz.add_siguiente((None, NodoCamino(index, estado, 0, self.nodo_raiz, self.cerradura_asociada.get(estado), [('START>', estado)])))#Añadir a la lista tupla
            index += 1
        
        nodos_a_tratar: list = [tupla_trn_nodo[1] for tupla_trn_nodo in self.nodo_raiz.siguientes]
        cont_cad = 0
        paths = []
        while cont_cad!=self.largo: 
            nuevos_nodos_a_tratar = []
            paso = cont_cad+1
            inpt_alf = self.cadena_recorrida[cont_cad]
            for nodo_actual in nodos_a_tratar: #vemos los nodos a tratar
                nodo_actual.input = inpt_alf
                for estado_en_cerradura in nodo_actual.cerraduras: # La cerradura del respectivo nodo //aun no se involucra ningun input
                    #Se hace la lectura del input sobre la cerradura del estado actual (nodo)
                    if not nodo_actual.nombre==estado_en_cerradura:
                        recorrido = nodo_actual.recorrido[:]
                        recorrido.append(('ε>', estado_en_cerradura))
                        nodo_transitorio_e = NodoCamino(index, estado_en_cerradura, nodo_actual.numero_paso, nodo_actual, self.cerradura_asociada.get(estado_en_cerradura), recorrido)
                        nodo_actual.add_siguiente(['ε', nodo_transitorio_e]) #Se hace la referencia en el nodo actual del siguiente, segun la trancision
                        index += 1
                    else:
                        nodo_transitorio_e = nodo_actual

                    next_estados =  self.transitions.get(estado_en_cerradura).get(inpt_alf) 
                    if next_estados:
                        for next_estado in next_estados:
                            recorrido = nodo_transitorio_e.recorrido[:]
                            recorrido.append((f'{inpt_alf}>', next_estado))
                            nodo_siguiente = NodoCamino(index, next_estado, paso, nodo_transitorio_e, self.cerradura_asociada.get(next_estado), recorrido)
                            nodo_transitorio_e.add_siguiente(nodo_siguiente) #Se hace la referencia en el nodo actual del siguiente, segun la trancision
                            nuevos_nodos_a_tratar.append(nodo_siguiente)
                            index += 1
                    else:
                            recorrido = nodo_transitorio_e.recorrido[:]
                            recorrido.append((f'{inpt_alf}(No trancision definida)>', estado_en_cerradura))
                            nodo_siguiente = NodoCamino(index, nodo_actual.nombre, paso, nodo_transitorio_e, self.cerradura_asociada.get(nodo_actual.nombre), recorrido)
                            nodo_transitorio_e.add_siguiente(nodo_siguiente) #Se hace la referencia en el nodo actual del siguiente, segun la trancision
                            paths.append(nodo_siguiente)
                            index += 1
            
            nodos_a_tratar = nuevos_nodos_a_tratar
            cont_cad += 1
        paths.extend(nodos_a_tratar)
        self.caminos_enlistado = [(nodo.recorrido, nodo.recorrido[-1][1] in self.estados_de_aceptacion ) for nodo in paths]
        return (self.caminos_enlistado, time()-start_simulation)