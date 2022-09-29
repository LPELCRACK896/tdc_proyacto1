
from AFD import AFD
from itertools import chain, product

def get_equivalents(equivalencias: list[list[str]], transiciones: dict[str:dict[str:str]]) -> list[list[str]]:

    n_eq = []
    for conjunto in equivalencias: # revisar cada conjunto
        for index, estado in enumerate(conjunto): # revisar cada estado en el conjunto
            transiciones_de_estado = list(transiciones.items()) # version iterable de las transiciones
            index_estado = transiciones_de_estado.index(estado) # indice del estado actual en el iterable 
            if index_estado < len(transiciones_de_estado)-1: # chequear si es el ultimo elemento para evitar error
                estado_a_comparar = transiciones_de_estado[index_estado+1] # recuperar estado a comparar con el actual
                for i, item in enumerate(list(transiciones[estado].items())): # iterar cada transicion del estado
                    if (item[1] in conjunto) and (estado_a_comparar[1] in conjunto): # si el destino de la transicion actual y el destino de la transicion 
                        # a comparar pertencen al mismo conjunto quiere decir que hay una equivalencia entre estos estados 
                        n_eq.append([item[1], transiciones_de_estado[i+1]]) #
    if equivalencias == n_eq:
        return n_eq # verificar si las equivalencias son irreducibles, si lo son se devuelve la lista con los estados minimizados
    else:
        get_equivalents(n_eq, transiciones) # si no lo son quiere decir que aun se pueden reducir mas

                        

def minimizador_AFD(afd: AFD)-> AFD:
    # E0
    estados = list(set(afd.estados).difference(afd.estados_de_aceptacion))
    e0 = [estados, afd.estados_de_aceptacion]
    # E1, E2, E3, ... , En
    estados_minimizados = get_equivalents(e0, afd.transitions)

    return AFD(afd.estado_inicial, alfabeto=afd.alfabeto, estados=estados_minimizados,
                estados_de_aceptacion=afd.estados_de_aceptacion, transitions=afd.transitions)
