opstack = [] 
def opPop():
    return opstack.pop()

def opPush(value):
    opstack.append(value)

def length():
    if len(opstack) > 0:
        op1 = opPop()
        if (type(op1) == list):
            listLength = len(opPop())
            return listLength
        else:
            print("Error: length - one of the operands is not a numerical value")
            opPop(op1)
    else:
        print("Error: length expects 2 operands")

def test_length(self):
    #(CptS355) length
    opPush('(CptS355)')
    length()
    self.assertEqual(opPop(),7)      
    self.assertTrue(len(opstack)==0) 

def length():
    if len(opstack) > 0:
        op1 = opPop()
    print(list(op1))