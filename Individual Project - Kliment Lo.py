# Individual Project - Kliment Lo

'''
title: Physics 30 calculator
author: Kliment Lo
date: December 13, 2022
'''
import math, csv
from datetime import datetime

# --- INPUTS --- #

def readFile(FILENAME):
    '''
    reads the file and stores it in a variable
    :return: (list)
    '''
    file = open(FILENAME)
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
    if option.isnumeric():
        option = int(option)
        if option > 0 and option < 6:
            return option
        else:
            print("Please enter a valid number! ")
            return menu()
    else:
        print("Please enter a valid number! ")
        return menu()


def chooseCalculation():
    print("hi")


def selectVariable():
    '''
    user decides what variable they want to solve for
    :return: int)
    '''
    value = 1
    variable = input("""          
What variable do you want to solve for?
1. Velocity (v)
2. Initial Velocity (vᵢ)
3. Final Velocity (vբ)
4. Centripetal Velocity(v꜀)
5. Acceleration(a)
6. Centripetal Acceleration(a꜀)
7. Distance (d)
8. Time (t)

> """)
    if variable.isnumeric():
        variable = int(variable)
        if variable > 0 and variable < 9:
            return str(value), str(variable)
        else:
            print("Please enter a valid option")
            return selectVariable()
    else:
        print("Please enter a valid number! ")
        return selectVariable()


def selectEquation(unitValue):
    '''
    selects the equation of their choice
    :return:
    '''
    global numberCombination
    numberCombination = unitValue[0] + unitValue[1]  # adds the unit number and variable number, giving it its own unique number. This displays which value they want to solve for
    equationList = getEquation[numberCombination] # Use the number combination to detect what they want to solve for, which assigns the list of possible equations they can use
    print("""
Which equation would you like to use? """)
    for i in range(len(equationList)):
        print(f"{i + 1}. {equationList[i]} ") # prints out the possible formulas
        if i + 1 == len(equationList): # once it displays all the formulas. If there isn't the + 1, it'll never meet the same length. (E.g. ["Hello", "World"]. i = 1. len = 2]
            equation = input("""
> """) # selects the formula they want
            if equation.isnumeric(): # if its a number
                equation = int(equation) # make it an integer
                if equation > 0 and equation <= len(equationList): # if they chose one of the possible formulas
                    numberCombination = numberCombination + f"{equation}" # adds another number to it's unique number code
                else: # if it isnt one of the possible options
                    print("Invalid option! Select one of the equations listed above. ")
                    return selectEquation(unitValue)
            else: # if it wasn't a number in the first place
                print("Invalid option! Select one of the equations listed above. ")
                return selectEquation(unitValue)
    getVariables = getEquation[numberCombination]# Extracts the variables required to solve the formula they wanna use
    print("""IMPORTANT. Separate the numbers and units with a space! (e.g 30 cm)
    """)
    return getVariables

def getValues(missingVariables):
    '''
    Asks the user the values, and also gets the units
    :param equation: array of what the formula needs to solve for the thing
    :return: (list of values) e.g (30, 25, 13)
    '''
    global numberCombination
    unitList = []
    variables = []
    # Requesting Values
    for i in range(len(missingVariables)):  # for the length of the list of variables [Distance? ,Time? , Final Velocity? ]
        variables.append(input(f"{missingVariables[i]} "))  # it appends what the user inputted
        variables[i] = variables[i].split(" ")
        reRun = True
        unit = ""
    # Checks if formatting is Correct
        if len(variables[i]) == 2: # if they did the formatting correctly e.g("90", "cm")
            try:
                variables[i][0] = float(variables[i][0]) # try to make it a float
            except: # but if turns out its a word
                print("Please enter a number! ")
                return getValues(missingVariables) # returns to start, making them reinput the value
        # Running through the units
            for j in range(len(variables[i][-1])): # for number of letters in the unit section
                unit += variables[i][-1][j] # unit adds an additioal unit letter to it
                if reRun == True: # if it wants to rerun this
                    try:
                        if unitConversions[unit]:
                            reRun = False
                            if unit == "d" or unit == "m":
                                if unit == "d":
                                    try:
                                        unitCheck = unit + variables[i][-1][j + 1]
                                        unitList.append(unitConversions[unitCheck])
                                    except (KeyError, IndexError):
                                        unitList.append(unitConversions[unit])
                                if unit == "m":
                                    try:
                                        slash = variables[i][-1][j + 1]
                                        if slash == "/":
                                            unitList.append(1)
                                        else:
                                            unitList.append(unitConversions[unit])
                                    except IndexError:
                                        unitList.append(1)
                            else:
                                unitList.append(unitConversions[unit])
                    except KeyError:
                        if j+1 == len(variables[i][-1]):
                            print("Those were invalid units! Try again. ")
                            reRun = False
                            getValues(missingVariables)
                        pass
        else:
            print("Please include a space between the numbers and units! ")
            getValues(missingVariables)
    returnVariables = []
    for i in range(len(variables)):
        returnVariables.append(variables[i][0])
    returnVariables.append(numberCombination)
    return (unitList, returnVariables)

