from AFN import AFN
from AFD import AFD
import AFN_to_AFD_transformer as afdC
from posfix_to_thompson import regex_to_afn_using_thompson
from regex_to_posfix import infix_to_postfix
from generador_de_archivos import *

def show_recorrido_afn(afn: AFN):
    accepted_input = False
    lectura = None
    while not accepted_input:
        lectura = input("Ingresa cadena a simular: ")
        accepted_input = afn_t.check_cadena(lectura)
        if not accepted_input: 
            print('Ingrese una cadena valida, que solo incluya simboloes del alfabeto')
            print('Alfabeto: '+str(afn_t.alfabeto))
            input("Enter para continuar...")
    caminos, tiempo = afn_t.recorrido_AFN(lectura)
    print(f'Tiempo en simulacion: {tiempo}')
    pasa = False
    for camino in caminos:
        print(camino[0])
        if not pasa and camino[1]: pasa = camino[1]
    if pasa: print('La cadena es aceptada')
    else: print('La cadena no es aceptada')
    input("Enter para continuar...")

def show_recorrido_afd(afd: AFD):
    accepted_input = False
    lectura = None
    while not accepted_input:
        lectura = input("Ingresa cadena a simular: ")
        accepted_input = afd.check_cadena(lectura)
        if not accepted_input: 
            print('Ingrese una cadena valida, que solo incluya simboloes del alfabeto')
            print('Alfabeto: '+str(afd.alfabeto))
            input("Enter para continuar...")
    vertices, esAceptada, tiempo = afd.emulate_AFD(lectura)
    if esAceptada: print("La cadena es acpetada")
    else: print("La cadena no es aceptada")
    print(f"El tiempo total de simulacion fue de: {tiempo}")
    input("Enter para continuar...")
#Variables de programa
afd: AFD = None
afn_t: AFN = None
afd_sub: AFD = None
regex: str = None
posfix: str = None

opciones_generales = {'g1': 'Generar archivo txt' }
opciones_con_regex = {  
    'r1': 'Construir AFN a partir de regex (Thompson)', 
    'r2': 'Construir AFD Directo a partir de regex', 
    'r3': 'Construir posfix a partir de regex', 
    'r4': 'Borrar regex', 
    'r5': 'Ver regex'
}
opciones_con_afn_t = {
    'afn_t1': 'Generar archivo del afn de thompson',
    'afn_t2': 'Ver afn', 
    'afn_t3': 'Simular trayectoria de afn', 
    'afn_t4': 'Transformar a AFD', 
    'afn_t5': 'Borrar AFN de thompson'
}
opciones_con_afd_sub = {
    'afd_s1': 'Generar archivo del afd formado con subconjuntos',
    'afd_s2': 'Ver afd', 
    'afd_s3': 'Simular trayectoria de afd de subconjuntos', 
    'afd_s4': 'Minimizar AFD', 
    'afd_s5': 'Borrar AFD de subconjuntos'
}
opciones_con_afd = {
    'afd1': 'Generar archivo del afd',
    'afd2': 'Ver afd', 
    'afd3': 'Simular trayectoria de afd', 
    'afd4': 'Minimizar AFD', 
    'afd5': 'Borrar AFD'
}
opciones_con_posfix = {
    'posf1': 'Ver posfix', 
    'posf2': 'Borrar posfix' 
}

#Variables para el flujo del menu
salir = False

