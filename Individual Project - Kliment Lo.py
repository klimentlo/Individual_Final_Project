# Individual Project - Kliment Lo

'''
title: Physics 30 calculator
author: Kliment Lo
date: December 13, 2022
'''
import math
from datetime import datetime

# --- INPUTS --- #

def readFile(FILENAME):
    '''
    reads the file and stores it in a variable
    :return: (list)
    '''
    if FILENAME == "decimalPlaceFile.txt":
        try:
            file = open(FILENAME, "x")
            file.write("2")
            file.close()
            fileList = 2
        except FileExistsError:
            file = open(FILENAME)
            fileList = file.read()
            fileList = int(fileList)
            file.close()
    else:
        try:
            file = open(FILENAME, "x")
            file.close()
            fileList = []
        except FileExistsError:
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
Please select one of the following:
1. Make a Calculation
2. Select Decimal Places
3. View Calculation History  
4. Display Formula Sheet
5. Display Unit Conversion Sheet
6. Exit
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
    global numberCombination, answerUnits
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

    answerUnits = getVariables[-1]

    return getVariables[:-1]

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
       userInput = checkValues(missingVariables[i])
       unitList.append(userInput[1])
       variables.append(userInput[0])


   returnVariables = []
   for i in range(len(variables)):
       returnVariables.append(variables[i])
   returnVariables.append(numberCombination)
   return (unitList, returnVariables)



def checkValues(missingVariables):
   variables = input(f"{missingVariables} ")  # it appends what the user inputted
   variables = variables.split(" ")
   unit = ""
   reRun = True
   # Checks if formatting is Correct
   if len(variables) == 2:  # if they did the formatting correctly e.g("90", "cm")
       try:
           variables[0] = float(variables[0])  # try to make it a float
       except:  # but if turns out its a word
           print("Please enter a number! ")
           return checkValues(missingVariables)  # returns to start, making them re input the value
       if missingVariables == "Time? " or missingVariables == "Period? ":
           variables[-1] = variables[-1].title()
           try:
               if unitConversionsTime[variables[-1]]:
                    returnUnit = unitConversionsTime[variables[-1]]
               else:
                   print("Doesn't Match :( ")
           except KeyError:
               print("Those were invalid units! Try again. ")
               return checkValues(missingVariables)

       elif missingVariables == "Distance? ":
           try:
               if unitConversionsDistance[variables[-1]]:
                    print("hi")
                    returnUnit = unitConversionsDistance[variables[-1]]
               else:
                   print("Doesn't Match :( ")
           except KeyError:
               print("Those were invalid units! Try again. ")
               return checkValues(missingVariables)

       elif missingVariables == "Velocity? " or missingVariables == "Initial Velocity? " or missingVariables == "Final Velocity? " or missingVariables == "Acceleration":
           variables[-1] = variables[-1].split("/")
           if len(variables[-1]) == 2:
               print(variables[-1][0])
               returnUnit = []
               try:
                    returnUnit.append(unitConversionsDistance[variables[-1][0]])
               except KeyError:
                   print("That is an invalid distance! Try again. ")
                   return checkValues(missingVariables)
               try:
                    variables[-1][1] = variables[-1][1].title()
                    print(variables[-1][1])
                    returnUnit.append(unitConversionsTime[variables[-1][1]])
               except KeyError:
                   print("That is an invalid time! Try again. ")
                   return checkValues(missingVariables)
           else:
               print("Please only use one slash!")
               return checkValues(missingVariables)


           if missingVariables == "Acceleration? ":
               pass


   else:
       print("Please include a space between the number and the units! ")
       return checkValues(missingVariables)
   return variables[0], returnUnit


