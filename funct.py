import random, math

def roll():
    listToReduce = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
    count = 0
    for y in listToReduce:
        if y == min(listToReduce) + count:
            count += 6
            listToReduce.remove(y)
    score = listToReduce[0]+listToReduce[1]+listToReduce[2]
    return score

def classSelect():
    passFail = 0
    while passFail == 0:
        print("\nHere is a list of classes. Please input the number associated with your class.")
        print("1.Barbarian  2.Bard  3.Cleric  4.Druid  5.Fighter  6.Mage  7.Wizard  8.Monk")
        print("9.Mystic  10.Paladin  11.Ranger  12.Sorceror  13.Thief  14. Rogue  15.Warlock")

        charClass = input()
        validClasses = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
        if charClass in validClasses:
            passFail = 1
        else:
            print("\nI'm sorry, that is an invalid input. Please try again.\n")
            passFail = 0
    classNums = {'1':'Barbarian','2':'Bard','3':'Cleric','4':'Druid','5':'Fighter','6':'Mage','7':'Wizard','8':'Monk','9':'Mystic','10':'Paladin','11':'Ranger','12':'Sorceror','13':'Thief','14':'Rogue','15':'Warlock',}
    print("\nYou have selected: " + classNums[charClass])
    return charClass


def statAssign():
    options = []
    for each in range(6):
        listToReduce = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
        count = 0
        for y in listToReduce:
            if y == min(listToReduce) + count:
                count += 6
                listToReduce.remove(y)
        score = listToReduce[0] + listToReduce[1] + listToReduce[2]
        options.append(score)
    print("\nYour stats to assign are:\n"+str(options).strip("[").strip("]"))
    print("\nThese are the stats you can assign them to:")
    print("1.STR  2.DEX  3.CON  \n4.INT  5.WIS  6.CHA")
    statVals = {}
    for each in options:
        passFail = 0
        while passFail == 0:
            att = input("\nWhere would you like to assign " + str(each) + "?\n")
            if att == "1":
                 statVals.update({"STR":each})
                 passFail = 1
            elif att == "2":
                statVals.update({"DEX":each})
                passFail = 1
            elif att == "3":
                statVals.update({"CON":each})
                passFail = 1
            elif att == "4":
                statVals.update({"INT":each})
                passFail = 1
            elif att == "5":
                statVals.update({"WIS":each})
                passFail = 1
            elif att == "6":
                statVals.update({"CHA":each})
                passFail = 1
            else:
                print("That is an invalid input, please try again.")
                passFail = 0
    return statVals

def modifierGet(stat):
    modifier = math.floor((stat/2)-5)
    return modifier

def healthGet(statVals,charClass):
    if charClass == "1":
        baseHP = 10
    if charClass == "5":
        baseHP = 10
    if charClass == "10":
        baseHP = 10
    else:
        baseHP = 8
    roll = random.randint(1,8)
    try:
        HP = modifierGet(statVals["CON"]) + roll + baseHP
    except KeyError:
        print("Make sure you don't input the same stat twice!")
    return HP

#Name

#roll 6 stats
#Then assign to:

#str
#dex
#con
#int
#wis
#cha

#(for monk) dex mod + wis mod + 10 for ac

#1d8 + con modifier + base health for total health