while not salir:

    accepted_input = False  
    while not accepted_input and not regex: 
        want_write_regex = False
        inpt = input("Ingrese el caracter \"R\" para ingresar regex o ingrese \"S\" para salir del programa.\n").strip()
        accepted_input = inpt.upper()=='S' or inpt.upper()=='R'
        if accepted_input: 
            if inpt.upper()=='S': salir = True
            elif inpt.upper()=='R': want_write_regex = True
        else:  input("Ingrese una opcion valida \nEnter para continuar...")
    
    accepted_input = False
    while not salir and want_write_regex and not accepted_input:
        bad_format_regex = False
        inpt = input("Ingresa regex: ")
        bad_format_regex = 'ε' in inpt
        if bad_format_regex: input("La regex no puede incluir el caracter \"ε\"\nEnter para continuar")
        else: 
            accepted_input = True
            regex = inpt

    if not salir and regex:
        accepted_input = False
        opciones_base = {'S': 'Salir de programa'}
        opciones_dicc = opciones_base | opciones_con_regex|(opciones_con_posfix if posfix else {})|(opciones_con_afd if afd else {})|(opciones_con_afd_sub if afd_sub else {})|(opciones_con_afn_t if afn_t else {}) 
        accion = None
        while not accepted_input and not accion: 
            want_write_regex = False
            opciones = ''
            print('\n\n-----------------------------MENU-----------------------------\n\n')
            for opc in opciones_dicc:
                opciones += f'{opc}: {opciones_dicc.get(opc)}\n'
            inpt = input(opciones+"\nIngrese su opcion: ").strip()
            accepted_input = inpt in opciones_dicc
            if accepted_input: accion = inpt 
            else: input('Ingrese una de las opciones indicadas.\nEnter para continuar...')
        
        if accion=='r1':
            print("\nGenerando afn...")
            afn_t = regex_to_afn_using_thompson(regex)
            input('Enter para continuar...')
        elif accion == 'r2':
            print("Lo siento... esta función aun está en producción")
            input('Enter para continuar...')
        elif accion=='r3':
            posfix = infix_to_postfix(regex)
            print("Posfix Generado")
            input('Enter para continuar...')
        elif accion=='r4':
            regex = None
            afn_t = None
            afd = None
            posfix = None
            afd_sub = None
            print("Regex eliminada")
            input('Enter para continuar...')
        elif accion == 'r5':
            print(regex)
        elif accion == 'afn_t1':
            print("Sobreescribiendo archivo AFN.txt")
            writeAFN(afn_t)
            input("Enter para continuar...")
        elif accion == 'afn_t2':
            print("--------------------AFN--------------------")
            print(AFN_toString(afn_t))
            input("Enter para continuar...")
        elif accion == 'afn_t3':
            show_recorrido_afn(afn_t)
        elif accion == 'afn_t4':
            print("\nTransformando a afd (guardando en variable \"afd\")")
            afd  = afdC.AFN_to_AFD_transformer(afn_t)
            input("Enter para continuar...")
        elif accion == 'afn_t5':
            afn_t = None
            print('AFN de thompson eliminado')
            input('Enter para continuar...')
        elif accion == 'afd_s1':
            print("Sobreescribiendo archivo AFD.txt")
            writeAFD(afd_sub)
            input("Enter para continuar...")
        elif accion == 'afd_s2':
            print("--------------------AFD--------------------")
            print(AFD_toString(afd_sub))
            input("Enter para continuar...")
        elif accion == 'afd_s3':
            show_recorrido_afd(afd_sub)
        elif accion == 'afd_s4':
            print("Funcion pendiente")
            input('Enter para continuar...')
        elif accion == 'afd_s5':
            afd_sub = None
            print("Afd de subconjuntos eliminado")
            input("Enter para continuer...")
        elif accion == 'afd1':
            print("Sobreescribiendo archivo AFD.txt")
            writeAFD(afd)
            input("Enter para continuar...")
        elif accion == 'afd2':
            print("--------------------AFD--------------------")
            print(AFD_toString(afd))
            input("Enter para continuar...")
        elif accion == 'afd3':
            show_recorrido_afd(afd)
        elif accion == 'afd4':
            print("Funcion pendiente")
            input('Enter para continuar...')
        elif accion == 'afd5':
            afd = None
            print('Afd borrado')
            input('Enter para continuar...')
        elif accion == 'posf1':
            print("Actual posfix: ")
            print(posfix)
            input("Enter para continuar...")
        elif accion == 'posf2':
            posfix = None
            print("Posfix elimiado")
            input("Enter para continuar...")
        elif accion == 'S':
            salir = True