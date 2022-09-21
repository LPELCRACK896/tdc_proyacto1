from temp_regex_to_posfix import run
from maquina_thompson import MaquinaThompson

def regex_to_afn_using_thompson(regex):
    posfix = run(regex)
    cont = 0
    estados_utilizado = -1
    operadores = ['*', '|', '.'] 
    alfabeto = set()

    terminos = [] # lista:  [termino,  isReservado]
    error = False
    for r in posfix: 
        if r not in operadores: alfabeto.add(r)
    alfabeto.add('ε')
    alfabeto = list(alfabeto)
    while cont<len(posfix) and not error:
        char = posfix[cont]
        cont += 1
        if char in operadores:
            if char == '*':
                if terminos[-1]:
                    terminos[-1] = MaquinaThompson(terminos[-1], None, char, 'estrella', estados_utilizado, alfabeto)
                    estados_utilizado += terminos[-1].estados_nuevos
                else: error = True
            else:
                if len(terminos)>1:
                    nombre = 'disyuncion' if char=='|' else 'concatenacion'
                    terminos[-2] = MaquinaThompson(terminos[-2], terminos[-1], char, nombre, estados_utilizado, alfabeto)
                    terminos.pop()
                    estados_utilizado += terminos[-1].estados_nuevos
                else: error = True
        else:
            maq = MaquinaThompson(char, None, None, f'simple-{char}', estados_utilizado, alfabeto)
            terminos.append(maq)
            estados_utilizado += maq.estados_nuevos
    return terminos[0].afn if not error and len(terminos)==1 else None