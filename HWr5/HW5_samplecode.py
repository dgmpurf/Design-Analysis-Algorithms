
# WRITE YOUR NAME and YOUR COLLABORATORS HERE
# Ke Ma
# get access from Proffessor code in pdf
## Change the following functions for static scope support. 
# dictPush
# define
# lookup
# stack
# evaluateArray

# Add a scope argument to the the following functions 
# psIf
# psIfelse
# psFor
# interpretSPS
# interpreter
import re

def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[\[][a-zA-Z-?0-9_\s\(\)!][a-zA-Z-?0-9_\s\(\)!]*[\]]|[\()][a-zA-Z-?0-9_\s!][a-zA-Z-?0-9_\s!]*[\)]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)  

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
    pass
    # if len(opstack) > 1:
    #     op1 = opPop()
    #     if op1[0]=='(':
    #         op2 = opPop()
    #         str1 = op1.replace('(','').replace(')','')
    #         if isinstance(op2,int):
    #             op3 = opPop()
    #             if op3[0]==('('):
    #                 str_id=id(op3)
    #                 str3 = op3.replace('(','').replace(')','')
    #                 str_result = '(' + str3[:op2] + str1 + str3[(len(str1) + op2):] + ')'
    #                 if len(dictstack) > 0:
    #                     if op3 in dictstack[-1].values():
    #                         dick_K = list(dictstack[-1].keys())[list(dictstack[-1].values().index(op3))]
    #                         dictstack[-1][dick_K]=str_result
    #                 if len(opstack) > 0:
    #                     for i in range(len(opstack)):
    #                         if id(opstack[i])==str_id:
    #                             opstack[i] = str_result
    # else:
    #     print("error")



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

#-------------Part 2-------------
def psIf():
    op1 = opPop()
    op2 = opPop()
    if op2 == True:
        interpretSPS(op1)

def psIfelse():
    op1 = opPop()
    op2 = opPop()
    op3 = opPop()
    if op3 == True:
        interpretSPS(op2)
    else:
        interpretSPS(op1)

def psFor():
    op1 = opPop()
    op2 = opPop()
    for item in op2:
        opPush(item)
        interpretSPS(op1)

fnc={'add':add, 'sub':sub, 'mul':mul, 'eq':eq, 'lt':lt, 'gt':gt, 'getinterval':getinterval, 'def':psDef, 'end':end, 'begin':begin, 'dict':psDict, 'stack':stack, 'exch':exch, 'clear':clear, 'pop':pop, 'count':count, 'copy':copy, 'dup':dup, 'astore':astore, 'aload':aload, 'search':search, 'putinterval':putinterval, 'get':get, 'length':length, 'for':psFor, 'if':psIf, 'ifelse':psIfelse}

# COMPLETE THIS FUNCTION
# The it argument is an iterator.
# The tokens between '{' and '}' is included as a sub code-array (dictionary). If the
# parenteses in the input iterator is not properly nested, returns False.
def numberMatch(it):
    lz = []
    it = it.split(" ")
    for c in it:
        end = c[-1]
        start = c[0]
        if end == ']':
            lz.append(convert(c[0:-1]))
            #end
            return lz
        elif start == '[':
            lz.append(numberMatch(it))
        elif c != ' ':
            lz.append(convert(c))
    return False

def groupMatch(it):
    res = []
    for c in it:
        if c == '}':
            return {'codearray':res}
        elif c=='{':
            # Note how we use a recursive call to group the tokens inside the
            # inner matching parenthesis.
            # Once the recursive call returns the code-array for the inner 
            # parenthesis, it will be appended to the list we are constructing 
            # as a whole.
            res.append(groupMatch(it))
        else:
            res.append(convert(c))
    return False

def convert(val):
    if val == 'true':
        return True
    elif val == 'false':
        return False
    elif '.' in val:
        try:
            return float(val)
        except:
            return val
    else:
        try:
            return int(val)
        except:
            return val
# COMPLETE THIS FUNCTION
# Function to parse a list of tokens and arrange the tokens between { and } braces 
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested dictionaries.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c=='}' or c==']':  #non matching closing parenthesis; return false since there is 
                    # a syntax error in the Postscript code.
            return False
        elif c=='{':
            res.append(groupMatch(it))
        elif c[0] == '[':
            a = numberMatch(c[1:])
            res.append(a)
        else:
            res.append(convert(c))
    return {'codearray':res}

# COMPLETE THIS FUNCTION 
# This will probably be the largest function of the whole project, 
# but it will have a very regular and obvious structure if you've followed the plan of the assignment.
# Write additional auxiliary functions if you need them. 
# def interpretSPS(code): # code is a code array
#     for i in code:
#         if isinstance(i, (list, int, bool, str)):
#             if isinstance(i, (list, int, bool)):
#                 opPush(i)
#             elif i[0] == '(' or i[0] == '/' or i[0] == '{':
#                 opPush(i)
#             elif i in fnc.keys():
#                 func = fnc[i]
#                 func()
#             elif isinstance(i, str):
#                 op = lookup(i)
#                 if isinstance(op,list):
#                     interpretSPS(iter(op))
#                 elif isinstance(op, (str, int, bool)):
#                     opPush(op)
#                 elif op == None:
#                     opPush(i)
#                 else:
#                     opPush(op)
#         else: 
#             opPush(i)

