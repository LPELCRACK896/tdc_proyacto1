from AFD import AFD
from itertools import chain

def get_equivalents():
    pass

def minimizador_AFD(afd: AFD)-> AFD:
    # E0
    estados = list(set(afd.estados).difference(afd.estados_de_aceptacion))
    e0 = [estados, afd.estados_de_aceptacion]
    # E1
    # rev_dict = {}
    # for key, value in afd.transitions.items():
    #     rev_dict.setdefault(value, set()).add(key)
    
    # e1 = list(set(chain.from_iterable(values for key, values in rev_dict.items() if len(values) > 1)))

    # if 

    for estado in afd.estados:
