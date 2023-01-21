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
    if FILENAME == "decimalPlaceFile.txt": # if its for the decimalPlaceFile
        try:
            file = open(FILENAME, "x") # try to open a new file
            file.write("2") # set regular as 2
            file.close() # close the file
            fileList = 2 # set it as two in the program itself
        except FileExistsError:
            file = open(FILENAME) # if already exists
            fileList = file.read() # read the file
            fileList = int(fileList) # make it ingeter
            file.close() # close file
    else: # if its the history file
        try:
            file = open(FILENAME, "x") # try to create file
            file.close()
            fileList = []
        except FileExistsError: # if already exists
            file = open(FILENAME)
            fileList = file.readlines() # read its contents
            file.close()
            for i in range(len(fileList)): # for the length of the file contents
                if fileList[i][-1] == "\n": # if there is a linebreak
                    fileList[i] = fileList[i][:-1] # remove the linebreak
                fileList[i] = fileList[i].split(",") # split each calculation into its own list
    return fileList # returns the file Contents


def menu():
    '''
    The place where the user can choose what they want to do
    :return:(int)
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
    if option.isnumeric(): # if its a number
        option = int(option) # make it an ingeter
        if option > 0 and option < 7: # if it is within the selectable options
            return option # return it
        else: # if its not within the possible options
            print("Please enter a valid number! ") # tell them its an invalid imput
            return menu() # try again
    else: # if its not a number
        print("Please enter a valid number! ") # print that its not a number
        return menu() # try again

def selectVariable():
    '''
    user decides what variable they want to solve for
    :return: (int)
    '''
    value = 1 # the value is set at 1, as initially i wanted to do different units in physics, but i couldnt find the time to do it, so instead of rewriting some code, I just made value = "1", and the code functions fine
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
    if variable.isnumeric(): # if whole number
        variable = int(variable) # make it integer
        if variable > 0 and variable < 9: # if in the possible option s
            return str(value), str(variable) # return the unit and the variable they want to solve for
        else:
            print("Please enter a valid option")
            return selectVariable()
    else:
        print("Please enter a valid number! ")
        return selectVariable()


def selectEquation(unitValue):
    '''
    Selects the variable they want to use to calculate the variable that they chose earlier
    :param unitValue: (list)
    :return: (list) (the values that they'll need to input in order to solve for that formula
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
    print("""
IMPORTANT. Seperate the numbers and units with a space! (e.g 50 am/min) """)
    print("For time, units include Seconds (s), Minutes (min), and Hours (h) ")
    print("")
    # What getVariables is at the moment. example: ["Velocity? ", "Time? ", "m/s^2"]
    answerUnits = getVariables[-1] #takes the last index of the list, and make its the answer units, so when we display the answer, it uses the correct units
    return getVariables[:-1] # returns the rest of the list, excluding the answer units

def getValues(missingVariables):
   '''
   Asks the user the values, and also gets the units
   :param missingVariables: (list) array of what the formula needs to solve for the thing
   :return: (list of values) e.g (30, 25, 13)
   '''
   global numberCombination
   # nubmerCombination currently is. example (str): 151
   # missingVariables currently is. example: ["Velocity? ", "Time? ]
   unitList = []
   variables = []

   # Requesting Values
   for i in range(len(missingVariables)):  # for the length of the list of variables eg. ["Velocity? ", "Time? ]
       userInput = checkValues(missingVariables[i]) # they put the variable into this function, where it sorts out the inputs
       # example of userInputs is currently: (30.0, 0.2777777777777778) 30.0 being the number they inputted, and 0.2777 being the unit conversion value they put (km/h)
       variables.append(userInput[0]) # appends the value they inputted
       unitList.append(userInput[1]) # appends the unit conversion, which will be applied later

   variables.append(numberCombination) # append number combination ("151") into variables list
   return (unitList, variables)



def checkValues(missingVariables):
   '''
   This is where the user inputs the values needed, to solve for the formula
   :param missingVariables: (str)
   :return:
   '''
   global acceleration # this is a terrible name for it, it's just to check if its a scenario which the units are combined weirdly. e.g(km/h) = 0.277777778

   # an example of missingVariables currently is: "Velocity? "

   variables = input(f"{missingVariables}")  # User inputs the value and units they want (there must be a space between them)
   variables = variables.split(" ") # seperates the units and values

   try:
       variables[0] = float(variables[0])  # try to make the first value a float
   except:  # but if turns out its a word
       print("Please enter a number! ")
       return checkValues(missingVariables)  # returns to start, making them re input the value
   # Checks if formatting is Correct
   if len(variables) == 2:  # if they did the formatting correctly e.g("90", "cm")
       if missingVariables == "Time? " or missingVariables == "Period? ": # if what the program is requesting is a time related input
           variables[-1] = variables[-1].title() # make the unit's first letter capitalized, and the rest undercased

           try:  # I realized that the if statement is useless, as if it doesnt work it'll bug out anyways, but it works as of right now and i don't wanna mess with it
               if unitConversionsTime[variables[-1]]: # try to put the unit into this library
                    acceleration += "n" # tell the program that no, its not a weird unit
                    returnUnit = unitConversionsTime[variables[-1]]

           except KeyError: # if it doesn't exist
               print("Those were invalid units! Try again. ")
               return checkValues(missingVariables) # try again

       elif missingVariables == "Distance? " or missingVariables == "Radius? ": # if what the computer was requesting for was distance
           try:
               if unitConversionsDistance[variables[-1]]: # put it into library, if it works
                    acceleration += "n" # tell the program that no, it's not a weird unit
                    returnUnit = unitConversionsDistance[variables[-1]]
           except KeyError: # if it didn't exist in the library
               print("Those were invalid units! Try again. ")
               return checkValues(missingVariables) # trry again

       elif missingVariables == "Velocity? " or missingVariables == "Initial Velocity? " or missingVariables == "Final Velocity? " or missingVariables == "Acceleration? ": # if its one of the wacky inputs, where theres
           # if its a value that represents something with double units
           variables[-1] = variables[-1].split("/") # split the units by the /
           if len(variables[-1]) == 2 : # if the length of the units is 2 (this is in case someone uses multiple slashes)
               returnUnit = []
               # Example of variables as of right now: [30.0, ['km', 'h']]
               try:
                    returnUnit.append(unitConversionsDistance[variables[-1][0]]) # Run the distance portion of the unit into the dictionary, and appends it
               except KeyError: # if it doesn't exist
                   print("That is an invalid distance! Try again. ")
                   return checkValues(missingVariables) # try again
               try:
                    variables[-1][1] = variables[-1][1].title() # make the time portion of the unit into a specific format, to account for the unit "min"
                    returnUnit.append(unitConversionsTime[variables[-1][1]]) # run the time portion of the unit into the time unit conversion dictionary, and appending the value
                    returnUnit = returnUnit[0]/returnUnit[1]  # divide the distance unit value with the time unit value
                    acceleration += "y" # tells the program that yea, its a weird unit thingy
               except KeyError: #if the time portion didnt exist
                   print("That is an invalid time! Try again. ")
                   return checkValues(missingVariables) # try again
           else: # if there are multple slashes
               if len(variables[-1]) > 2:
                    print("Please only use one slash!")
               else:
                   print("Please use a slash the separate the units (30 km/h)")
               return checkValues(missingVariables) # try again

   else: # if the units weren't formatted properly
       print("Include a space between the number and the units! ")
       return checkValues(missingVariables) # try again


   # variables[0] is currently: "30.0"
   # returnUnit is currently : 0.2777777777777778

   return variables[0], returnUnit # returns it back to the getValues function, where it'll run it again as it's in a for loop, until all the missing values are retrieved


def trackHistory(formula, requestValues, values, time, answer, roundedAnswer):
    ''' This is my favorite function
    Tracks the calculation history of the user
    :param formula: (str)
    :param requestValues: (list)
    :param values: 2D array
    :param time: ?????
    :param answer: (float)
    :param roundedAnswer: (float)
    :return: (none)
    '''
    global historyPast, answerUnits, acceleration
    #      (2D ARRAY)     (str)          (str)

    # --- # The following code is to prepare it so it is able to be written in a file, where it can be reviewed as the calculation history

    # requested Values was ["Distance? ", "Time? "]
    requestValues = "".join(requestValues) # join them into one string

    # values is currently ([0.2777777777777778, 1.0], [30.0, 20.0, '151'])
    units = values[0]  # gets the units

    for i in range(len(units)):
        units[i] = str(units[i]) # makes the units a string
    units = " ".join(units) # joins them

    values = values[1][:-1]  # gets the values inputted
    for i in range(len(values)):
        values[i] = str(values[i])
    values = " ".join(values)
    time = str(time)
    answer = str(answer)
    roundedAnswer = str(roundedAnswer)
    newHistory = ["-----------------------------------------------------",time,formula,requestValues,values,units, answer, roundedAnswer, answerUnits, acceleration, "-----------------------------------------------------"]
    historyList = []

    for i in range(len(historyPast)): # for the length of old history path
        historyList.append(historyPast[i]) # append all of it into the historyList
    historyList.append(newHistory) # append the new history into that list of history
    FILE = open("calculation_history.txt", "w")
    for i in range(len(historyList)): # for the length of total history
        historyList[i] = ",".join(historyList[i]) + "\n" # join the commas, then add a line break
        FILE.write(historyList[i]) # write it into the file
    FILE.close() # once done, close the file

def askDecimal(decimalPlace):
    '''
    asks how many decimal places the user wants. The default is set to 2
    :param decimalPlace: (int)
    :return: (int)
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

    file = open("decimalPlaceFile.txt", "w") # open decimal file
    decimalPlace = str(decimalPlace) # make decimal into string
    file.write(decimalPlace) # write it down
    file.close # close the file


# --- PROCESSING --- #
def solveEquation(equation):
    '''
    Solves the equations
    :param equation: (tuple).
    :return: (float)
    '''

    # an example of equation currently: ([0.2777777777777778, 1.0], [30.0, 20.0, '151'])
    for i in range(len(equation[0])): # for the length of the unitConversion values
        equation[1][i] = equation[0][i] * equation[1][i] # multiply the unit conversion value with their respective value

    # example of what equation[1] currently is: [8.333333333333334, 20.0, '151']

    returnAnswer = actuallySolveIt(equation[1]) # runs the accurate values into the function that looks for the equation

    for i in range(len(equation[1]) - 1): # for the length of values -1 (cause of the numberCombination)
        equation[1][i] = equation[1][i] / equation[0][i] # divide them back to their original state, its only used to

    return returnAnswer

def actuallySolveIt(variable):
    '''
    looks for the formula that the user wants to use, and plugs in the numbers
    :param variable: (list)
    :return: (float)
    '''
    # example of variable currently: [8.333333333333334, 20.0, '151']

    for i in range(len(variable)-1): # for the length of variables
        variable[i] = float(variable[i]) # make sure they're floats

    # the reason why we must check if its 3 or 4 long is that if a 3 length variable goes in, it will print out an error as the formulas that use up 4 formulas will not detect a 4th variable

    if len(variable) == 3: # if the length of variable is 3 (including the numberCombination)
        try:
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
        except ZeroDivisionError:
            print("Values can not be divided by 0! Please try again.")
            return "zero"

        answer = getFormula1[variable[-1]] # inputs the numberCombination, which plugs in the values
        return answer

    if int(len(variable)) == 4:
        getFormula2 = {
            # Initial Velocity
            "121": (variable[0] - (0.5 * variable[2] * variable[1] ** 2)) / variable[1],
            "122": (variable[0] - 2 * variable[1] * variable[2]),
            "123": (variable[0] / variable[2] * 2 - variable[1]),
            # Final Velocity
            "131": (variable[0] - 0.5 * variable[2] * variable[1] ** 2) / variable[1],
            "132": (variable[0] / variable[2] * 2 - variable[1]),
            "133": (variable[0] ** 2 + (2 * variable[1] * variable[2])),
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
        if variable[-1] == "122": # if its this scenario
            if answer < 0: # if the initial velocity is negative
                answer = answer * -1 # make it positive

            answer = math.sqrt((answer))
            answer = answer * -1

        if variable[-1] == "183" or variable[-1] == "184": # it wouldn't allow me to square root it inside the library
            try:
                answer1 = (-variable[1] + math.sqrt(answer)) / variable[2] # uses the quadratic formula
                answer2 = (-variable[1] - math.sqrt(answer)) / variable[2] # uses the quadratic formula
                 # since time can't be negative

                if answer1 > 0 and answer2 < 0: # if answer 1 is positive
                    return answer1

                elif answer2 > 0 and answer1 < 0: # if answer 2 is positive
                    return answer2

                elif answer1 < 0 and answer2 < 0: # if answer 1 and 2 were both negative
                    return "none"

                elif answer1 > 0 and answer2 > 0:
                    return [answer1, answer2]

            except ValueError:
                return "none"

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
It saves your calculation history, and allows you to clear it!
All answers are outputted in the standard units, but you may use any unit when inserting the values!
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
    -------------------------------------------------------------------------------------------------
    |                                   Prefix Symbol Value                                         |    
    |                                                                                               |      
    |                   Distance                                                                    |    
    |                                                                                               |    
    |    atto .......... a ........... 10⁻¹⁸                                                        |                           
    |    femto ......... f ........... 10⁻¹⁵                                                        |                                        
    |    pico .......... p ........... 10⁻¹²                                                        |                                           
    |    nano .......... n ........... 10⁻⁹                  Velocity                               |    
    |    micro ......... u ........... 10⁻⁶                                                         |    
    |    milli ......... m ........... 10⁻³    seconds ......... s .......... 10⁰                   |    
    |    centi ......... c ........... 10⁻²    minutes ......... min ........ 1.66 * 10⁻²           |    
    |    deci .......... d ........... 10⁻¹    hours ........... h .......... 2.7777 * 10⁻⁴         |    
    |    deka .......... da .......... 10¹                                                          |    
    |    hecto ......... h ........... 10²                                                          |    
    |    kilo .......... k ........... 10³                                                          |    
    |    mega .......... M ........... 10⁶                                                          |    
    |    giga .........  G ........... 10⁹                                                          |    
    |    tera .......... T ........... 10¹²                                                         |    
    |                                                                                               |    
    -------------------------------------------------------------------------------------------------
""")

    menu = input("""Press any key to return to menu

> """)

def displayHistory():
    '''
    displays the entire calculation history of the user
    :return: (none)
    '''
    global historyPast
    if len(historyPast) != 0: # if the history has content in it
        print("""
        
        
     
                                               Oldest""")
        # Make them look nicer
        for i in range(len(historyPast)): # for the amount of calculations
            values = []
            historyPast[i][3] = historyPast[i][3].split("? ") # splits the requested variable ("Velocity?", "Distance?")
            historyPast[i][4] = historyPast[i][4].split()  # splits the value number ("30.0", "20.0")
            historyPast[i][5] = historyPast[i][5].split() #splits the unit conversion values ("1.0", "1000000.0")
            for j in range(len(historyPast[i][4])): # for the length of that specific value length
                try:
                    if historyPast[i][9][j] == "n": # if it doesn't have any weird combination unit (examples include the unit conversions of km/h, km/min, etc.)
                        values.append(historyPast[i][3][j] + ": " + historyPast[i][4][j] + " " + reverseUnitConversions[historyPast[i][5][j]]) # appends them nicely
                    else: # if it does have them weird combinations
                        values.append(historyPast[i][3][j] + ": " + historyPast[i][4][j] + " " + reverseUnitConversionsAcceleration[historyPast[i][5][j]]) # appends them nicely
                except KeyError:
                    # im very sorry for having to resort to this. Im not sure if all of them work, and it would take too long to run and test through all of them, however from all the values i've test with, they've worked
                    if historyPast[i][9][j] == "n":
                        values.append(historyPast[i][3][j] + ": " + historyPast[i][4][j] + " " + "ERROR")
                    else:
                        values.append(historyPast[i][3][j] + ": " + historyPast[i][4][j] + " " + "ERROR")

            ifAcceleration = ""
            if historyPast[i][-3][-2:] == "^2": # if the units were this
                historyPast[i][-3] = historyPast[i][-3][:-2] # make it disappear
                ifAcceleration = "²" # makes it so its little 2, which will then print nicer
            print(f"""{historyPast[i][0]}
                
  Time: {historyPast[i][1]}
  Formula Used: {displayFormula[historyPast[i][2]]}""")
            print(f"""  Inputted Values: """)
            for h in range(len(values)):

                print(f"""  {values[h]}""")
            print(f"""
  Answer: {historyPast[i][6]} {historyPast[i][8]}{ifAcceleration}
  Rounded Answer: {historyPast[i][7]} {historyPast[i][8]}{ifAcceleration}
  
{historyPast[i][10]}""")
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
    print(f"""
Answer: {answer} {printAnswerUnits}{ifAcceleration}""")

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
    "Min" : 60,
    "H" : 3600,
}



reverseUnitConversions = {
    # Distance
    "1e-18" :      "am",
    "1e-15" :      "fm",
    "1e-12" :      "pm",
    "1e-09" :      "nm",
    "1e-06" :      "μm",
    "0.001" :      "mm",
    "0.01" :       "cm",
    "0.1" :        "dm",
    "1":           "m",
    "10" :         "dam",
    "100" :        "hm",
    "1000" :       "km",
    "1000000" :    "Mm",
    "1000000000" : "Gm",
    "1e-12" :      "Tm",
    # Time
    "1.0" :        "s",
    "60" :         "min",
    "3600" :       "h",
}

reverseUnitConversionsAcceleration = {
    # Seconds
    "1e-18" :                "am/s",
    "1e-15" :                "fm/s",
    "1e-12" :                "pm/s",
    "1e-09" :                "nm/s",
    "1e-06" :                "μm/s",
    "0.001" :                "mm/s",
    "0.01" :                 "cm/s",
    "0.1" :                  "dm/s",
    "1":                     "m/s",
    "1.0" :                  "m/s",
    "10.0" :                 "dam/s",
    "100.0" :                "hm/s",
    "1000.0" :               "km/s",
    "1000000.0" :            "Mm/s",
    "1000000000.0" :         "Gm/s",
    "1000000000000.0" :      "Tm/s",
    # Min
    "1.6666666666666668e-20" : "am/min",
    "1.6666666666666667e-17" : "fm/min",
    "1.6666666666666667e-14" : "pm/min",
    "1.6666666666666667e-11" : "nm/min",
    "1.6666666666666667e-08" : "μm/min",
    "1.6666666666666667e-05" : "mm/min",
    "0.00016666666666666666" : "cm/min",
    "0.0016666666666666668" :  "dm/min",
    "0.016666666666666666":    "m/min",
    "0.16666666666666666" :    "dam/min",
    "1.6666666666666667" :     "hm/min",
    "16.666666666666668" :     "km/min",
    "16666.666666666668" :     "Mm/min",
    "16666666.666666666" :     "Gm/min",
    "16666666666.666666" :     "Tm/min",
    # Hours
     "2.777777777777778e-22" :    "am/h",
     "2.777777777777778e-19" :    "fm/h",
     "2.777777777777778e-16" :    "pm/h",
     "2.777777777777778e-13" :    "nm/h",
     "2.7777777777777777e-10'" :  "μm/h",
     "2.7777777777777777e-10" :   "μm/h",
     "2.7777777777777776e-07" :   "mm/h",
     "2.777777777777778e-06" :    "cm/h",
     "2.777777777777778e-05" :    "dm/h",
     "0.0002777777777777778":     "m/h",
     "0.002777777777777778" :     "dam/h",
     "0.027777777777777776" :     "hm/h",
     "0.2777777777777778" :       "km/h",
     "277.77777777777777" :       "Mm/h",
     "277777.77777777775" :       "Gm/h",
     "277777777.7777778" :        "Tm/h",
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
        acceleration = ""
        historyPast = readFile("calculation_history.txt")  # it reads the history file, and after someone does a calculation, it updates the "historyPast" variable with the newly added history, which is already added to the file
        decimalPlace = readFile("decimalPlaceFile.txt")
        option = menu() # asks user what they want to do
        if option == 1:  # if they want to make a calculation
            choice = selectVariable()  # returns a tuple, where the first thing identifies the unit it's from, and the second thing identifies the variables
            equation = selectEquation(choice) # identifies what values thats needed to solvefor the formula they want
            values = getValues(equation) # actually gets the values and the unitConversion ratios
            answer = solveEquation(values) # put values into the equations
            if isinstance(answer, list):
                print(f"""Two possible answers were given out. Reinput the values to look for the extraneous root!  
{answer[0]} and {answer[1]}""")
            elif answer == "none":
                print("This calculation was not possible. Please try with other values. ")
            elif answer == "zero":
                pass
            else:
                # if its a list or is none, its not going to save it in the history as it is pointless
                roundedAnswer = round(answer, decimalPlace)  # rounds it
                displayAnswer(roundedAnswer) # displays the answer as the rounded answer
                time = datetime.now() # retrives the time of the calculation being made
                trackHistory(numberCombination, equation, values, time, answer, roundedAnswer) # tracks the history and writes it into the file
        if option == 2: # if they want to change decimal place value
            decimalPlace = askDecimal(decimalPlace) #changes it
            saveDecimal(decimalPlace) # saves it to the file, so they don't have to consistently readjust it every time they open the program
        if option == 3:
            displayHistory() # displays the history, even allowing them to clear it if needed
        if option == 4:
            formulaSheet("formulaSheet") # displays the formula sheet
        if option == 5:
            formulaSheet("unitConversionSheet") # displays the unit conversion sheet value
        if option == 6:
           exit() #closes the program