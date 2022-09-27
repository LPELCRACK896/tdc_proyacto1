from stack import Stack

def process_regex(regex: list):
    """
    ingresa una expresion regular para recorrerla y separarla
    """
    modified = regex[0]
    for i in range(1,len(regex)):
        if( (((regex[i].isalpha() or regex[i].isdigit() ) 
                and regex[i-1] != '(') or regex[i] == '(') 
                and (regex[i-1] != '|' or regex[i-1] == ')') ):
            modified += '.'+regex[i]
        else:
            modified += regex[i]       
    return modified

def infix_to_postfix(regex):
    """
    ingresa una regex, se revisa que caracter es, se compara
    y se va creando una expresion regex que se pasa a str para
    ser devuelta
    """
    ordered = Stack()
    tokens = list(regex)
    output = []

    priority = {
        "*" : 4,
        "?" : 4,
        "+" : 4,
        "." : 3,
        "|" : 2,
        "(" : 1,
    }
    
    for i in tokens:
        if (i.isalpha() or i.isdigit() or i == ' '):
            output.append(i)
        elif (i == '('):
            ordered.push(i)
        elif (i == ')'):
            top = ordered.pop()
            while(top != '('):
                output.append(top)
                top = ordered.pop()
        else:
            while (not ordered.isEmpty()) and (priority[ordered.peek()] >= priority[i]):
                  output.append(ordered.pop())
            ordered.push(i)
    while(not ordered.isEmpty()):
        output.append(ordered.pop())
    
    return ''.join(output)

# conditional is the only one to be checked?