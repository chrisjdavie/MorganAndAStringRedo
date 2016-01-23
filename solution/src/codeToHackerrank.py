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
    if stringI[i] < stringJ[j]:
        stringOp.append(stringI[i])
        iOp += 1
    else:
        stringOp.append(stringJ[j])
        jOp += 1
            
    return iOp, jOp
    

def solveSame(stringI,i,stringJ,j,stringOp):
    
    stringOp.append(stringI[i])
    
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
#         
#         print minCharSide, pD, oD
        if minCharSide == 'i':
            jOp = j + pD
            iOp = i + oD - pD
        else:
            iOp = i + pD
            jOp = j + oD - pD
#     
#     print stringOp, minChar
#     print stringI, stringJ
#     print iOp, jOp
#     
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