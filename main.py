
import AFN_to_AFD_transformer

from AFD import AFD
from AFN import AFN


r = '(1|0)*'
w = '10000'

afd = AFD('A', ['1', '0'], ['A', 'B'], ['B'],{
                'A':
                    {
                        '0': 'B', 
                        '1': 'A'
                    },
                'B':
                    {
                        '0': 'B', 
                        '1': 'A'
                    },
                }
        )

afn = AFN('A', ['0', '1', 'ε'], ['A', 'B', 'C', 'D', 'E', 'F'], ['D'], 
            {
                'A':
                    {
                        '0': ['E'], 
                        '1': ['B'],
                        'ε': None
                    },
                'B':
                    {
                        '0': None, 
                        '1': ['C'],
                        'ε': ['D']
                    },
                'C':
                    {
                        '0': None, 
                        '1': ['D'],
                        'ε': None
                    },
                'D':
                    {
                        '0': None, 
                        '1': None,
                        'ε': None
                    },
                'E':
                    {
                        '0': ['F'], 
                        '1': None,
                        'ε': ['B', 'C']
                    },
                'F':
                    {
                        '0': ['D'], 
                        '1': None,
                        'ε': None
                    },
            })



AFN_to_AFD_transformer.AFN_to_AFD_transformer(afn)


# AFN(afn)
jelly = 0

''' while jelly == 0:
    print("\n-------Escoga una de las opciones para continuar-------")
    print("1. Transformación de expresión regular a postfix\n2. Generación de AFN (Archivo)\n3. Conversión AFN a AFD (Archivo)\n4. Generación de AFD Directo (Archivo)\n5. Minimización de AFD’s (Archivo)\n6. Simulación AFN y AFD\n7. Salir del programa")

    try:
        opcion = int(input())
        if opcion == 1:
            print("Transformación de expresión regular a postfix")
            regextransformer()
        elif opcion == 2:
            print("Generación de AFN (Archivo)\nSe creará un archivo txt del resultado.")
            f=open("AFN.txt",'w')
        elif opcion == 3:
            print("Conversión AFN a AFD (Archivo)\nSe creará un archivo txt del resultado.")
            AFN_to_AFD_transformer()
        elif opcion == 4:
            print("Generación de AFD Directo (Archivo)\nSe creará un archivo txt del resultado.")
            f=open("AFDD.txt",'w')
        elif opcion == 5:
            print("Minimización de AFD’s (Archivo)\nSe creará un archivo txt del resultado.")
            f=open("minimizado.txt",'w')
        elif opcion == 6:
            print("Simulación AFN y AFD\nSe creará un archivo txt del resultado.")
        elif opcion == 7:
            jelly=1
            print("Programa cerrado")
        else:
            print("Escoga una de las opciones ingresando solamente el número")
    except:
        print("Debe escoger una opción valida")


 '''