# def interpreter(s): # s is a string
#     interpretSPS(parse(tokenize(s)))

# #clear opstack and dictstack
# def clearStacks():
#     opstack[:] = []
#     dictstack[:] = []

# ------ SSPS functions -----------
# search the dictstack for the dictionary "name" is defined in and return the (list) index for that dictionary (start searhing at the top of the stack)
def staticLink(name):
    for i in range(len(dictstack)):
        inp = dictstack[len(dictstack)-i-1][0]
        if inp.get(name) != None:
            return(len(dictstack)-i-1,inp[name])


#the main recursive interpreter function
def interpretSPS(tokenList,scope):
    for i in tokenList:
        if isinstance(i, (list, int, bool, str)):
            if isinstance(i, (list, int, bool)):
                opPush(i)
            elif i[0] == '(' or i[0] == '/' or i[0] == '{':
                opPush(i)
            elif i in fnc.keys():
                func = fnc[i]
                func()
            elif isinstance(i, str):
                op = lookup(i)
                if isinstance(op,list):
                    interpretSPS(iter(op))
                elif isinstance(op, (str, int, bool)):
                    opPush(op)
                elif op == None:
                    opPush(i)
                else:
                    opPush(op)
            elif not isinstance(i,list):
                if lookup(i,scope):
                    opPush(lookup(i,scope))
                else:
                    opPush(i)
        else: 
            opPush(i)
#parses the input string and calls the recursive interpreter to solve the
#program
def interpreter(s, scope):
    tokenL = parse(tokenize(s))
    interpretSPS(tokenL,scope)

#clears both stacks
def clearBoth():
    opstack[:] = []
    dictstack[:] = []

########################################################################
####  ASSIGNMENT 5 - SSPS TESTS
########################################################################

def sspsTests():

    testinput1 = """
    /x 4 def
    /g { x stack } def
    /f { /x 7 def g } def
    f
    """

    testinput2 = """
    /x 4 def
    (static_?) dup 7 (x) putinterval /x exch def
    /g { x stack } def
    /f { /x (dynamic_x) def g } def
    f
    """

    testinput3 = """
    /m 50 def
    /n 100 def
    /egg1 {/m 25 def n} def
    /chic
    	{ /n 1 def
	      /egg2 { n stack} def
	      m  n
	      egg1
	      egg2
	    } def
    n
    chic
        """

    testinput4 = """
    /x 10 def
    /A { x } def
    /C { /x 40 def A stack } def
    /B { /x 30 def /A { x } def C } def
    B
    """

    testinput5 = """
    /x 2 def
    /n 5  def
    /A { 1  n -1 1 {pop x mul} for} def
    /C { /n 3 def /x 40 def A stack } def
    /B { /x 30 def /A { x } def C } def
    B
    """

    testinput6 = """
    /out true def 
    /xand { true eq {pop false} {true eq { false } { true } ifelse} ifelse dup /x exch def stack} def 
    /myput { out dup /x exch def xand } def 
    /f { /out false def myput } def 
    false f
    """

    testinput7 = """
    /x [1 2 3 4] def
    /A { x aload pop add add add } def
    /C { /x [10 20 30 40 50] def A stack } def
    /B { /x [6 7 8 9] def /A { x } def C } def
    B
    """

    testinput8 = """
    /x [2 3 4 5] def
    /a 10 def  
    /A { x } def
    /C { /x [a 2 mul a 3 mul dup a 4 mul] def A  a x stack } def
    /B { /x [6 7 8 9] def /A { x } def /a 5 def C } def
    B
    """

    testinput9 = """
    /x [2 3 4 5] def
    /a 9 def  
    /A { x } def
    /C { /x [a 2 mul a 3 mul dup a 4 mul] def A  a x stack } def
    /B { /x [6 7 8 9] def /A { x } def /a 5 def C } def
    B
    """

    testinput10 = """
    /x [1 2 3] def
    /A { x aload pop add add } def
    /C { /x [10 20 30 40 50] def A stack } def
    /B { /x [6 7 8 9] def /A { x } def C } def
    B
    """

    testinput11 = """
    /out true def 
    /xand { true eq {pop false} dup /x exch def stack} def 
    /myput { out dup /x exch def xand } def 
    /f { /out false def myput } def 
    false f
    """
    ssps_testinputs = [testinput1, testinput2, testinput3, testinput4, testinput5, testinput6, testinput7, testinput8, testinput9, testinput10, testinput11]
    i = 1
    for input in ssps_testinputs:
        print('TEST CASE -',i)
        i += 1
        print("Static")
        interpreter(input, "static")
        clearBoth()
        print("Dynamic")
        interpreter(input, "dynamic")
        clearBoth()
        print('\n-----------------------------')