from sqlite3 import OperationalError
from AFN import AFN
from AFD import AFD
from operacion_binaria import OperacionB
from operacion_unitaria import OperacionU

class Automatabuilder():
    
    def __init__(self, regex) -> None:
        self.operations = ['union', 'estrella',  'concat']
        self.simbolos_operations = {
            '|': 'or',
            '+': 'concat',
            '.': 'concat',
            '*': 'star',
            '': 'concat',
        }
        self.afn: AFN = None
        self.afd: AFD = None
        self.regex = self.reformat_regex(regex)
        self.stack_regex = None
    '''
    Aqui voy a leer la regex y voy a guardar su interpretacion en una lista que tiene referencia de simbolos y otras expresiones

    Considerar incluir el concepto de nivel de prioridad como en el proyecto de lógica -> para dar distinta prioridad segun los parentesis
    '''
    def stack_operation_builder(self, regex: str) -> list:
        """Consideremo esto el convertir el regex a postfix >> En realidad no sé si es precisamente eso, pero es mi forma de hacerlo que sea asmila mas a la idea de un postfix. 

        Args:
            regex (str): Cadena de expresion regular que se desea convertir a AFN y/o AFD

        Returns:
            list: Regresa el self.stackregex con las operacion convertidas a un tipo de post fix
        """
        if not regex:
            print("Definir a un regex valido")
            return
        if 'ε' in regex:
            print("Cadena no pude contener caracter vacio")
            return
        
        reg_index = 0
        nivel  = 1
        regex_format_error = False
        operacion_principal = OperacionU(0, None, None, 'Object', None, -1, 'principal')
        operacion_actual  = operacion_principal
        alfabeto = []
        index = 0
        expect_open_parentesis = True
        expect_regular_char = True
        expect_close_parentesis = False
        opend_parentesis = 0
        expect_operator = False
        opecion_pendiente = None
        # Cada operacion es una tupla
        '''
        Estructura por tupla: 
        > Concatenacion: 
        - 0 > Operacion
        - 1 > Lista de terminos (cada termino puede ser del indice de otra tupla o un termino unitario)
        > Union: 
        - 0 > Operacion
        - 1 > Lista de terminos (cada termino puede ser del indice de otra tupla o un termino unitario)
        > Estrella: 
        - 0 > Operacion
        - 1 > Termino (un termino puede ser del indice de otra tupla o un termino unitario)
        '''
        while reg_index!=len(regex) and not regex_format_error:
            char = regex[reg_index]
            if char=='(' and expect_open_parentesis:
                if operacion_actual.nombre == 'principal':
                    new_termino = OperacionB(nivel, None, None, operacion_actual, None, index, 'parentesis-vacio')
                    operacion_principal.termino = new_termino
                    operacion_actual = new_termino
                    nivel += 1 
                    opend_parentesis += 1
                elif operacion_actual.nombre == 'unitario' or operacion_actual.nombre == 'binario-completo':
                    empar = OperacionB(nivel, operacion_actual, None, operacion_actual.operador_superior, None, index, 'binario')
                    nivel += 1  
                    new_termino = OperacionB(nivel, None, None, empar, None, index, 'parentesis-vacio')
                    empar.termino_secundario = new_termino
                    operacion_actual = empar
                    opend_parentesis += 1
                elif operacion_actual.nombre == 'parentesis-vacio':
                    new_termino = OperacionB(nivel, None, None, operacion_actual, None, index, 'parentesis-vacio')
                    operacion_actual.termino = new_termino
                    operacion_actual.nombre = 'parentesis-con-un-termino'
                    nivel += 1
                else:
                    regex_format_error = True
            elif char == ')' and  opend_parentesis>0:
                pass
            elif char in self.simbolos_operations and expect_operator:
                pass
            elif expect_regular_char:
                if operacion_actual.nombre == 'principal':
                    if not operacion_actual.termino:
                        new_termino =  OperacionU(nivel, char, None, 'string', operacion_principal, index, 'unitario')
                        operacion_principal.termino = new_termino
                        index += 1
                    else:
                        empar = OperacionB(nivel, operacion_actual.termino, None, operacion_principal, None, index, 'binario-completo')
                        new_termino = OperacionU(nivel, char, None, 'string', operacion_principal, index, 'unitario')
                        empar.termino_secundario = new_termino
                        operacion_principal = empar
                        
            else:
                regex_format_error = True



            reg_index += 1

    def reformat_regex(self, regex):
        cont = 0
        last_was_a_star = False
        syntaxis_error = False
        
        while cont<len(regex) and not syntaxis_error:
            char = regex[cont]
            res = None
            sum =  None
            cont_fnd_par =  None
            cont_fnd_par2 =  None
            if self.simbolos_operations.get(char)=='or':
                if cont>0:
                    if regex[cont-1]==')':
                        cont_fnd_par = cont-2
                        cls_par = 0
                        found_it = False
                        while not found_it and not cont_fnd_par < 0: 
                            if regex[cont_fnd_par] == ')': cls_par +=1
                            elif regex[cont_fnd_par] == '(':
                                if cls_par>0: cls_par -= 1
                                else: found_it = True
                            if not found_it: cont_fnd_par -= 1
                        strt_term = cont_fnd_par if found_it else None
                        syntaxis_error = True if not strt_term else False
                    else: 
                        res = 2 if last_was_a_star else 1
                    if not syntaxis_error and regex[cont+1] == '(':
                        cont_fnd_par2 = cont+2
                        opn_par = 0
                        found_it = False
                        while not found_it and not cont_fnd_par2>len(regex): 
                            if regex[cont_fnd_par2] == '(': opn_par +=1
                            elif regex[cont_fnd_par2] == ')':
                                if opn_par>0: opn_par -= 1
                                else: found_it = True                      
                            if not found_it: cont_fnd_par2 += 1
                        fnsh_term = cont_fnd_par2 if found_it else None 
                        syntaxis_error = True if not fnsh_term else False
                    else:
                        sum = 2
                        if len(regex)>cont+2: sum = 3 if regex[cont+2]=='*' else sum
                
                if not syntaxis_error:
                    start_term = cont-res if res else cont_fnd_par
                    finish_term = cont+sum-1 if sum else fnsh_term
                    regex = regex[0:start_term]+'('+regex[start_term: finish_term+1]+')'+regex[finish_term+1: len(regex)]
                    last_was_a_star = False
                    cont = cont+sum-1 if sum else finish_term-1
            elif self.simbolos_operations.get(char)=='star': last_was_a_star = True
            else: last_was_a_star = False  
            cont += 1
        return False if syntaxis_error else regex