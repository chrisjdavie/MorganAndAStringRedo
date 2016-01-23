'''
Hackerrank run test file

Created on 2 Jan 2016

@author: chris
'''
from src import solver, testSolver

def testOneFile(inputFname, outputFname): 
    inputStrings = []
    with open(inputFname,'rb') as f:
        for line in f:
            inputStrings.append(line.strip())
    
    testStrings = []
    with open(outputFname,'rb') as f:
        for testLine in f:
            testStrings.append(testLine.strip())
#             print len(testLine)
    print
    solverOutput = testSolver(inputStrings[1:], testStrings)
#     solverOutput = solver(inputStrings[1:])#, testStrings)
#     
#     print
#     for solverLine in solverOutput:
#         print solverLine
    
    
    with open(outputFname,'rb') as f:
        for testLine, solverLine in zip(f, solverOutput):
            testLine = testLine.strip()
            print testLine == solverLine
            if testLine != solverLine:
                for i, (charTest, charSolver) in enumerate(zip(testLine, solverLine)):
                    if charTest != charSolver:
                        print i, charTest, charSolver
                        print testLine[i-10:i+2]
                        print solverLine[i-10:i+2]
#                         print inputStrings
#                         print testLine
#                         print solverLine
                        raw_input("Press any key to continue testing")
                        break
    
if __name__ == '__main__':
    
    num = 'FG'

    inputFname  = 'data1/Input' + num + '.txt'
    outputFname = 'data1/Output'+ num + '.txt'  
    
    testOneFile(inputFname, outputFname)