def trackHistory(formula, requestValues, values, time, answer, roundedAnswer):
    '''
    Tracks the calculation history of the user
    :param formula: (str)
    :param requestValues: (list)
    :param values: 2D array
    :param time: ?????
    :return: (none)
    '''
    global historyPast, answerUnits
    for i in range(len(requestValues)):
        requestValues[i] = str(requestValues[i])
    requestValues = "".join(requestValues)

    units = values[0]  # gets the units

    for i in range(len(units)):
        units[i] = str(units[i])
    units = " ".join(units)
    print(f"Units: {units}")

    values = values[1][:-1]  # gets the values inputted
    for i in range(len(values)):
        values[i] = str(values[i])
    values = " ".join(values)
    time = str(time)
    answer = str(answer)
    roundedAnswer = str(roundedAnswer)
    newHistory = ["-----------------------------------------------------",time,formula,requestValues,values,units, answer, roundedAnswer, answerUnits, "-----------------------------------------------------"]
    historyList = []

    for i in range(len(historyPast)):
        historyList.append(historyPast[i])
    historyList.append(newHistory)
    FILE = open("calculation_history.txt", "w")
    for i in range(len(historyList)):
        historyList[i] = ",".join(historyList[i]) + "\n"
        FILE.write(historyList[i])



    FILE.close()

def askDecimal(decimalPlace):
    '''
    asks how many decimal places the user wants. The default is set to 2
    :return:
    '''
    newDecimalPlace = input(f"""
How many decimal places would you like there to be? Current: ({decimalPlace})

> """)
    if newDecimalPlace.isnumeric():
        newDecimalPlace = int(newDecimalPlace)
        return newDecimalPlace
    else:
        print("Please enter a whole number! ")
        return askDecimal(decimalPlace)

def saveDecimal(decimalPlace):
    '''
    saves the decimal places in a file. It seems useless, but if a user uses the calculator frequently, they may find it annoying to re-input the amount of decimal points
    :param decimalPlace: (int)
    :return: (none)
    '''
    file = open("decimalPlaceFile.txt", "w")
    decimalPlace = str(decimalPlace)
    file.write(decimalPlace)
    file.close


# --- PROCESSING --- #
def solveEquation(equation):
    '''
    Solves the equations
    :param equation: (tuple).
    :return:
    '''
    equation = list(equation)
    unitConversionValues = []
    product = 1

    for i in range(len(equation[0])):
        appendAgain = True
        try:
            for j in range(len(equation[0][i])):
                product *= equation[0][i][j]
                if appendAgain == True:
                    unitConversionValues.append(equation[0][i])
                    appendAgain = False
            equation[0][i] = product
        except TypeError:
            unitConversionValues.append(equation[0][i])
            pass
        equation[1][i] = equation[0][i] * equation[1][i]
    returnAnswer = actuallySolveIt(equation[1])

    for i in range(len(equation[1]) - 1):
        equation[1][i] = equation[1][i] / equation[0][i]

    equation[0] = unitConversionValues

    return [returnAnswer,equation]

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
            "162": (4 * (3.141592653589793238462643383279502884197169399375105820974944592 ** 2) * variable[0]) / variable[1] ** 2,
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
    print("""

Welcome to the Kinematics Calculator! 
This calculator will help you calculate any variable in Kinematics!
It can save your calculation history, and also allows you to clear it!
""")


def formulaSheet(formula):
    '''
    prints out the formula sheet BEAUTIFULLY
    :return: (none)
    '''
    global universalConstant
    if formula == "formulaSheet":
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
    else:
          print("""
    -------------------------------------------------------------------------------------------------------------------------------------------------- 
    |                                                          Prefix Symbol Value
    |                   Distance                                      Velocity
    |    
    |    atto ............. a ..............10⁻¹⁸
    |    femto ............ f ..............10⁻¹⁵
    |    pico.............. p ..............10⁻¹²
    |    nano.............. n ..............10⁻⁹
    |    micro ............ u ..............10⁻⁶
    |    milli............. m ..............10⁻³
    |    centi............. c...............10⁻²
    |    deci.............. d ..............10⁻¹
    |    deka ............. da..............10¹
    |    hecto ............ h ..............10²
    |    kilo ............. k ..............10³
    |    mega ............. M ..............10⁶
    |    giga.............  G...............10⁹
    |    tera.............. T ..............10¹²
    |
    -----------------------------------------------------------------------------------------------
""")

    menu = input("""Press any key to return to menu

> """)

