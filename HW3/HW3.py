# CptS 355 - Fall 2020 - Assignment 3
# Please include your name and the names of the students with whom you discussed any of the problems in this homework
from itertools import combinations
import itertools

debugging = False
def debug(*s): 
     if debugging: 
          print(*s)

## problem 1-a) getNumCases - 10%
def getNumCases(data,counties,months):
     """
     for counties, monthsdic, in data.items():
          for months, caseNum in monthsdic.items():
               case[months] = case.get(months,0) + caseNum
     return case
     """
     case = 0
     for key, value in data.items():
          if key in counties:
               for k,v in value.items():
                    for month in months:
                         if month in k:
                              case += v
                         
     return case

## problem 1-b) getMonthlyCases - 15%
from functools import reduce
def getMonthlyCases(data):
     newdata = dict([(value,(v,k)) for v,(value,k) in data.items()])
     return newdata

## problem 1-c) mostCases - 15%
def mostCases(data):
     case = {}
     for counties, monthsdic, in data.items():
          for months, caseNum in monthsdic.items():
               case[months] = case.get(months,0) + caseNum
     return max(case.values())
     
## problem 2a) searchDicts(L,k) - 5%
def searchDicts(L,k):
     count = 0
     i = -1 # starts at end
     while count < len(L):
          if L[i].get(k,None) is None:
               i -= 1
               count += 1
          else:
               return L[i].get(k,None)

## problem 2b) searchDicts2(L,k) - 10%
def searchDicts2(tp, k):
    size = len(tp) - 1
    return nextIndex(tp,k,size)

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

## problem 3 - adduptoZero - 10%
from itertools import combinations
def adduptoZero(L,n):
    totallist=[]
    lis = list(combinations(L,n))
    for i in lis:
        if sum(i)==0:
            totallist.append(i)
    return totallist
          
     
## problem 4 - getLongest - 10%
def getLongest(L):
     return max(openlist(L),key=len)

def openlist(L):
     openlis=[]
     for val in L:
          if isinstance(val,list):
               openlis.extend(openlist(val))
          else:
               openlis.append(val)
     return openlis
## problem 5 - apply2nextN - 20% 
class apply2nextN():
     def __init__(self, func, coun, seq: iter):
          if not hasattr(seq, '__iter__'):
               raise Exception("Invalid parameter, provide only iterator type")
          self._seq = seq
          self._c = coun
          self._f = func
     def __iter__(self):
          return self
     def __next__(self):
          j=0
          ls=[]
          for i in range(0,len(self._c)):
               self._seq += next(self._seq)
               j += 1
          for k in range(j,len(self._c)):
               ls.append(self._c[k])
          
          