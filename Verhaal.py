import os
os.system("cls")
inleiding = False
stukje_1 = False #
stukje_2 = False #
stukje_3 = False #
stukje_4 = False #
stukje_5 = False #
stukje_6 = False #
stukje_7 = False #
stukje_8 = False #
stukje_9 = False #
stukje_10 = False #
stukje_11 = False #
stukje_12 = False #
stukje_13 = False #
stukje_14 = False #
stukje_15 = False #
stukje_16 = False #
stukje_17 = False #
stukje_18 = False #
stukje_19 = False #
stukje_20 = False #
stukje_21 = False #
stukje_22 = False #
stukje_23 = False #
einde_1 = False #Gepakt
einde_2 = False # Blijven wonen in duitseland
einde_3 = False # Richting Spanje maar dat halen jullie niet
einde_4 = False # Moeder naar nederland halen
spelletje = False 

#Begin
print("Druk op enter om te starten!")
Druk_op_enter_1 = input(">>>")

inleiding = True
spelletje = True

while spelletje == True:
    os.system("cls")
    
    while inleiding == True:
        print("Inleiding,")
        print("Mijn naam is Max Montanus. Ik heb een verhaal geschreven over een vluchteling genaam Ruwanda. Ik hoop dat je goede keuze's maakt in het verhaal.")
        print("(druk op je enter toets om verder te gaan)")
        Druk_op_enter_1 = input(">>>")
        print("")
        stukje_1 = True
        inleiding = False
    
#Stukje_1
    while stukje_1 == True:
        print("Voordat de taliban binnendrong")
        print("Ruwanda was aan het werk in haar eigen Beauty salon totdat ze ineens inmensen knallen hoorde. De taliban was binnen gedrongen")
        print("Ruwanda wist nog van niks totdat ze de volgende dag hoorde van haar vader dat hij een dreigbrief had ontvangen. ")
        print("Wat moet ze doen:")
        print(" A = Vlucht uit afganistan ")
        print(" B = Onderduiken ")
        print(" C = Blijven")
        print(" Type A, B of c")
        Antwoord_1 = input(">>>")
    
        if Antwoord_1 == "A":
            stukje_2 = True
            stukje_1 = False
        
        elif Antwoord_1 == "B":
            stukje_3 = True
            stukje_1 = False
            
        elif Antwoord_1 == "C":
            stukje_4 = True
            stukje_1 = False
        else:
            print("Let op hoofdletters")
            continue

#Stukje_2
        print("Je hebt gekozen om te vluchten uit afghanistan. Slim je vlucht richting het westen.")

    while stukje_2 == True:
        print("Jullie gaan richting het Westen. Maar weten niet hoe jullie daar heen moeten. Iemand uit de groep heeft contact gehad met een mensen smokkelaar.")
        print(" Hij kan jullie richting Spanje laten")
        print("  A. ")
        print("  B. ")
        Antwoord_2 = input(">>>")
        if Antwoord_2 == "A":
            stukje_5 = True
            stukje_2 = False
        
        elif Antwoord_2 == "B":
            stukje_6 = True
            stukje_2 = False
        
        elif Antwoord_1 == "C":
            stukje_4 = True
            stukje_1 = False
        else:
            
            print("Let op hoofdletters")
            print("")
            continue

#Stukje_3
    while stukje_3 == True:
        print("Het is te gevaarlijk voor Ruwanda om onder te duiken. ")
        print(" Ze weet niet wat ze moet doen en praat met haar vader en vrienden erover wat ze het beste kunnen doen.")
        print(" Jullie twijfelen om morgen meteen weg te vluchten. Maar denken er ook aan om de volgende week weg te vluchten.")
        print(" (Wat moeten ze volgens jou doen!)")
        print("  A = Je vlucht de dag erna alsnog weg. ")
        print("  B = Je blijft een week ondergedoken. ")
        Antwoord_3 = input(">>>")
        if Antwoord_3 == "A":
            stukje_6 = True
            stukje_3 = False
        elif Antwoord_3 == "B":
            stukje_5 = True
            stukje_3 = False
        else:
            print("Let op hoofdletters")
            print("")
            continue

#stukje_4
    while stukje_4 == True:
        print(" ")
        print("")
        print("")
        print("")
        print("")
        print("  A. ")
        print("  B. ")
        Antwoord_4 = input(">>>")
        if Antwoord_4 == "A":
            stukje_8 = True
            stukje_4 = False
        elif Antwoord_4 == "B":
            stukje_7 = True
            stukje_4 = False
        else:
            print("")
            print("")
            continue

#stukje_5
    while stukje_5 == True:
        print("")
        stukje_6 = True
        stukje_5 = False

#stukje_6
    while stukje_6 == True:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("  A.")
        print("  B. ")
        Antwoord_6 = input(">>>")
        if Antwoord_6 == "A":
            stukje_10 = True
            stukje_6 = False
        elif Antwoord_6 == "B":
            stukje_9 = True
            stukje_6 = False
        else:
            print("")
            print("")
            continue
# Stukje_7
    while stukje_7 == True:
        print("")
        stukje_8 = True
        stukje_7 = False

# Stukje_8
    while stukje_8 == True:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("  A. ")
        print("  B. ")
        Antwoord_8 = input(">>>")
        if Antwoord_8 == "A":
            stukje_13 = True
            stukje_8 = False
        elif Antwoord_8 == "B":
            stukje_9 = True
            stukje_8 = False
        else:
            print("")
            print("")
            continue   
    print("De Reis")
    print("")
