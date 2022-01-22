CDCdata = {'King':{'Mar':2706,'Apr':3620,'May':1860,'Jun':2157,'July':5014,'Aug':4327,'Sep':2843}, 'Pierce':{'Mar':460,'Apr':965,'May':522,'Jun':647,'July':2470,'Aug':1776,'Sep':1266}, 'Snohomish':{'Mar':1301,'Apr':1145,'May':532,'Jun':568,'July':1540,'Aug':1134,'Sep':811}, 'Spokane':{'Mar':147,'Apr':222,'May':233,'Jun':794,'July':2412,'Aug':1530,'Sep':1751}, 'Whitman' : {'Apr':7,'May':5,'Jun':19,'July':51,'Aug':514,'Sep':732, 'Oct':278} }
def getNumCases(data,counties,months):
    """
    case = 0
    monthDic = {}
    for i in range(len(counties)):
        monthDic = counties[i]
        for counties[i] in data.items():
            for j in range(len(months)):
                for months[i] in monthDic:
                    case += monthDic[months[j]]
    return case
    """
    """
    case = {}
    for counties, monthsdic, in data.items():
        for months, caseNum in monthsdic.items():
            case[months] = case.get(months,0) + caseNum
    return case
    """
    case={}
    total = 0
    for i in range(0,len(counties)):
        for counties[i], monthDic in data.items():
            for j in range(0,len(months)):
                for months[j], amount in monthDic.items():
                    case[months[j]] = case.get(months[j],0) + amount

    return case
            


    
getNumCases(CDCdata,['Whitman'],['Apr','May','Jun'])
getNumCases(CDCdata,['Pierce'],['Apr','May','Jun'])
#getNumCases(CDCdata,['King','Pierce'],['July','Aug'])

def adduptoZero(L,n):
    lis = []
    totlist = []
    for i in range(0,len(L)-(n-1)):
        n = n-1
        if (L[i] + adduptoZero(L,n) == 0):
            lis.append(L[i])
    return totlist

def adduptoZero(L,n):
     lis = []
     totlist = []
     for i in range(0,len(L)-2):
          for j in range(i+1,len(L)-1):
               for k in range(j+1,len(L)):
                    #for m in range(k+1,n):
                    if(L[i]+L[j]+L[k]==0):
                         lis = lis.append(L[i])
                         lis = lis.append(L[j])
                         lis = lis.append(L[k])
                         #lis = lis.append(L[m])
                         totlist.append(lis)
     return totlist

def getNumCases(data,counties,months):
    case = 0
    for key, value in data.items():
        if key in counties:
            for k,v in value.items():
                for index in months:
                    if index in k:
                        case += v
                        
    return case

from itertools import combinations
def adduptoZero(L,n):
    totallist=[]
    lis = list(combinations(L,n))
    for i in lis:
        if sum(i)==0:
            totallist.append(i)
    return totallist