'''
So this one uses two indicies in the repeated strings case. I finally
twigged that the complication is that in these running strings,
if the end is the same as the beginning, either can be used, so 
the front needs to be compared to the end.

It's obvious now I see it, and the code is quite simple really.

The testing classes and exceptions were to allow me to find where 
the errors occured in the strings, as soon as new characters were
added it checked they were valid.

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
        
        if len(self.stringOp) > len(self.testString) or \
                self.stringOp[-1] != self.testString[len(self.stringOp)-1]:
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
        print "a"
        iOp, jOp = solveSame(stringI,i,stringJ,j,stringOp)
    else:
        print "b"
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
        print len(stringI), len(stringJ)
        print len(stringOp.testString)
        print iOp, jOp
        print len(stringOp)
        print stringI, stringJ[jOp]
#         print "".join(stringOp[-10:])
#         print "".join(stringOp.testString[len(stringOp)-10:len(stringOp)])
#         print "".join(stringI[i-10:i+3])
#         print "".join(stringJ[j-10:j+1])
        exit()
        
    return iOp, jOp
    

def solveSame(stringI,i,stringJ,j,stringOp):
    
    try:
        stringOp.append(stringI[i])
    except testSolverMistmatchException:
        print "".join(stringOp[-10:])
        print "".join(stringOp.testString[len(stringOp)-10:len(stringOp)])
        print "".join(stringI[i-10:i+2])
        print "".join(stringJ[j-10:j+2])
        print i, j
        exit()
        
        
    oD = 1
    pD = 0
    
    char0 = stringI[i]
    comparison = False
    
    while i + oD < len(stringI) and j + oD < len(stringJ) \
            and stringI[i+oD] == stringJ[j+oD] \
            and stringI[i+pD] >= stringI[i+oD]:
        if stringI[i+oD] <= stringI[i+pD]:
            stringOp.append(stringI[i+oD])
            oD += 1
        
        if comparison:
            pD += 1
        
        if stringI[i+oD] == stringI[i]:
            comparison = True
            pD = 0
    
    
    if stringJ[j+oD] < stringI[i+oD]:
        minCharSide = 'j'
        minChar = stringJ[j+oD]
    else:
        minCharSide = 'i'
        minChar = stringI[i+oD]
    
    
    if minChar > char0:
        stringOp += stringI[i+pD:i+oD-pD]
        stringOp += 2*stringI[i+oD-pD:i+oD]
        
        iOp = i + oD
        jOp = j + oD
        
    if minChar <= char0:
        if stringI[i+pD] < minChar:
            stringOp.append(stringI[i+pD])
            oD += 1
            pD += 1
        elif stringI[i+pD] > minChar:
            stringOp.append(minChar)
            oD += 1
            pD = 0
        else:
            pD = 0
        
        print minCharSide, pD, oD
        if minCharSide == 'i':
            jOp = j + pD
            iOp = i + oD - pD
        else:
            iOp = i + pD
            jOp = j + oD - pD
    
    print stringOp, minChar
    print stringI, stringJ
    print iOp, jOp
    
#     exit()
#     
    return iOp, jOp

if __name__ == '__main__':
    inputStrings = []
    
    for _ in range(input()):
        inputStrings.append(raw_input().strip())
        inputStrings.append(raw_input().strip())
        
    output = solver(inputStrings)
    
    for o in output:
        print o
        