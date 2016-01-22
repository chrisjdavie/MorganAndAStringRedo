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
            print self.stringOp[-1], self.testString[len(self.stringOp)-1]
            raise testSolverMistmatchException()
        return self.stringOp
    
    def append(self,other):
        self.stringOp.append(other)
        if self.stringOp[-1] != self.testString[len(self.stringOp)-1]:
            print self.stringOp[-1], self.testString[len(self.stringOp)-1]
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
        print "".join(stringOp)
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
        print iOp, jOp
        print len(stringOp)
        print "".join(stringOp[-10:])
        print "".join(stringOp.testString[len(stringOp)-10:len(stringOp)])
        print "".join(stringI[i-10:i+3])
        print "".join(stringJ[j-10:j+1])
        raise testSolverMistmatchException
        
    return iOp, jOp
    

def solveSame(stringI,i,stringJ,j,stringOp):
    
    m = 0 # last position both strings are depleted to
    n = 1 # front position being examined
    p = 0 # last position one string is depleted to
    
    # properties:     m <= p
    #                 p < n
    
    stillSame = True
    while i + n < len(stringI) and j + n < len(stringJ) and stillSame:
        
        print
        print stringI[n]
        print p, m, n#, i+n, len(stringI)
        print stringOp
        
        if stringI[i+n] == stringJ[j+n]:
            
            if stringI[i+n] > stringI[i+m]:
                print "foo"
    #             print stringOp, stringI[i+n], stringI[i+p:i+n]
                stringOp += stringI[i+p:i+n] + stringI[i+m:i+n]
                p = n
                m = n
                n += 1
                
            elif stringI[i+n] > stringI[i+p] and stringI[i+p] < stringI[i+m]:
                stringOp += [stringI[i+p]]
                p += 1
            
            elif stringI[i+n] == stringI[i+p] and n != p:
                print "bar"
                stringOp += [ stringI[i+p] ]
                p += 1
                n += 1
                
            elif (stringI[i+n] < stringI[i+p]):
                n += 1
        else:
            stillSame = False
#             print p, n, m
            try:
                stringOp += stringI[i+p:i+n]
            except testSolverMistmatchException:
                print i+p, i+n
#                 print len(stringOp)
#                 raise testSolverMistmatchException
                
            if stringI[i+n] < stringJ[j+n]:
                if stringI[i+n] >= stringI[i+m]:
                    stringOp += stringJ[j+m:j+n]
                    jOp = j + n
                else:
                    jOp = j + m
                stringOp += [stringI[i+n]]
                iOp = i + n + 1
                
            if stringJ[j+n] < stringI[i+n]:
                if stringJ[j+n] >= stringJ[j+m]:
                    stringOp += stringI[i+m:i+n]
                    iOp = i + n
                else:
                    iOp = i + m 
                stringOp += [stringJ[j+n]]
                jOp = j + n + 1
         
        print stringOp
        print p, m, n
        
    if stillSame:
        iOp = i + n
        jOp = j + n
    
#     print
#     print stringI, iOp
#     print stringJ, jOp
#     print stringOp
#     print
#         print p, m, n, len(stringI)
#         print stringOp
    
    return iOp, jOp

if __name__ == '__main__':
    inputStrings = []
    
    for _ in range(input()):
        inputStrings.append(raw_input().strip())
        inputStrings.append(raw_input().strip())
        
    output = solver(inputStrings)
    
    for o in output:
        print o
        