def displayHistory():
    '''
    displays the entire calculation history of the user
    :return: (none)
    '''
    global historyPast
    if len(historyPast) != 0:
        print("""
        
        
     
                                               Oldest""")
        # Make them look nicer
        for i in range(len(historyPast)):
            values = []
            print(f"Before: {historyPast[i][5]}")
            historyPast[i][3] = historyPast[i][3].split()
            historyPast[i][4] = historyPast[i][4].split()
            historyPast[i][5] = historyPast[i][5].split()
            print(f"After: {historyPast[i][5]}")
            ifAcceleration = ""
            if historyPast[i][-2][-2:] == "^2":
                historyPast[i][-2] = historyPast[i][-2][:-2]
                ifAcceleration = "²"


            for j in range(len(historyPast[i][4])):
                values.append(historyPast[i][3][j] + " " + historyPast[i][4][j] + " " + reverseUnitConversions[historyPast[i][5][j]])
            print(f"""{historyPast[i][0]}
  Time: {historyPast[i][1]}
  Formula Used: {displayFormula[historyPast[i][2]]}""")
            print(f"""  
  Inputted Values: """)
            for h in range(len(values)):

                print(f"""  {values[h]}""")
            print(f"""
  Answer: {historyPast[i][6]} {historyPast[i][8]}{ifAcceleration}
  Rounded Answer: {historyPast[i][7]} {historyPast[i][8]}{ifAcceleration}
{historyPast[i][9]}""")
        print("""                                          Most Recent
    
*If you would like to clear calculation
history, type "Clear All".    
        
    """)
        menu = input("""Press any key to return to menu.

> """)
        if menu == "Clear All":
            file = open("calculation_history.txt", "w")
            file.write("")
            file.close()
            print(""" 
History Cleared Successfully! """)
        else:
            pass
    else:
        print("""
        
Empty calculation history!
""")

def displayAnswer(answer):
    '''
    displays the answer
    :param answer: (float)
    :return: (none)
    '''
    ifAcceleration = ""
    global answerUnits
    printAnswerUnits = answerUnits
    if answerUnits[-2:] == "^2":
        printAnswerUnits = answerUnits[:-2]
        ifAcceleration = "²"
    print(f"""Answer: {answer} {printAnswerUnits}{ifAcceleration}""")

### --- DICTIONARY --- ###

unitConversionsDistance = {
    "am": 0.000000000000000001,
    "fm": 0.000000000000001,
    "pm": 0.000000000001,
    "nm": 0.000000001,
    "um": 0.000001,
    "mm": 0.001,
    "cm": 0.01,
    "dm": 0.1,
    "m": 1,
    "dam": 10,
    "hm": 100,
    "km": 1000,
    "Mm": 1000000,
    "Gm": 1000000000,
    "Tm": 1000000000000,
}

unitConversionsTime = {
    "S" : 1.0,
    "Mins" : 60,
    "H" : 3600,
    "Days" : 86400,
    "Weeks" : 604800,
}



