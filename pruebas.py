from AFN import AFN
from AFD import AFD
import AFN_to_AFD_transformer as afdC

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
afn2 = AFN('A', ['0', '1', 'ε'], ['A', 'B', 'C'], ['C'], 
            {
                'A':
                    {
                        '0': ['B'], 
                        '1': ['B'],
                        'ε': ['B']
                    },
                'B':
                    {
                        '0': None, 
                        '1': ['A'],
                        'ε': ['A']
                    },
                'C':
                    {
                        '0': ['A'], 
                        '1': ['B'],
                        'ε': None
                    },
            }
)

afn.create_cerradura_de_estados()

afd = afdC.AFN_to_AFD_transformer(afn)
print(afd.emulate_AFD('000'))