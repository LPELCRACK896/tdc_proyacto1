
from AFD import AFD
from itertools import chain

def get_equivalents(equivalencias: list[list[str]], transiciones: dict[str:dict[str:str]]) -> list[list]:
    # 0e
    n_eq = []
    for conjunto in equivalencias:
        for index, estado in enumerate(conjunto):
            

def minimizador_AFD(afd: AFD)-> AFD:
    # E0
    estados = list(set(afd.estados).difference(afd.estados_de_aceptacion))
    e0 = [estados, afd.estados_de_aceptacion]
    # E1, E2, E3, ... , En
    estados_minimizados = get_equivalents(e0, afd.transitions)

    return AFD(afd.estado_inicial, alfabeto=afd.alfabeto, estados=estados_minimizados,
                estados_de_aceptacion=afd.estados_de_aceptacion, transitions=transitions)
