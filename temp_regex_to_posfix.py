class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def processRegex(regex):
    modified = regex[0]
    for i in range(1,len(regex)):
        if( (((regex[i].isalpha() or regex[i].isdigit() ) and regex[i-1] != '(') or regex[i] == '(') and (regex[i-1] != '|' or regex[i-1] == ')') ):
            modified += '.'+regex[i]
        else:
            modified += regex[i]       
    return modified

def infix2postfix(regex):
    prec = {}
    prec["*"] = 4
    prec["?"] = 4
    prec["+"] = 4
    prec["."] = 3
    prec["|"] = 2
    prec["("] = 1
    tokens = list(regex)
    output = []
    stack = Stack()
    for token in tokens:
        if (token.isalpha() or token.isdigit() or token == ' '):
            output.append(token)
        elif (token == '('):
            stack.push(token)
        elif (token == ')'):
            top = stack.pop()
            while(top != '('):
                output.append(top)
                top = stack.pop()
        else:
            while (not stack.isEmpty()) and (prec[stack.peek()] >= prec[token]):
                  output.append(stack.pop())
            stack.push(token)
    while(not stack.isEmpty()):
        output.append(stack.pop())
    
    return ''.join(output)

def run(regex): return infix2postfix(processRegex(regex))

# conditional is the only one to be checked