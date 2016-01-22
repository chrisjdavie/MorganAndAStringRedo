'''
Created on 22 Jan 2016

@author: chris
'''
from os import listdir
from shutil import copy

if __name__ == '__main__':
    dirTest = 'data0/'
    dirTmp = 'dataTmp/'
    
    allFileNames = listdir(dirTest)
    for fName in allFileNames:
        
        fNameNew = fName
        if fName[:2] == 'In':
            charAdj = fName[5]
            if charAdj.isalpha():
                charNew = chr(ord(charAdj)+1)
                fNameNew = fName[:5] + charNew + fName[6:]
            
        if fName[:2] == 'Ou':
            charAdj = fName[6]
            if charAdj.isalpha():
                charNew = chr(ord(charAdj)+1)
                fNameNew = fName[:6] + charNew + fName[7:]
        
        
        copy(dirTest + fName, dirTmp + fNameNew)