# Stukje_9
    while stukje_9 == True:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("  A. ")
        print("  B. ")
        Antwoord_9 = input(">>>")
        if Antwoord_9 == "A":
            stukje_11 = True
            stukje_9 = False
        elif Antwoord_9 == "B":
            stukje_12 = True
            stukje_9 = False
        else:
            print("")
            print("")
            continue

#stukje_10
    while stukje_10 == True:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("  A. ")
        print("  B. ")
        Antwoord_10 = input(">>>")
        if Antwoord_10 == "A":
            stukje_11 = True
            stukje_10 = False
        elif Antwoord_10 == "B":
            stukje_12 = True
            stukje_10 = False
        else:
            print("")
            continue
# stukje_11
    while stukje_11 == True:
        print("")
        print("")
        print("")
        print("")
        einde_1 = True
        stukje_11 = False

#stukje_12
    while stukje_12 == True:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("  A. ")
        print("  B. ")
        Antwoord_12 = input(">>>")
        if Antwoord_12 == "A":
            stukje_16 = True
            stukje_12 = False
        elif Antwoord_12 == "B":
            stukje_15 = True
            stukje_12 = False
        else:
            print("")
            print("")
            continue
#stukje_13
    
    while stukje_13 == True:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("  A. ")
        print("  B. ")
        Antwoord_13 = input(">>>")
        if Antwoord_13 == "A":
            stukje_14 = True
            stukje_13 = False
        elif Antwoord_13 == "B":
            stukje_18 = True
            stukje_13 = False
        else:
            print("")
            print("")
            continue

#Stukje_14
    while stukje_14 == True:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("  A. ")
        print("  B. ")
        Antwoord_14 = input(">>>")
        if Antwoord_14 == "A":
            stukje_17 = True
            stukje_14 = False
        elif Antwoord_14 == "B":
            stukje_18 = True
            stukje_14 = False
        else:
            print("")
            print("")
            continue

#stukje_15
    while stukje_15 == True:
        print("")
        print("")
        print("")
        print("")
        einde_1 = True
        stukje_15 = False

    #stukje_16
    while stukje_16 == True:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("  A. ")
        print("  B. ")
        Antwoord_16 = input(">>>")
        if Antwoord_16 == "A":
            stukje_17 = True
            stukje_16 = False
        elif Antwoord_16 == "B":
            stukje_18 = True
            stukje_16 = False
        else:
            print("")
            print("")
            continue

    #stukje_17
    while stukje_17 == True:
        print("")
        print("")
        einde_1 = True
        stukje_17 = False

    #stukje_18
    while stukje_18 == True:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("  A. ")
        print("  B. ")
        Antwoord_18 = input(">>>")
        if Antwoord_18 == "A":
            stukje_19 = True
            stukje_18 = False
        elif Antwoord_18 == "B":
            stukje_20 = True
            stukje_18 = False
        else:
            print("")
            print("")
            continue

    #stukje_19
    while stukje_19 == True:
        print("")
        print("")
        print("")
        print(" ")
        stukje_21 = True
        stukje_19 = False

    # stukje_20
    while stukje_20 == True:
        print("")
        print("")
        print("")
        print("")
        stukje_24 = True
        stukje_20 = False



    #stukje 21
    while stukje_21 == True:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("  A. ")
        print("  B. ")
        Antwoord_21 = input(">>>")
        if Antwoord_21 == "A":
            stukje_22 = True
            stukje_21 = False
        elif Antwoord_21 == "B":
            stukje_23 = True
            stukje_21 = False
        else:
            print("")
            print("")
            continue

    #stukje 22
    while stukje_22 == True:
        print("")
        print("")
        print("")
        stukje_27 = True
        stukje_22 = False

    #stukje 23
    while stukje_23 == True:
        print("")
        print("")
        print("")
        stukje_28 = True
        stukje_23 = False


    #einde1
    while einde_1 == True:
        print("Je bent gepakt door de Taliban")
        print("  A. ")
        print("  B. ")
        Antwoord_E1 = input(">>>")
        if Antwoord_E1 == "A":
            inleiding = True
            einde_1 = False
        elif Antwoord_E1 == "B":
            print("")
            print("")
            spelletje = False
            einde_1 = False
        else:
            print("")
            print("")
            continue

    while einde_2 == True:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("  A. ")
        print("  B.")
        Antwoord_E2 = input(">>>")
        if Antwoord_E2 == "A":
            inleiding = True
            einde_2 = False
        elif Antwoord_E2 == "B":
            print("")
            print("")
            spelletje = False
            einde_2 = False
        else:
            print("")
            print("")
            continue

    while einde_3 == True:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("  A. ")
        print("  B. ")
        Antwoord_E3 = input(">>>")
        if Antwoord_E3 == "A":
            inleiding = True
            einde_3 = False
        elif Antwoord_E3 == "B":
            print("")
            print("")
            spelletje = False
            einde_3 = False
        else:
            print("")
            print("")
            continue
        
    while einde_4 == True:
        print("")
        print("  A. ")
        print("  B. ")
        Antwoord_E4 = input(">>>")
        if Antwoord_E4 == "A":
            inleiding = True
            einde_4 = False
        elif Antwoord_E4 == "B":
            print("Bedankt dat je dit spel hebt gespeeld!")
            print("Hoop dat je het leuk vond!")
            spelletje = False
            einde_4 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue
