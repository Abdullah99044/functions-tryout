def actionFunction():
    print("...........................")
    print("You have no choice now but to attack him, choose your strike")
    print("1-Normal attack 10 dmg")
    print("2-hard attack 20 dmg")
    print("3-range attack 12 dmg")
    print("4-hard range attack 22 dmg ")
    print("5-magic attack 30 dmg")
    print("6-debuff (heal 10 dmg)")
    print("7-fire attack 13 dmg")
    print("8-counter attack (20 dmg)")
    print("9-ultimate attack 40 dmg (you can use it only for one time!)")
    print("10-special attack 20 dmg")
    print("...........................")
    

def gameoverFunction():
    print(".........................................")
    print("It was a weak strike, you lost the battle")
    print("Game over!") 

def lootFunction():
    while True:
        print(".........................")
        print("loot dragon items:")
        print("You can't carry more than 50 kg!")
        print(".........................")
        print("Horn 22kg max 3")
        print("wing crust 15kg max 1")
        print("dragonTeeth 13kg max 8")
        horn1 = 22
        horns = int(input("how much will you take? (horn)"))
        horn = int(horn1 * horns)
        wingcrust1 = 15
        wingcrust2 = int(input("how much will you take? (wing crust)"))
        wingCrust = int(wingcrust1 * wingcrust2)
        dragonTeeth1 = 15
        drgonteth2 = int(input("how much will you take? (dragonTeeth)"))
        dragonteeth = int(dragonTeeth1 * drgonteth2 )
        print("total:")
        total = int(dragonteeth + wingCrust + horn )
        print(total)
        if total <= 50:
            print("Mission complited")
            break
        else:
            if  total >= 50:
                print("it is more than what you can")
    


while True:   
    print("..................................")
    naam = input("What is your name?")
    print("Welcome", naam)
    print("..................................")
    print("You are a magical warrior, a village was attacked by a huge dragon and you were asked to fight  ")
    print("him to liberate the village and kill him before he attacks another village.")
    print("Will you accept the request" , naam , "?")
    print("...........................")
    answer = input("yes or no?:")
    if answer == "yes" :
        print("...........................")
        print("You are now in the village that was attacked, the whole village is destroyed and the fire burned")
        print("everything, the bodies of the soldiers are everywhere.")
        answer = input("press to continue")
        print("Suddenly the giant dragon came to you, after smelling your scent from afar")
        print("Ahhhhhhh he started screaming, looks like he's been hungry for a long time and now he found his food.")
        actionFunction()
        print("dragon health is 70")
        answer = input("chose the number of your attack:")
        #path 1 choice 1 (win)
        if answer == "9":
            print("...........................")
            print("The dragon get dammaged!! , hit hem again with a powerfull attack or you will die. ")
            print("...........................")
            print("You have no choice now but to attack him, choose your strike")
            print("1-Normal attack 10 dmg")
            print("2-hard attack 20 dmg")
            print("3-range attack 12 dmg")
            print("4-hard range attack 22 dmg ")
            print("5-magic attack 30 dmg")
            print("6-debuff (heal 10 dmg)")
            print("7-fire attack 13 dmg")
            print("8-counter attack 20 dmg")
            print("9-special attack 20 dmg ")
            print("...........................")
            print("dragon health is 30")
            print("...........................")
            answer = input("chose the number of your attack:")
            if answer == "5":
                print("Well done, you killed the giant dragon and liberated the village,")
                print(" the generations will remember you and your family will be proud of you.......")
                print(".")
                print(".")
                answer = input("Press any button to continue ")
                lootFunction()
            else:
                gameoverFunction()
        elif answer == "5":
            print("The dragon get dammaged!! , hit hem again with a powerfull attack or you will die. ")
            print("...........................")  
            print("You have no choice now but to attack him, choose your strike")
            print("1-Normal attack 10 dmg")
            print("2-hard attack 20 dmg")
            print("3-range attack 12 dmg")
            print("4-hard range attack 22 dmg ")
            print("5-magic attack 30 dmg")
            print("6-debuff (heal 10 dmg)")
            print("7-fire attack 13 dmg")
            print("8-counter attack (20 dmg)")
            print("9-ultimate attack 40 dmg (you can use it only for one time!)")
            print("10-special attack 20 dmg ")
            print("...........................")
            print("dragon health is 40")
            print("...........................")
            answer = input("chose the number of your attack:") 
            if answer == "9":
                print(".............................")
                print("Well done" ,naam)  
                print("you killed the giant dragon and liberated the village,")
                print(" the generations will remember you and your family will be proud of you.......")
                print(".")
                print(".")
                answer = input("Press any button to continue ")
                lootFunction()
            else:
                gameoverFunction()
        #path 2
        else:
            print("...........................")
            print("It was a weak attack, you have to choose your attack carefully again or you will die!") 
            actionFunction() 
            answer = input("chose the number of your attack:")
            if answer == "9":
                print("Well done" ,naam)  
                print("you killed the giant dragon and liberated the village,")
                print(" the generations will remember you and your family will be proud of you.......")
                print(".")
                print(".")
                answer = input("Press any button to continue ")
                lootFunction()
            else:
                gameoverFunction()  
    else:
        print("....................")
        print("you lost" , naam)   
        
