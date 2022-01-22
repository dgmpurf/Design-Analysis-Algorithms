# WRITE YOUR NAME and YOUR COLLABORATORS HERE
# Ke Ma
# get access from Proffessor code in pdf
#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the end of the list

# Now define the HELPER FUNCTIONS to push and pop values on the opstack 
# Remember that there is a Postscript operator called "pop" so we choose 
# different names for these functions.
# Recall that `pass` in Python is a no-op: replace it with your code.

def opPop():
    if (len(opstack) > 0):
        return opstack.pop()
    else:
        return opstack
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
    dictstack.pop()
    # dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    dictstack.append(d)
    #dictPush pushes the dictionary ‘d’ to the dictstack. 
    #Note that, your interpreter will call dictPush only when Postscript 
    #“begin” operator is called. “begin” should pop the empty dictionary from 
    #the opstack and push it onto the dictstack by calling dictPush.

def define(name, value):
    newdic={}
    newdic[name]=value
    dictPush(newdic)
    #dictPush()
    #add name:value pair to the top dictionary in the dictionary stack. 
    #Keep the '/' in the name constant. 
    #Your psDef function should pop the name and value from operand stack and 
    #call the “define” function.

def lookup(name):
    #searchDict in HW3
    postName = '/' + name
    c = 0
    i = -1
    while c < len(dictstack):
        if dictstack[i].get(postName,None) is None:
            i -= 1
            c += 1
        else:
            return dictstack[i].get(postName,None)
    print ("Error: no name")
    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.

#--------------------------- 10% -------------------------------------
# Arithmetic and comparison operators: add, sub, mul, eq, lt, gt 
# Make sure to check the operand stack has the correct number of parameters 
# and types of the parameters are correct.
def add():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1, int) and isinstance(op2,int)):
            opPush(op1+op2)
        else:
            print("Error: add - one of the operands is not a numerical value")
            opPop(op1)
            opPush(op2)
    else:
        print("Error: add expects 2 operands")

def sub():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1, int) and isinstance(op2,int)):
            opPush(op1 - op2)
        else:
            print("Error: sub - one of the operands is not a numerical value")
            opPop(op1)
            opPush(op2)
    else:
        print("Error: sub expects 2 operands")

def mul():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1, int) and isinstance(op2,int)):
            opPush(op1 * op2)
        else:
            print("Error: mul - one of the operands is not a numerical value")
            opPop(op1)
            opPush(op2)
    else:
        print("Error: mul expects 2 operands")

def eq():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1, int) and isinstance(op2,int) and op1 == op2):
            opPush(op1 == op2)
        elif(isinstance(op1, list) and isinstance(op2,list) and set(op1) == set(op2)):
            opPush(op1 == op2)
        else:
            print("Error: eq - one of the operands is not a numerical value")
            opPop(op1)
            opPush(op2)
    else:
        print("Error: eq expects 2 operands")

def lt():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1, int) and isinstance(op2,int)):
            opPush(op1 < op2)
        else:
            print("Error: lt - one of the operands is not a numerical value")
            opPop(op1)
            opPush(op2)
    else:
        print("Error: lt expects 2 operands")

def gt():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1, int) and isinstance(op2,int)):
            opPush(op1 > op2)
        else:
            print("Error: gt - one of the operands is not a numerical value")
            opPop(op1)
            opPush(op2)
    else:
        print("Error: gt expects 2 operands")
#--------------------------- 20% -------------------------------------
# String operators: define the string operators length, get, getinterval,  putinterval, search
def length():
    if len(opstack) > 0:
        op1 = opPop()
        if isinstance(op1, str):
            listLength = len(op1)-2
            opPush(listLength)
        else:
            print("Error: length - one of the operands is not a numerical value")
            opPop(op1)
    else:
        print("Error: length expects 2 operands")


def get():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op2, int) and isinstance(op1,str)):
            opPush(ord(op1[op2+1]))
        else:
            print("Error: get - one of the operands is not a numerical value")
    else:
        print("Error: get expects 2 operands")

def getinterval():
    if len(opstack) > 1:
        op3 = opPop()
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op3, int) and isinstance(op2,int) and isinstance(op1,str)):
            opPush('(' + op1[op2+1:op2+op3+1] + ')')
        else:
            print("Error: getinterval - one of the operands is not a numerical value")
    else:
        print("Error: getinterval expects 2 operands")

def putinterval():
    op1 = opPop()
    op2 = opPop()
    op3 = opPop()
    if op2 < len(op3):
        for i in op1:
            op3[op2] = i
            op2 += 1
    else:
        print("Error: putinterval expects 2 operands")

def search():
    if len(opstack) > 1:
        op0 = opPop()
        op1 = opPop()
        #somchar = ["(",")"]
        #op0=''.join(m for m in op0 if not m in somchar)
        if(isinstance(op1,str)):
            opp0 = op0.replace('(','').replace(')','')
            if opp0 in op1:
                opp=op1.split(opp0,1)
                opPush('('+opp[1])
                opPush('('+opp0+')')
                opPush(opp[0]+')')
                opPush(True)
            else:
                opPush(op1)
                opPush(False)

        else:
            print("Error: search - one of the operands is not a numerical value")
    else:
        print("Error: search expects 2 operands")


#--------------------------- 18% -------------------------------------
# Array functions and operators:
#      define the helper function evaluateArray
#      define the array operators aload, astore
def evaluateArray(aInput):
    fucname={'add':add, 'sub':sub, 'mul':mul, 'eq':eq, 'lt':lt, 'gt':gt, 'getinterval':getinterval}
    for i in aInput:
        if isinstance(i,int):
            opPush(i)
        elif isinstance(i, bool):
            opPush(i)
        elif i in fucname:
            fucname[i]()
        elif isinstance(i, str):
            if ('/'+i) in dictstack:
                p = lookup(i)
                opPush(p)
            else:
                opPush(i)
    return opstack
    #should return the evaluated array

def aload():
    op = opPop()
    for i in op:
        opPush(i)
    opPush(op)

def astore():
    op = opPop()
    j=len(op)
    l1=[]
    for i in range(0,j):
        l1.append(opPop())
    opPush(list(reversed(l1)))




#--------------------------- 6% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, count, pop, clear, exch, stack
def dup():
    if (len(opstack) > 0):
        opPush(opstack[-1])
    else:
        print("Error: dup expects 2 operands")

def copy():
    if len(opstack) > 1:
        op1 = opPop()
        if (op1 <= len(opstack) + 1):
            cl = []
            while (op1 > 0):
                cl.append(opPop())
                op1 = op1 - 1
            cl.reverse()
            opstack.extend(cl)
            opstack.extend(cl)
        else:
            print("Error: copy - one of the operands is not a numerical value")
    else:
        print("Error: copy expects 2 operands")

def count():
    return len(opstack)

def pop():
    if len(opstack) > 0:
        opPop()
    else:
        print("Error: pop expects 2 operands")

def clear():
    opstack.clear()

def exch():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        opPush(op2)
        opPush(op1)
    else:
        print("Error: exch expects 2 operands")

def stack():
    if len(opstack) > 0:
        for i in range(0,len(opstack)):
            print(opstack[i])
#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.
def psDict():
    s = opPop()
    for i in range(s):
        opPush(dict())

def begin():
    if len(opstack) > 0:
        op1 = opPop()
        if isinstance(op1, dict):
            dictPush(op1)
        else:
            print("Error: begin - one of the operands is not a numerical value")
    else:
        print("Error: begin expects 2 operands")

def end():
    dictPop()

def psDef():
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        define(op2,op1)
    else:
        print("Error: psDef expects 2 operands")