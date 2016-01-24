'''
This is a simplification of fifth go

Created on 22 Jan 2016

@author: chris
'''


def solver(inputStrings):
    output = []
    for stringI, stringJ in zip(inputStrings[::2],inputStrings[1::2]):
        stringI = list(stringI)
        stringJ = list(stringJ)
        stringOp = []
        
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
    return stringOp

def solveString(stringI,i,stringJ,j,stringOp):
    
    # two parts - if characters are equal or if they're different.
    #           - I think the part that checks if they're 
    #           - equal will have to call the part that checks if
    #           - they're different     

    if stringI[i] == stringJ[j]:
        iOp, jOp = solveSame(stringI,i,stringJ,j,stringOp)
    else:
        iOp, jOp = solveDiff(stringI, i, stringJ, j, stringOp)    
        
    return iOp, jOp

def solveDiff(stringI, i, stringJ, j, stringOp):
    iOp = i
    jOp = j
    if stringI[i] < stringJ[j]:
        stringOp.append(stringI[i])
        iOp += 1
    else:
        stringOp.append(stringJ[j])
        jOp += 1
            
    return iOp, jOp
    


def solveSame(stringI,i,stringJ,j,stringOp):
    
#     try:
#         stringOp.append(stringI[i])
#     except testSolverMistmatchException:
#         print "solveSame a"
# #         print "".join(stringOp[-10:])
# #         print "".join(stringOp.testString[len(stringOp)-10:len(stringOp)])
# #         print "".join(stringI[i-10:i+2])
# #         print "".join(stringJ[j-10:j+2])
#         print i, j
#         exit()
        
        
    oD = 1
    pD = 0
    
    char0 = stringI[i]
    comparison = False
    if stringI[i+oD] != stringI[i+pD]:
        rerunGap = True
    else:
        rerunGap = False
    
    while i + oD < len(stringI) and j + oD < len(stringJ) \
            and stringI[i+oD] == stringJ[j+oD] \
            and stringI[i+pD] >= stringI[i+oD]:
        
        if stringI[i+oD] <= stringI[i+pD]:
#             stringOp.append(stringI[i+oD])
            oD += 1
        
        if comparison:
            pD += 1

        if stringI[i+oD] != stringI[i+pD]:
                rerunGap = True            
        
        if stringI[i+oD] == stringI[i] and rerunGap:
            comparison = True
            rerunGap = False
            pD = 0
    
    
    if stringJ[j+oD] < stringI[i+oD]:
        minCharSide = 'j'
        minChar = stringJ[j+oD]
    else:
        minCharSide = 'i'
        minChar = stringI[i+oD]
    
    if minChar > char0:
#         print oD, pD
        if pD == 0 or oD - pD == pD:
            stringOp += 2*stringI[i:i+oD]
            iOp = i + oD
            jOp = j + oD            
            
        else:
            drawFromFront = None
            lD = oD
            for K in range(0,pD):
                mD = pD + K
                lD = oD - pD + K
                
                if stringI[i+mD] > stringI[i+lD]:
                    drawFromFront = False
                    break
                elif stringI[i+mD] < stringI[i+lD]:
                    drawFromFront = True
                    break
            else:
#                 stringOp.pop()
                lD = oD
            
            if drawFromFront != None:
                if drawFromFront:
                    stringOp += stringI[i:i+oD-pD]
                    stringOp += stringI[i:i+pD]
                    iOp = i + oD-pD
                    jOp = j + pD          
                    
                else:
#                     print minChar, char0
#                     print i, j
#                     print oD, pD
#                     print "".join(stringI[i:i+oD])
#                     print "".join(stringJ[j:j+oD])
#                     print "".join(2*stringI[i:i+oD])
                    stringOp += 2*stringI[i:i+oD]
                    iOp = i + oD
                    jOp = j + oD  
            else:
                stringOp += 2*stringI[i:i+oD-pD]
                stringOp += 2*stringI[i+oD-pD:i+oD]
                
                iOp = i + oD
                jOp = j + oD    
                
        
        
    if minChar <= char0:
        if stringI[i+pD] < minChar:
            oD += 1
            pD += 1
        elif stringI[i+pD] > minChar:
            oD += 1
            pD = 0
        else:
            pD = 0
 
        if minCharSide == 'i':
            jOp = j + pD
            iOp = i + oD - pD
            stringOp += stringI[i:iOp]
            stringOp += stringJ[j:jOp]
        else:
            iOp = i + pD
            jOp = j + oD - pD
            stringOp += stringJ[j:jOp]
            stringOp += stringI[i:iOp]
    
    return iOp, jOp


if __name__ == '__main__':
    inputStrings = []
    
    for _ in range(input()):
        inputStrings.append(raw_input().strip())
        inputStrings.append(raw_input().strip())
        
    output = solver(inputStrings)
    
    for o in output:
        print o