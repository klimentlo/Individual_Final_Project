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
    value = input("""
What unit would you like to solve from?
1. Kinematics
2. Dynamics
3. Momentum and Energy
4. Waves
5. Electricity and Magnetism
6. Atomic Physics
7. Quantum Mechanics and Nuclear Physics

> """)
    if value.isnumeric():
        value = int(value)
        if value > 0 and value < 8:
            if value == 1:
                variable = input("""What variable do you want to solve for?
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
                    if variable > 0 and variable < 7:
                        return variable

            elif value == 2:
                pass
                variable = input("""What variable do you want to solve for?

> """)
            elif value == 3:
                pass
                variable = input("""What variable do you want to solve for?
> """)
            elif value == 4:
                pass
                variable = input("""What variable do you want to solve for?
> """)
            elif value == 5:
                pass
                variable = input("""What variable do you want to solve for?
> """)
            elif value == 6:
                pass
                variable = input("""What variable do you want to solve for?
> """)
            elif value == 7:
                pass
                variable = input("""What variable do you want to solve for?

> """)
            else:
                print("That is not a valid option! ")
                return selectVariable()
        else:
            print("Please enter a valid option")
    else:
        print("Please enter a valid number! ")
        return selectVariable()

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

# --- MAIN PROGRAM --- #
if __name__ == "__main__":
    universalConstant = readFile()
    #print(universalConstant)
    intro()
    while True:
        option = menu()
        if option == 1:
            choice = selectVariable()
        if option == 2:
            pass
        if option == 3:
            pass
        if option == 4:
            formulaSheet()
        if option == 5:
            exit()