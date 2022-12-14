#Individual Project - Kliment Lo

'''
title: Physics 30 calculator
author: Kliment Lo
date: December 13, 2022
'''

# --- INPUTS --- #
conversionUnits = {
    "a" : 0.000000000000000001,
    "f" : 0.000000000000001,
    "p" : 0.000000000001,
    "n" : 0.000000001,
    "μ" : 0.000001,
    "m" : 0.001,
    "c" : 0.01,
    "d" : 0.1,
    "da" : 10,
    "h" : 100,
    "k" : 1000,
    "M" : 1000000,
    "G" : 1000000000,
    "T" : 1000000000000
}

def readFile():
    '''
    reads the file and stores it in a variable
    :return: (list)
    '''
    file = open("universal_constant.txt")
    fileList = file.readlines()
    file.close()
    for i in range(len(fileList)):
        if fileList[i][-1] == "\n":
            fileList[i] = fileList[i][:-1]
        fileList[i] = fileList[i].split(",")
    return fileList

def menu():
    '''
    The place where the user can choose what they want to do
    :return:
    '''
    option = input("""
Please choose an option:
1. Make a calculation
2. Change universal constants
3. View calculation history  
4. Display Formula Sheet
5. Exit

> """)
    return int(option)

def chooseCalculation():
    print("hi")

# --- PROCESSING --- #

# --- OUTPUTS --- #
def intro():
    '''
    introduction to the program and what it does
    :return: (none)
    '''
    print("Welcome to the Physics 30 calculator! Choose what variable you would like to solve for, and we will do it for you!")

def formulaSheet():
    '''
    prints out the formula sheet BEAUTIFULLY
    :return: (none)
    '''
    global universalConstant
    print("""
    ----------------------------------------------------------------------------------------------------------------
    |     Kinematics                                           PHYSICS DATA SHEET                                            |
    |                                                                                                              |
    |  vₐᵥₑ = ᵈ⁄ₜ                                            Prefixes Used with SI Units                                      |
    |  aₐᵥₑ = ᵛ⁄ₜ                                                                                                  |   
    |  d = vᵢt + ½at²                                                                   |   
    |                                                                                                              |   
    |                                                                                                              |   
    |                                                                                                              |
    |                                                                                                              |
    |                                                                                                              |
    |                                                                                                              |
    |                                                                                                              |
    |                                                                                                              |      
    |                                                                                                              |     
    """)
# --- MAIN PROGRAM --- #
if __name__ == "__main__":
    universalConstant = readFile()
    print(universalConstant)
    intro()
    formulaSheet()
    choice = menu()