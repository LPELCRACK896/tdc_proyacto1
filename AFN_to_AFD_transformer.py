from AFD import AFD
from AFN import AFN

def AFN_to_AFD_transformer(afn: AFN) -> AFD:
    tabla_trancisiones_AFD = {'VACIO': {input: 'VACIO' for input in afn.alfabeto}}# Tabla inicialmente con el estado vacío
    new_states  = ['VACIO']
    accepted_states = []
    needs_empty_state = False
    
    def esEstadoAcpetado(nuevoEstado: set):
        index = 0
        aceptado = False
        nuevoEstado = list(nuevoEstado)
        while index!=len(nuevoEstado) and not aceptado:
            if nuevoEstado[index] in afn.estados_de_aceptacion: aceptado = True
            index += 1        
        return aceptado
    
    pendientes = [afn.cerraduras_de_estados.get(afn.estado_inicial)]

    while len(pendientes)!=0:
        estado_tratado = pendientes[0]
        new_states.append(estado_tratado)
        transitions = {}
        for input in afn.alfabeto:
            if input!= 'ε':
                next_state = set()
                for estado_de_cerradura in estado_tratado:
                    next_possible_states = afn.transitions.get(estado_de_cerradura).get(input)
                    if next_possible_states:
                        for estados_siguientes in next_possible_states:
                            for cerr in afn.cerraduras_de_estados.get(estados_siguientes): 
                                next_state.add(cerr)
                        
                if next_state:
                    transitions[input] = str(next_state)
                    if not next_state in new_states: 
                        pendientes.append(next_state)
                        if esEstadoAcpetado(next_state) and not str(next_state) in accepted_states: accepted_states.append(str(next_state))
                else:
                    needs_empty_state = True
                    transitions[input] = 'VACIO'
        tabla_trancisiones_AFD[str(estado_tratado)] = transitions

        
        pendientes.pop(0)

    if not needs_empty_state:
        new_states.pop(0)
        tabla_trancisiones_AFD.pop('VACIO')
    return AFD(str(afn.cerraduras_de_estados.get(afn.estado_inicial)), [alf for alf in afn.alfabeto if alf != 'ε'], [str(state) for state in new_states], accepted_states, tabla_trancisiones_AFD)
    