def trackHistory(formula, requestValues, values, time):
    '''
    Tracks the calculation history of the user
    :param formula: (str)
    :param requestValues: (list)
    :param values: 2D array
    :param time: ?????
    :return: (none)
    '''
    global historyPast

    for i in range(len(requestValues)):
        requestValues[i] = str(requestValues[i])
    requestValues = " ".join(requestValues)

    units = values[0]  # gets the units

    for i in range(len(units)):
        units[i] = str(units[i])
    units = " ".join(units)

    values = values[1][:-1]  # gets the values inputted

    for i in range(len(values)):
        values[i] = str(values[i])
    values = "".join(values)

    time = str(time)
    newHistory = ["-----------------------------------------------------", formula, requestValues, values, units, time,"-----------------------------------------------------"]
    historyList = []
    historyList.append(newHistory)
    for i in range(len(historyPast)):
        historyList.append(historyPast[i])
    print(historyList)
    FILE = open("calculation_history.csv", "w")
    for i in range(len(historyList)):

        historyList[i] = ", ".join(historyList[i]) + "\n"
        FILE.write(historyList[i])
    print(historyList)



    FILE.close()


# --- PROCESSING --- #
def solveEquation(equation):
    '''
    Solves the equations
    :param equation: (list).
    :return:
    '''
    print(equation)
    for i in range(len(equation[0])):
        equation[1][i] = equation[0][i] * equation[1][i]
    answer = actuallySolveIt(equation[1])
    print(answer)

def actuallySolveIt(variable):
    '''
    looks for the formula that the user wants to use, and plugs in the numbers
    :param variable: (list)
    :return: (float)
    '''
    for i in range(len(variable)-1):
        variable[i] = float(variable[i])

    if len(variable) == 3:
        getFormula1 = {
            # Velocity
            "111": variable[0] / variable[1],
            "112": variable[0] * variable[1],
            # Centripetal Velocity
            "141": (2 * math.pi * variable[0] / variable[1]),
            # Acceleration
            "151": variable[0] / variable[1],
            # Centripetal Acceleration
            "161": variable[0] ** 2 / variable[1],
            "162": 4 * (3.1415926535 ** 2) * variable[0] / variable[1],
            # Time
            "181": variable[1] / variable[0],
            "182": variable[1] / variable[0],

        }
        answer = getFormula1[variable[-1]]

    if int(len(variable)) == 4:
        getFormula2 = {
            # Initial Velocity
            "121": (variable[0] - 0.5 * variable[2] * variable[1] ** 2) / variable[1],
            "122": (variable[0] - 2 * variable[1] * variable[2]),
            "123": (variable[0] / variable[2] * 2 - variable[1]),
            # Final Velocity
            "131": (variable[0] - 0.5 * variable[2] * variable[1] ** 2) / variable[1],
            "132": (variable[0] / variable[2] * 2 - variable[1]),
            "133": (variable[0] ** 2 + 2 * variable[1] * variable[2]),
            #Distance
            "171": variable[0] * variable[1] + 0.5 * variable[2] * variable[1] ** 2,
            "172": variable[0] * variable[1] - 0.5 * variable[2] * variable[1] ** 2,
            "173": ((variable[0] + variable[1]) / 2) / variable[2],
            "174": (variable[0] - variable[1] ** 2) / (2 * variable[2]),
            #Time
            "183": variable[1] ** 2 - (2 * variable[2] * variable[0]),
            "184": variable[1] ** 2 - (2 * variable[2] * variable[0]),
            "185": variable[0] / ((variable[1] + variable[2]) / 2)
        }
        answer = getFormula2[variable[-1]]
        print(f"Answer: {answer}")
        if variable[-1] == "122":
            if answer < 0:
                answer = answer * -1
                print("Replace me with a thing indicating it's south or something")
            answer = math.sqrt((answer))
        if variable[-1] == "183" or variable[-1] == "184":
            try:
                answer1 = (-variable[1] + math.sqrt(answer)) / variable[2]
                answer2 = (-variable[1] - math.sqrt(answer)) / variable[2]
                print(f"Answer 1: {answer1}")
                print(f"Answer 2: {answer2}")
            except ValueError:
                print("That's Not possible little boy :)")
    return answer


