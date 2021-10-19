def nameFunction( x , y):
    print("Hallo :" , x)
    print("leeftijd is :" , y)
    return

while True:
    print("**********************************")
    print("Schrijf stop als u wilt stoppen")
    naam = input("Wat is jouw naam? : ")
    leeftijd = input("Hoe oud ben je? : ")
    nameFunction(naam , leeftijd)
    if naam and leeftijd == "stop":
        print("Je heeft gestopt")
        break
   
    