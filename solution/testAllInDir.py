'''
Created on 22 Jan 2016

@author: chris
'''
from os import listdir
from run import testOneFile

if __name__ == '__main__':
    dirTest = 'data1/'
    allFileNames = listdir(dirTest)
    
    inputFileNames = [ iFile for iFile in allFileNames if iFile[:2] == 'In' ]
    
    inputFileNames.sort()
    print inputFileNames
    for inputFname in inputFileNames:
        idF = inputFname[5:7]
        if idF.isalpha():
            outputFname = 'Output' + idF + '.txt'
            print inputFname
            testOneFile(dirTest + inputFname, dirTest + outputFname)