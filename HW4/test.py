# WRITE YOUR NAME and YOUR COLLABORATORS HERE
# Ke Ma

#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the end of the list

# Now define the HELPER FUNCTIONS to push and pop values on the opstack 
# Remember that there is a Postscript operator called "pop" so we choose 
# different names for these functions.
# Recall that `pass` in Python is a no-op: replace it with your code.

def opPop():
    return opstack.pop()
    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

def opPush(value):
    opstack.append(value)

#-------------------------- 16% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to 
# define name, and to lookup a name

def dictPop():
    return dictstack.pop()
    # dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    dictstack.append(d)
    #dictPush pushes the dictionary ‘d’ to the dictstack. 
    #Note that, your interpreter will call dictPush only when Postscript 
    #“begin” operator is called. “begin” should pop the empty dictionary from 
    #the opstack and push it onto the dictstack by calling dictPush.

def define(name, value):
    newdic={}
    newdic['/'+name]=value
    dictPush(newdic)
    #dictPush()
    #add name:value pair to the top dictionary in the dictionary stack. 
    #Keep the '/' in the name constant. 
    #Your psDef function should pop the name and value from operand stack and 
    #call the “define” function.

def lookup(name):
    #searchDict in HW3
    size = len(dictstack) - 1
    return nextIndex(dictstack,name,size)

# helper func for searchDicts2()
def nextIndex(tp,k,index):
     tpList = tp[index] # get tuple at index
     d = tpList[1] # get dict from tuple
     length = len(d.values())
     newIndex = tpList[0] # first tuple value tells us next index
     for (key,value) in d.items(): 
          if key == k:
               return value
          else:
               continue
     if newIndex == index:
          return None 
     return nextIndex(tp,k,newIndex)
    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.


def setUp(self):
    #clear the opstack and the dictstack
    opstack [:] = []
    dictstack [:] = []  

# Tests for helper functions : define, lookup   
def test_lookup1(self):
    dictPush({'/v':3, '/x': 20})
    dictPush({'/v':4, '/x': 10})
    dictPush({'/v':5})
    self.assertEqual(lookup('x'),10)
    self.assertEqual(lookup('v'),5)

def testLookup2(self):
    dictPush({'/a':355})
    dictPush({'/a':[3,5,5]})
    self.assertEqual(lookup("a"),[3,5,5])

def test_define1(self):
    dictPush({})
    define("/n1", 4)
    self.assertEqual(lookup("n1"),4)

def test_define2(self):
    dictPush({})
    define("/n1", 4)
    define("/n1", 5)
    define("/n2", 6)
    self.assertEqual(lookup("n1"),5)
    self.assertEqual(lookup("n2"),6)        

def test_define3(self):
    dictPush({})
    define("/n1", 4)
    dictPush({})
    define("/n2", 6)
    define("/n2", 7)
    dictPush({})
    define("/n1", 6)
    self.assertEqual(lookup("n1"),6)
    self.assertEqual(lookup("n2"),7)  

def gt():
    if len(opstack) >= 2:
        var1 = opstack[len(opstack)-1]
        var2 = opstack[len(opstack)-2]
        if type(var1) == type(var2):
            opPush(var1 < var2)
        else:
            print("Error: incompatable types")
    else:
        print("Error: not enough operands on stack")

def length():
    if len(opstack >= 1):
        var1 = opstack[len(opstack)-1]
        if isinstance(var1, list):
            temp = len(opPop())
            opPush(temp)
        else:
            print("Error: operand is not an array")
    else:
        print("Error: not enough operands on stack")

def length():
    if len(opstack) >= 1:
        op1 = opPop()
        if isinstance(op1, list):
            listLength = len(opPop())
            opPush(listLength)
        else:
            print("Error: length - one of the operands is not a numerical value")
    else:
        print("Error: length expects 2 operands")

def get():
	if len(opstack) >= 2:
		var1 = opstack[len(opstack)-1]
		var2 = opstack[len(opstack)-2]
		if isinstance(var1, int) and isinstance(var2, list):
			var1 = opPop()
			var2 = opPop()
			opPush(var2[var1])
		else:
			print("Error: incompatable types")
	else:
		print("Error: not enough operands on stack")

def length():
    if (len(opstack) > 0):
        op = opPop()
        if (type(op) == list):
            opPush(len(op))
        else:
            opPush(op)

def evaluateArray(aInput):
    fucname={'add':add, 'sub':sub, 'mul':mul, 'eq':eq, 'lt':lt, 'gt':gt, 'getinterval':getinterval}
    for i in aInput:
        if isinstance(i,int):
            opPush(i)
            
        else:
            if aInput[i] in fucname:
                fucname[aInput[i]]()
            elif ('/'+aInput[i]) in dictstack:
                opPush(lookup(aInput[i]))
            else:
                opPush(aInput[i])
    return opstack

def evaluateArray(aInput):
    fucname={'add':add, 'sub':sub, 'mul':mul, 'eq':eq, 'lt':lt, 'gt':gt, 'getinterval':getinterval}
    for c in aInput:
        if isinstance(c, list): # should be the same as [type(c) == list]
            opPush(c)
        elif isinstance(c, int):
            opPush(c)
        elif isinstance(c, bool):
            opPush(c)
        elif c in fucname.keys():   # i think its missing pushing str (fixed)
            fucname[c]()
        elif isinstance(c, str):
            if c[0] == '/':
                opPush(c)
            else: # in dict use lookup...
                op = lookup(c)
                if op == None: # fix this part...
                    opPush(c) # changed from op/ changed from c
                elif isinstance(op, list):
                    evaluateArray(op) # changed from interpreter
                else:
                    opPush(op)

x = [1,'x',3,4,'y',6]
y = 'hahahaha'
for i in x:
    if isinstance(i, str):
        print(i+y)