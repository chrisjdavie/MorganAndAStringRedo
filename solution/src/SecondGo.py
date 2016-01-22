'''
Solving the hackerrank puzzle Morgan And A String

There's a number of possible cases when dealing with a strings that
have the same patterns. There are simple cases, but the general case,
with the same, repeated pattern, needs to be treated carefully.

Also, this can be done linearly, and any solution that backtracks 
will take much more time than that. It doesn't need to backtrack,
I don't think, so I'm thinking hard about all the cases. I think 
there are maybe 10, but I have to be careful.


Memory and recursion notes:

I'm not passing substrings, just references to the original objects.
This code is going to be pretty recursive, so I'm hoping if I store
just a few ints in each recursion layer, I won't hit the limit.

I'm not sure I know how to this any other way than recursively.

Created on 2 Jan 2016

@author: chris
'''
def solver(inputStrings):
    output = []
    
    for stringI, stringJ in zip(inputStrings[::2],inputStrings[1::2]):
        stringI = list(stringI)
        stringJ = list(stringJ)
        
        outputString = mergeStrings(stringI, stringJ)
    
        output.append("".join(outputString))    
    
    return output

def mergeStrings(stringI, stringJ):
    stringI.append('z')
    stringJ.append('z')
    stringOp = []
    
    i = 0
    j = 0
    
    k = 0
    while stringI[i] != 'z' or stringJ[j] != 'z':
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
    
def solveDiff(stringI,i,stringJ,j,stringOp):
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
    # as we don't know if we're going to increment i or j yet,
    # we keep m and n - m is the earliest offset not yet examined, n is
    # point where we're currently examining
     
    m = 0
    n = 1
    p = 0
    print
    repeatConsiderations = False
    inspectNext = True
    while inspectNext:
        print stringI[i+n], i, j, n, p, "".join(stringOp)
        
        if stringI[i+n] == stringJ[j+n]:
            
            if (stringI[i+n] == stringI[i+p]):
                stringOp += [ stringI[p] ]
                p += 1
                n += 1
                repeatConsiderations = True            
            elif repeatConsiderations:
                if (stringI[i+n] > stringI[i+p]):
                    stringOp += [stringI[p]] + stringI[i+m:i+n]
                    p += 1
                    m = p
                elif (stringI[i+n] < stringI[i+p]):
                    stringOp += [stringI[p]] + stringI[i+m:i+p]
                    p += 1
                    m = p
                if n == p:
                    repeatConsiderations = False
            else:
                if (stringI[i+n] > stringI[i+m]):
                    inspectNext = False
                    stringOp += stringI[i+m:i+n] + stringI[i+m:i+n]
                    iOp = i+n
                    jOp = j+n
                    n += 1
                elif (stringI[i+n] < stringI[i+m]):
                    n += 1            
            
                
#             if (lotsIdentical and stringI[i+n] == stringI[i+m]):
#                 continue
#             else:
#                 lotsIdentical = False
#                 if n > 1:
#                     inspectNext = False
#                     stringOp += stringI[i:i+n] + stringI[i:i+n]
#                     iOp = i+n
#                     jOp = j+n
#                     continue
#             
#             if (stringI[i+n] > stringI[i+m]):
#                 inspectNext = False
#                 stringOp += stringI[i:i+n] + stringI[i:i+n]
#                 iOp = i+n
#                 jOp = j+n
#                 n += 1
#                 continue
#             if (stringI[i+n] < stringI[i+m]):
#                 n += 1
#                 continue

#                 stringOp += stringI[i:i+n] + [stringI[i+m]]
#                 iOp, jOp = solveString(stringI, m, stringI, n, stringOp)
                
                
        else:
            inspectNext = False
            stringOp += stringI[i:i+n]
            if stringI[i+n] < stringJ[j+n]:
                iOp, jOp = solveDiff(stringI, i+n, stringJ, j+m, stringOp)
            else:
                iOp, jOp = solveDiff(stringI, i+m, stringJ, j+n, stringOp)
    
    print "".join(stringOp)  
          
    return iOp, jOp
    
    
if __name__ == '__main__':
    inputStrings = []
    
    for _ in range(input()):
        inputStrings.append(raw_input().strip())
        inputStrings.append(raw_input().strip())
     
    output = solver(inputStrings)
    
    for o in output:
        print o