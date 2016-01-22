'''
Solving the hackerrank puzzle Morgan And A String

https://www.hackerrank.com/challenges/morgan-and-a-string

---------------------

Problem Statement

Russian | Chinese

Jack and Daniel are friends. Both of them like letters, especially upper-case ones. 
They are cutting upper-case letters from newspapers, and each one of them has their collection of letters stored in separate stacks. 
One beautiful day, Morgan visited Jack and Daniel. He saw their collections. Morgan wondered what is the lexicographically minimal string, made of that two collections. He can take a letter from a collection when it is on the top of the stack. 
Also, Morgan wants to use all the letters in the boys' collections.

Input Format

The first line contains the number of test cases, T. 
Every next two lines have such format: the first line contains string A, and the second line contains string B.

Constraints 
1≤T≤5 
1≤|A|≤105 
1≤|B|≤105 
A and B contain upper-case letters only.

Output Format

Output the lexicographically minimal string S for each test case in new line.

---------------------

This solution is wrong and will never work, it doesn't resolve strings
of the same pattern properly. See SecondGo

Created on 2 Jan 2016

@author: chris
'''
def solver(inputStrings):
    output = []
    
#     for inputString in inputStrings[:2]:
#     print inputStrings
    for stringI, stringJ in zip(inputStrings[::2],inputStrings[1::2]):
        stringI = list(stringI)
        stringJ = list(stringJ)
        
        outputString = mergeStrings(stringI, stringJ)
    
        output.append("".join(outputString))    
    
    return output
    
def getNextsubstringInds(i,j,stringI,stringJ):
    
    i1 = i
    j1 = j
    
    inspectNext = True
    while inspectNext:
        i1 += 1
        j1 += 1
        
        if stringI[i1] > stringI[i1-1] and stringJ[j1] > stringJ[j1-1]:
            
            
            iOut = i1
            jOut = j1
            inspectNext = False
        elif stringI[i1] == stringJ[i1]: # each <= previous
            inspectNext = True
        elif stringI[i1] < stringJ[j1]:
            iOut = i1 + 1
            inspectNext = False
        elif stringJ[j1] < stringI[i1]:
            jOut = j1 + 1
            inspectNext = False
    
    return iOut, jOut
    
    
def mergeStrings(stringI, stringJ):
    stringI.append('z')
    stringJ.append('z')
    
    i = 0
    j = 0
    outputString = []
    
    # This is properly hacky flow control. But, I can add a lot of
    # ugly logic to make sure this terminates correctly, and then
    # a bunch of extra logic for the exit case.
    #
    # Or, I can append a lowercase z to the list, which causes the
    # logic to extend properly to the end (as z is higher than 
    # everything else, it won't be appended until last) and then
    # have it detect the z and stop spinning.
    # 
    # so that's what I'm doing.
    while stringI[i] != 'z' or stringJ[j] != 'z':
        
        print "".join(outputString)
        print "".join(stringI[i:])
        print "".join(stringJ[j:])
        print
        
        charI = stringI[i]
        charJ = stringJ[j]
        
        if charI < charJ:
            outputString.append(charI)
            i += 1
        elif charJ < charI:
            outputString.append(charJ)
            j += 1
        else:
            i1, j1 = getNextsubstringInds(i,j,stringI,stringJ)
            outputString += stringJ[j:j1]
            j = j1
            outputString += stringJ[i:i1]
            i = i1
#     except(IndexError):
#         pass
    
    return outputString
    

if __name__ == '__main__':
    inputStrings = []
    
    for _ in range(input()):
        inputStrings.append(raw_input().strip())
        inputStrings.append(raw_input().strip())
        
    output = solver(inputStrings)
    
    for o in output:
        print o