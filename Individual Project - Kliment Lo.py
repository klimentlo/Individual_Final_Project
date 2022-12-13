#Individual Project - Kliment Lo

'''
title: Physics 30 calculator
author: Kliment Lo
date: December 13, 2022
'''

# --- INPUTS --- #
conversionUnits = {
    "a" : 0.000000000000000000,
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
    FILE = open("universal_constant.txt")
# --- PROCESSING --- #

# --- OUTPUTS --- #


# --- MAIN PROGRAM --- #
if __name__ == "__main__":
    universalConstant = readFile(1)