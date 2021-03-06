'''
Solving this backwards from previously - race conditions (long,
repeating strings that are identical) and then add in differences,
which are much simpler.

Created on 15 Jan 2016

@author: chris
'''
class testSolverMistmatchException(Exception):
    pass

class outputString(object):
    def __init__(self):
        self.iOp = 0
        self.stringOp = []
    
    def __iadd__(self, other):
        self.stringOp += other
        return self.stringOp
    
    def append(self,other):
        self.stringOp.append(other)
        return self.stringOp
    
    def pop(self,i=-1):
        return self.stringOp.pop(i)
    
    def __str__(self):
        return self.stringOp.__str__()
    
    def __iter__(self):
        return self.stringOp.__iter__()
    
    def __len__(self):
        return self.stringOp.__len__()
    
    def __getitem__(self,*args):
        return self.stringOp.__getitem__(*args)
        
    def next(self):
        return self.stringOp.next()
    
    
class testOutputString(outputString):
    def __init__(self,testString):
        self.iOp = 0
        self.stringOp = []
        self.testString = testString
    
    def __iadd__(self, other):
        self.stringOp += other
        if self.stringOp[-1] != self.testString[len(self.stringOp)-1]:
            #print self.stringOp[-1], self.testString[len(self.stringOp)-1]
            raise testSolverMistmatchException()
        return self.stringOp
    
    def append(self,other):
        self.stringOp.append(other)
        if self.stringOp[-1] != self.testString[len(self.stringOp)-1]:
            #print self.stringOp[-1], self.testString[len(self.stringOp)-1]
            raise testSolverMistmatchException()        
        return self.stringOp
    
    
def testSolver(inputStrings, testStrings):
    output = []
    
    for stringI, stringJ, testString in zip(inputStrings[::2],inputStrings[1::2], testStrings):
        stringI = list(stringI)
        stringJ = list(stringJ)
        stringOp = testOutputString(testString)
        
        mergeStrings(stringI, stringJ, stringOp)
    
        output.append("".join(str(x) for x in stringOp))    
    
    return output       

def solver(inputStrings):
    output = []
    for stringI, stringJ in zip(inputStrings[::2],inputStrings[1::2]):
        stringI = list(stringI)
        stringJ = list(stringJ)
        stringOp = outputString()
        
        mergeStrings(stringI, stringJ, stringOp)
        
        if stringOp[-1] == 'z':
            stringOp.pop()
        
        output.append("".join(str(x) for x in stringOp))    
    
    return output

def mergeStrings(stringI, stringJ, stringOp):
    stringI.append('z')
    stringJ.append('z')
    
    i = 0
    j = 0
    
    k = 0
    while i < len(stringI) - 1 or j < len(stringJ) - 1:
        k += 1
            
        i, j = solveString(stringI, i, stringJ, j, stringOp)
        #print "".join(stringOp)
    return stringOp

def solveString(stringI,i,stringJ,j,stringOp):
    
    # two parts - if characters are equal or if they're different.
    #           - I think the part that checks if they're 
    #           - equal will have to call the part that checks if
    #           - they're different     

    if stringI[i] == stringJ[j]:
#         print "a"
        iOp, jOp = solveSame(stringI,i,stringJ,j,stringOp)
    else:
#         print "b"
        iOp, jOp = solveDiff(stringI, i, stringJ, j, stringOp)    
        
    return iOp, jOp

def solveDiff(stringI, i, stringJ, j, stringOp):
    iOp = i
    jOp = j
    try:
        if stringI[i] < stringJ[j]:
            stringOp.append(stringI[i])
            iOp += 1
        else:
            stringOp.append(stringJ[j])
            jOp += 1
    except testSolverMistmatchException:
        print iOp, jOp
        print len(stringOp)
        print "".join(stringOp[-10:])
        print "".join(stringOp.testString[len(stringOp)-10:len(stringOp)])
        print "".join(stringI[i-10:i+3])
        print "".join(stringJ[j-10:j+1])
        raise testSolverMistmatchException
        
    return iOp, jOp
    

def solveSame(stringI,i,stringJ,j,stringOp):
    
    def pullForwards(m, stringI, n, stringJ, oD):
        # this is pulling all the inds forwards
        if m < oD:
            m = oD
        elif n < oD:
            stringOp.append(stringJ[j+n])
            n += 1
        else:
            stringOp.append(stringI[i+oD])
            oD += 1
        return  m, n, oD
    
    m = 0 # last position both strings are depleted to
    n = 0 # last position one string is depleted to
    
    stringOp.append(stringI[i+n])
    oD = 1
    pD = 0
    
    # properties:     m <= p
    #                 p < n
    comparison = False
    
    char0 = stringI[i]
    
    while i + oD < len(stringI) and j + oD < len(stringJ) \
            and stringI[i+oD] == stringJ[j+oD] \
            and stringI[i+pD] >= stringI[i+oD]:
        if stringI[i+oD] <= stringI[i+pD]:
            stringOp.append(stringI[i+oD])
            oD += 1
        if stringI[i+oD] == stringI[i+pD]:
            comparison = True
            pD = 1
        
        if comparison:
            if stringI[i+pD] < stringI[i+oD]:
                drawFromFront = True
            elif stringI[i+pD] > stringI[i+oD]:
                drawFromFront = False
            else:
                comparison = True
                pD += 1
    
    
    if drawFromFront:
        print stringOp
        print oD, pD
        #oD -= pD
    
    
    
    
    if stringJ[j+oD] < stringI[i+oD]:
        minCharSide = 'j'
        minChar = stringJ[j+oD]
    else:
        minCharSide = 'i'
        minChar = stringI[i+oD]
#     
#     if drawFromFront:
#         oD -= pD
    
    
    
    if minChar > char0:
        m = oD
        
        if drawFromFront:
            stringOp += stringI[i+n+pD:i+oD-pD]
            stringOp += 2*stringI[i+oD-pD:i+oD]
        else:
            stringOp += stringI[i+n:i+oD]
        
        jOp = oD+pD
        iOp = oD+pD
        
    print oD, pD, stringOp, comparison, drawFromFront
    if minChar < char0:
        nD = oD
        mD = oD        
        if minCharSide == 'i':
            nD = n
            if comparison and drawFromFront:
                stringOp.append(stringI[i+pD])
                nD += 1
            else:
                stringOp.append(stringI[i+oD])
                mD += 1
                
        if minCharSide == 'j':
            mD = m
            if comparison and drawFromFront:
                stringOp.append(stringJ[j+pD])
                mD += 1
            else:
                stringOp.append(stringJ[j+oD])
                nD += 1
            
        iOp = mD
        jOp = nD
        
    return iOp, jOp

if __name__ == '__main__':
    inputStrings = []
    
    for _ in range(input()):
        inputStrings.append(raw_input().strip())
        inputStrings.append(raw_input().strip())
        
    output = solver(inputStrings)
    
    for o in output:
        print o
        