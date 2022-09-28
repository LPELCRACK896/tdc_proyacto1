from AFD import AFD
from AFN import AFN
def writeAFD(afd: AFD):
    trans = ""
    for r in afd.transitions:
        for b in afd.transitions.get(r):
            trans += (f"({r}, {b}, {afd.transitions.get(r).get(b)})- ")
  

    f=open("AFD.txt",'w',encoding="utf-8")
    
    f.write('Estados: '+str(afd.estados)+'\n'+'Simbolos: '+str(afd.alfabeto)+'\n'+'Estado inicial: '+str(afd.estado_inicial)+'\n'+'Aceptacion: '+str(afd.estados_de_aceptacion)+'\n'+'Transiciones: '+str(trans)+'\n')

def writeAFN(afn: AFN):
        f=open("AFN.txt",'w',encoding="utf-8")
        trans=""
        tablita = afn.transitions
        for r in tablita:
            for b in tablita.get(r):
                trans += (f"({r}, {b}, {tablita.get(r).get(b)})- ")
        
        f.write('Estados: '+str(afn.estados)+'\n'+'Simbolos: '+str(afn.alfabeto)+'\n'+'Estado inicial: '+str(afn.estado_inicial)+'\n'+'Aceptacion: '+str(afn.estados_de_aceptacion)+'\n'+'Transiciones: '+str(trans)+'\n')