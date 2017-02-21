import funct

def __main__():
    print("Welcome to Camden's Character Creator")
    input("Press enter to continue.\n")
    charName = input("\nEnter the name of your character, then press enter to continue.\n")
    charClass = funct.classSelect()
    passFail = 0
    while passFail == 0:
        try:
            statVals = funct.statAssign()
            try:
                HP = funct.healthGet(statVals,charClass)
            except UnboundLocalError:
                print("")
                passFail = 0
            classNums = {'1': 'Barbarian', '2': 'Bard', '3': 'Cleric', '4': 'Druid', '5': 'Fighter', '6': 'Mage', '7': 'Wizard',
                 '8': 'Monk', '9': 'Mystic', '10': 'Paladin', '11': 'Ranger', '12': 'Sorceror', '13': 'Thief',
                 '14': 'Rogue', '15': 'Warlock', }
            print("\n\n\nHere is your character:\n")
            print(str(charName)+" the "+classNums[charClass])
            try:
                print("HP = " + str(HP))
            except UnboundLocalError:
                print("")
            print("STR = " + str(statVals["STR"]))
            print("DEX = " + str(statVals["DEX"]))
            print("CON = " + str(statVals["CON"]))
            print("INT = " + str(statVals["INT"]))
            print("WIS = " + str(statVals["WIS"]))
            print("CHA = " + str(statVals["CHA"]))
            passFail = 1
        except KeyError:
            print("\n\n\n\n\n\n\n\n\n\n\nMake sure you don't input the same stat twice!")
            print("Try again.\n\n")
    input("\nThanks for rolling!")

__main__()