# --- OUTPUTS --- #
def intro():
    '''
    introduction to the program and what it does
    :return: (none)
    '''
    print(
        "Welcome to the Kinematics Calculator! Choose what variable you would like to solve for, and we will do it for you! You can input any type of unit, and it will print it out into the regular one")


def formulaSheet():
    '''
    prints out the formula sheet BEAUTIFULLY
    :return: (none)
    '''
    global universalConstant
    print("""
    ---------------------------------------------------------------------------------------------------------------------------------------------------
    | EQUATIONS                                                                                                                                       |
    |                                                                                                                                                 |
    |             Kinematics                                           Waves                                 Atomic Physics                           |
    |                                                                                                                                                 |
    |  vₐᵥₑ = △d/△t        d = vբt - ½at²               T = 2π√(m/k)     m = hᵢ/hₒ = -dᵢ/dₒ            W = hf₀         E = hf = (hc)/λ                  |
    |  aₐᵥₑ = △v/△t        d = [(vբ + vᵢ) / 2]t         T = 2π√(l/g)     1/f = 1/dₒ + 1/dᵢ           Eₖmax = qₑVₛₜₒₚ     N = N₀(½)ⁿ                        |                     
    |  d = vᵢt + ½at²     vբ = vᵢ² + 2ad               T = (1/f)        n₂/n₁ = sin0₁/sin0₂                                                           |
    | |v꜀|=  2πr/T        |a꜀| = v²/r = (4π²r)/T²       v = fλ           n₂/n₁ = v₁/v₂ = λ₁/λ₂      Quantum Mechanics and Nuclear Physics              |         
    |                                                  f = v/(v±vₛ)fₛ     λ = [d(sin0)]/n                                                               |
    |             Dynamics                                               λ = xd/nl                  △E = △mc²     E = pc                              |
    |                                                                                               p = h/λ       △λ = h/(mc) (1 - cos0)              |
    |     a = Fₙₑₜ / m     |Fᵍ| = (Gm₁m₂)/r²                                                                                                            |
    |                                                                                                       Trigonometry and Geometry                 |
    |    |Fբ| = μ|Fₙ|     |g| = (Gm)/r²                                                                                                               |
    |     Fₛ = -kx        g = Fᵍ/m                                                                sin0 = opposite/hypotenuse      Line                |
    |                                                       Electricity and Magnetism            cos0 = adjacent/hypotenuse       m = △y/△x           |
    |        Momentum and Energy                                                                 tan0 = opposite/adjacent         y = mx+b            |
    |                                                   |Fₑ| = (kq₁q₂)/r²      △V = △E/q          c² = a² + b²                                        |
    |    p = mv              Eₖ = ½mv²                  |E| = (kq)/ r²         I = q/t           a/(sinA) = b/(sinB) = c(sinC)    Area                | 
    |    F△t = m△v           Eₚ = mgh                    E = Fₑ/q               |Fₘ| = Il|B|        c² = a² + b² - 2ab cos C         Rectangle = lw    |
    |    W = |F||d|cos0      Eₚ = ½kx²                  |E| = △V/△d           |Fₘ| = qv|B|                                          Triangle = ½ab    |  
    |    W = △E                                                                                                                    Circle = πr²      |
    |    P = W/t                                                                                                                   Circle = 2πr      |
    |                                                                                                                                                |
    --------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                

    """)
    menu = input("Press enter to return to menu. ")


### --- DICTIONARY --- ###

