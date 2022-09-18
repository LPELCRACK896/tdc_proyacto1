from AFD import AFD
from AFN import AFN
r = '(1|0)*'
w = '10000'



'''
logica para obetener de regex a un afn o afd
'''


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
                    },})
#print(afd.transitions)



def writeAFD(afd: AFD):
    trans = "Transitions: "
    for r in afd.transitions:
        for b in afd.transitions.get(r):
            trans += (f"({r}, {b}, {afd.transitions.get(r).get(b)})- ")
    print(f"Estados =  {afd.estados}")
    print(afd.alfabeto)
    print(afd.estado_inicial)
    print(afd.estados_de_aceptacion)
    print(trans)

writeAFD(afd)
#devuelve = afd.emulate_AFD(w)


#print(devuelve)