reverseUnitConversions = {
    "1e-18" : "am",
    "1e-15" :    "fm",
    "1e-12" :       "pm",
    "1e-09" :          "nm",
    "1e-06" :             "μm",
    "0.001" :                "mm",
    "0.01" :                 "cm",
    "0.1" :                  "dm",
    "10" :                   "dam",
    "100" :                  "hm",
    "1000" :                 "km",
    "1000000" :              "Mm",
    "1000000000" :           "Gm",
    "1e-12" :                "Tm",
    "1" :                    "m",
    "1.0" :                  "s",
    "60" :                   "mins",
    "3600" :                 "h",
    "86400" :                "days",
    "604800" :               "weeks"
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
    "111": ["Distance? ", "Time? ", "m/s"],
    "112": ["Acceleration? ", "Time? ", "m/s"],
    # Initial Velocity
    "121": ["Distance? ", "Time? ", "Acceleration? ", "m/s"],
    "122": ["Final Velocity? ", "Acceleration? ", "Distance? ", "m/s"],
    "123": ["Distance? ", "Final Velocity? ", "Time? ", "m/s"],
    # Final Velocity
    "131": ["Distance? ", "Time? ", "Acceleration? ", "m/s"],
    "132": ["Distance? ", "Initial Velocity? ", "Time? ", "m/s"],
    "133": ["Initial Velocity? ", "Acceleration? ", "Distance? ", "m/s"],
    # Centripetal Velocity
    "141": ["Radius? ", "Period? ", "m/s"],
    # Acceleration
    "151": ["Velocity? ", "Time? ", "m/s^2"],
    # Centripetal Acceleration
    "161": ["Velocity? ", "Radius? ", "m/s^2"],
    "162": ["Radius? ", "Period? ", "m/s^2"],
    # Distance
    "171": ["Initial Velocity? ", "Time? ", "Acceleration? ", "m"],
    "172": ["Final Velocity? ", "Time? ", "Acceleration? ", "m"],
    "173": ["Final Velocity? ", "Initial Velocity? ", "Time? ", "m"],
    "174": ["Final Velocity? ", "Initial Velocity? ", "Acceleration? ", "m"],
    # Time
    "181": ["Velocity? ", "Distance? ", "Seconds"],
    "182": ["Acceleration? ", "Velocity? ", "Seconds"],
    "183": ["Distance? ", "Initial Velocity? ", "Acceleration? ", "Seconds"],
    "184": ["Distance? ", "Final Velocity? ", "Acceleration? ", "Seconds"],
    "185": ["Distance? ", "Final Velocity? ", "Initial Velocity? ", "Seconds"]
}

displayFormula = {
    # Velocity
    "111": "vₐᵥₑ = △d/△t",
    "112": "aₐᵥₑ = △v/△t",
    #Initial Velocy
    "121": "d = vᵢt + ½at²",
    "122": "vբ = vᵢ² + 2ad",
    "123": "d = [(vբ + vᵢ) / 2]t",
    #Final Velocity
    "131": "d = vբt - ½at² ",
    "132": "d = [(vբ + vᵢ) / 2]t",
    "133": "vբ = vᵢ² + 2ad",
    #Centripetal Velocity
    "141": "|v꜀|=  2πr/T",
    #Acceleration
    "151": "aₐᵥₑ = △v/△t",
    #Centripetal Acceleration
    "161": "|a꜀| = v²/r",
    "162": "|a꜀|= (4π²r)/T²",
    #Distance
    "171": "d = vᵢt + ½at²",
    "172": "d = vբt - ½at²",
    "173": "d = [(vբ + vᵢ) / 2]t",
    "174":  "vբ = vᵢ² + 2ad",
    #Time
    "181": "vₐᵥₑ = △d/△t",
    "182": "aₐᵥₑ = △v/△t",
    "183": "d = vᵢt + ½at",
    "184": "d = vբt - ½at²",
    "185": "d = [(vբ + vᵢ) / 2]t"



}
# --- MAIN PROGRAM --- #
if __name__ == "__main__":
    intro()
    while True:
        historyPast = readFile("calculation_history.txt")  # it reads the history file, and after someone does a calculation, it updates the "historyPast" variable with the newly added history, which is already added to the file
        decimalPlace = readFile("decimalPlaceFile.txt")
        option = menu()
        if option == 1:
            choice = selectVariable()  # returns a tuple, where the first thing identifies the unit it's from, and the second thing identifies the variables
            equation = selectEquation(choice)
            values = getValues(equation)
            answer = solveEquation(values)
            values = answer[1]
            answer = answer[0]
            roundedAnswer = round(answer, decimalPlace)
            displayAnswer(roundedAnswer)
            time = datetime.now()
            trackHistory(numberCombination, equation, values, time, answer, roundedAnswer)
        if option == 2:
            decimalPlace = askDecimal(decimalPlace)
            saveDecimal(decimalPlace)
        if option == 3:
            displayHistory()
        if option == 4:
            formulaSheet("formulaSheet")
        if option == 5:
            formulaSheet("unitConversionSheet")
        if option == 6:
           exit()