unitConversions = {
    "a": 0.000000000000000001,
    "f": 0.000000000000001,
    "p": 0.000000000001,
    "n": 0.000000001,
    "μ": 0.000001,
    "m": 0.001,
    "c": 0.01,
    "d": 0.1,
    "da": 10,
    "h": 100,
    "k": 1000,
    "M": 1000000,
    "G": 1000000000,
    "T": 1000000000000,
    "s": 1,
}

getEquation = {
    # What the numbers mean: (unit) (Variable they want to solve) (chosen equation) (e.g 112, (kinematics)(velocity)(aₐᵥₑ = △v/△t)
    # Velocity
    "11": ["vₐᵥₑ = △d/△t", "aₐᵥₑ = △v/△t"],
    # Initial Velocity
    "12": ["d = vᵢt + ½at²", "vբ = vᵢ² + 2ad", "d = [(vբ + vᵢ) / 2]t"],
    # Final Velocity
    "13": ["d = vբt - ½at² ", "d = [(vբ + vᵢ) / 2]t", "vբ = vᵢ² + 2ad"],
    # Centripetal Velocity
    "14": ["|v꜀|=  2πr/T"],
    # Acceleration
    "15": ["aₐᵥₑ = △v/△t"],
    # Centripetal Acceleration
    "16": ["|a꜀| = v²/r", "|a꜀|= (4π²r)/T²"],
    # Distance
    "17": ["d = vᵢt + ½at²", "d = vբt - ½at²", "d = [(vբ + vᵢ) / 2]t", "vբ = vᵢ² + 2ad"],
    # Time
    "18": ["vₐᵥₑ = △d/△t", "aₐᵥₑ = △v/△t", "d = vᵢt + ½at", "d = vբt - ½at²", "d = [(vբ + vᵢ) / 2]t"],
    ### Gets the actual equation, like the one we will use to help calculate their result
    # Velocity
    "111": ["Distance? ", "Time? "],
    "112": ["Acceleration?", "Time? "],
    # Initial Velocity
    "121": ["Distance? ", "Time? ", "Acceleration? "],
    "122": ["Final Velocity? ", "Acceleration? ", "Distance? "],
    "123": ["Distance? ", "Final Velocity? ", "Time? "],
    # Final Velocity
    "131": ["Distance? ", "Time? ", "Acceleration? "],
    "132": ["Distance? ", "Initial Velocity? ", "Time? "],
    "133": ["Initial Velocity? ", "Acceleration? ", "Distance? "],
    # Centripetal Velocity
    "141": ["Radius? ", "Period? "],
    # Acceleration
    "151": ["Velocity? ", "Time? "],
    # Centripetal Acceleration
    "161": ["Velocity? ", "Radius? "],
    "162": ["Radius? ", "Period? "],
    # Distance
    "171": ["Initial Velocity? ", "Time? ", "Acceleration? "],
    "172": ["Final Velocity? ", "Time? ", "Acceleration? "],
    "173": ["Final Velocity? ", "Initial Velocity? ", "Time? "],
    "174": ["Final Velocity? ", "Initial Velocity? ", "Acceleration? "],
    # Time
    "181": ["Velocity? ", "Distance? "],
    "182": ["Acceleration? ", "Velocity"],
    "183": ["Distance? ", "Initial Velocity", "Acceleration? "],
    "184": ["Distance? ", "Final Velocity? ", "Acceleration? "],
    "185": ["Distance? ", "Final Velocity? ", "Initial Velocity? "]
}

# --- MAIN PROGRAM --- #
if __name__ == "__main__":
    universalConstant = readFile("universal_constant.txt")
    historyPast = readFile("calculation_history.csv")
    # print(universalConstant)
    intro()
    while True:
        option = menu()
        if option == 1:
            choice = selectVariable()  # returns a tuple, where the first thing identifies the unit it's from, and the second thing identifies the variables
            print(f"Choice: {choice}")
            equation = selectEquation(choice)
            print(numberCombination)
            print(f"Equation: {equation}")
            values = getValues(equation)
            print(f"Values: {values}")
            solveEquation(values)
            time = datetime.now()
            print(f"Time: {time}")
            trackHistory(numberCombination, equation, values, time)
        if option == 2:
            pass
        if option == 3:
            pass
        if option == 4:
            formulaSheet()
        if option == 5:
            exit()