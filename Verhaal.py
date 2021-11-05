#KEUZES
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
        print("Mijn naam is Max Montanus. Ik heb een verhaal geschreven over een vluchteling genaamd Ruwanda. Ik hoop dat je goede keuze's maakt in het verhaal.")
        print("(druk op je enter toets om verder te gaan)")
        Druk_op_enter_1 = input(">>>")
        print("")
        stukje_1 = True
        inleiding = False
    
#start
    while stukje_1 == True:
        print(" Voordat de taliban binnendrong: ")
        print(" Ruwanda was aan het werk in haar eigen Beauty salon totdat ze ineens inmensen knallen hoorde. De taliban was binnen gedrongen")
        print(" Ruwanda wist nog van niks totdat ze de volgende dag hoorde van haar vader dat hij een dreigbrief had ontvangen. Jullie weten niet wat jullie moeten doen")
        print(" Ze twijfelen om meteen te vluchten om onder te duiken of gewoon te blijven en afwachten.")
        print(" Wat moet ze doen:")
        print(" A = Vlucht uit afganistan ")
        print(" B = Onderduiken ")
        print(" C = Blijven")
        print(" Type A, B of C")
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

#Keuze Vluchten #2

    while stukje_2 == True:
        print(" Jullie willen richting het Westen. Maar weten niet hoe jullie daar heen moeten. Iemand uit de groep heeft contact gehad met een mensen smokkelaar.")
        print(" Hij kan jullie richting Spanje meenemen alleen dat is een van de gevaarlijkste en langste route's die er is. ")
        print(" Jullie hebben te horen gekregen dat het ook via Griekenland kan. Dat is veiliger en korter.  ")
        print(" Welke optie moeten ze pakken?")
        print("  A = Via Spanje")
        print("  B = Via Griekenland")
        Antwoord_2 = input(">>>")
        if Antwoord_2 == "A":
            stukje_7 = True
            stukje_2 = False
        
        elif Antwoord_2 == "B":
            stukje_9 = True
            stukje_2 = False
        
        else:
            
            print("Let op hoofdletters")
            print("")
            continue

#Keuze onderduiken #3
    while stukje_3 == True:
        print(" Het is te gevaarlijk voor Ruwanda en haar vader om onder te duiken. ")
        print(" Ze weet niet wat ze moet doen en praat met haar vader en vrienden erover wat ze het beste kunnen doen.")
        print(" Jullie twijfelen om morgen meteen weg te vluchten. Maar denken er ook aan om de volgende week weg te vluchten.")
        print(" (Wat moeten ze volgens jou doen!)")
        print("  A = Je vlucht de dag erna alsnog weg. ")
        print("  B = Je blijft een week ondergedoken. ")
        Antwoord_3 = input(">>>")
        if Antwoord_3 == "A":
            stukje_7 = True
            stukje_3 = False
            continue 
        elif Antwoord_3 == "B":
            einde_1 = True
            stukje_3 = False
            continue
        else:
            print("Let op hoofdletters")
            print("")
            continue

#stukje_4 #stopt hier
    while stukje_4 == True:
        print(" Jullie kozen om te blijven maar de taliban heeft jullie al snel te pakken. Ruwanda's vader word meegenomen naar een andere cel dan waar zij zit. ")
        print(" Ruwanda komt er na een tijdje achter dat haar vader is vermoord. Ruwanda blijft gevangen zolang de Taliban de baas is over afghanistan")
        Antwoord_4 = input(">>>")
        if Antwoord_4 == "":
            einde_1 = True
            continue
        else:
            print("Let op hoofdletters")
            print("")
            continue
        

#stukje_5 #vervolg op stuk 2
    while stukje_5 == True:
        print(" Jullie vluchten toch weg. Iemand uit de groep heeft contact gehad met een mensen smokkelaar.")
        print(" Hij kan jullie richting Spanje meenemen alleen dat is een van de gevaarlijkste en langste route's die er is. ")
        print(" Jullie hebben te horen gekregen dat het ook via Griekenland kan. Dat is veiliger en korter.  ")
        print(" Welke optie moeten ze pakken?")
        print("  A = Via Spanje ")
        print("  B = Via Griekenland")
        Antwoord_2 = input(">>>")
        if Antwoord_2 == "A":
            stukje_7 = True
            stukje_2 = False
        
        elif Antwoord_2 == "B":
            stukje_8 = True
            stukje_2 = False
        
        else:
            
            print("Let op hoofdletters")
            print("")
            continue

#stukje_6 vervolg op stuk 3 A
    while stukje_6 == True:
        print(" Jullie vluchten toch weg. Iemand uit de groep heeft contact gehad met een mensen smokkelaar.")
        print(" Hij kan jullie richting Spanje meenemen alleen dat is een van de gevaarlijkste en langste route's die er is. ")
        print(" Jullie hebben te horen gekregen dat het ook via Griekenland kan. Dat is veiliger en korter.  ")
        print(" Welke optie moeten ze pakken?")
        print("  A = Via Spanje ")
        print("  B = Via Griekenland")
        Antwoord_6 = input(">>>")
        if Antwoord_6 == "A":
            stukje_7 = True
            stukje_6 = False
        elif Antwoord_6 == "B":
            stukje_8 = True
            stukje_6 = False
        else:
            print("")
            print("")
            continue


# Stukje_7 stopt hier
while stukje_7 == True:
        print(" Deze route naar Spanje is veel te gevaarlijk en te lang. Het eten wat jullie hadden meegenomen is op en zijn er nog lang niet")
        print(" Na 2 dagen kan niemand meer en iedereen overlijd door vermoeidheid. ")
        print("")
        Antwoord_2 = input(">>>")
        if Antwoord_2 == "":
            einde_2 = True
            continue
        else:
            
            print("Let op hoofdletters")
            print("")
            continue

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
# Stukje_9
while stukje_9 == True:
        print(" Jullie gaan richting Griekenland. Een korte route over zee en minder gevaarlijk.")
        print(" Bij aankomst in griekenland moeten jullie snel wegwezen. Griekenland Wilt geen vluchteling in hun land en probeert iedere vluchteling op te pakken.")
        print(" Gelukkig heeft de man die jullie helpt snel het goede vervoer kunnen contacteren. Alleen weten ze nog niet precies waar jullie heen gaan.")
        print(" Ze twijfelen om naar Belgie, Nederland of Duitseland te rijden.")
        print("  A = Belgie")
        print("  B = Nederland")
        print("  C = Duitseland")
        Antwoord_9 = input(">>>")
        
        if Antwoord_9 == "A":
            stukje_11 = True
            
            stukje_9 = False
        elif Antwoord_9 == "B":
            stukje_12 = True
            stukje_9 = False
        
        elif Antwoord_9 == "C":
            stukje_13 = True
            stukje_9 = False
        
        else:
            print("Let op hoofdletters")
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
# stukje_11 Belgie
while stukje_11 == True:
        print(" Jullie wisten nog niet naar waar jullie gebracht werden. Jullie werden met ze alle in een vrachtwagen gegooid.")
        print(" Het was erg donker in de vrachtwagen de kleppen waren dicht en er kwam geen zonlicht naar binnen.")
        print(" Toen de luiken open gingen wisten jullie nog niks en toen werd er verteld dat jullie in België waren.")
        print(" Jullie bleven hier en kregen asiel. Na 2 maanden kon Ruwanda's vader zijn vrouw uit afghanistan krijgen. Jullie starten met ze alle opnieuw in België!")
        einde_1 = True
        stukje_11 = False

#stukje_12 nederland
while stukje_12 == True:
        print(" Jullie wisten nog niet naar waar jullie gebracht werden. Jullie werden met ze alle in een vrachtwagen gegooid.")
        print(" Het was erg donker in de vrachtwagen de kleppen waren dicht en er kwam geen zonlicht naar binnen.")
        print(" Toen de luiken open gingen wisten jullie nog niks en toen werd er verteld dat jullie in Nederland waren.")
        print(" Jullie wisten niet zeker of jullie moesten blijven of ergens anders heen wouden.")
        print(" Blijven jullie of gaan jullie verder?")
        print("  A = Blijven ")
        print("  B = Jullie reizen verder ")
        Antwoord_12 = input(">>>")
        if Antwoord_12 == "A":
            stukje_14 = True
            stukje_12 = False
        elif Antwoord_12 == "B":
            stukje_15 = True
            stukje_12 = False
        else:
            print(" Let op hoofdletters!")
            print("")
            continue
#stukje_13 duitseland
    
while stukje_13 == True:
        print(" Jullie wisten nog niet naar waar jullie gebracht werden. Jullie werden met ze alle in een vrachtwagen gegooid.")
        print(" Het was erg donker in de vrachtwagen de kleppen waren dicht en er kwam geen zonlicht naar binnen.")
        print(" Toen de luiken open gingen wisten jullie nog niks en toen werd er verteld dat jullie in Duitseland waren.")
        print(" Jullie twijfelde heel erg over dit land.")
        print(" De taal is extreem moeilijke wisten niks over dit land")
        print(" Blijven jullie of gaan jullie richting Nederland.")
        print("  A = In Duitseland blijven. ")
        print("  B = Naar Nederland reizen. ")
        Antwoord_13 = input(">>>")
        if Antwoord_13 == "A":
            stukje_16 = True
            stukje_13 = False
        elif Antwoord_13 == "B":
            stukje_19 = True
            stukje_13 = False
        else:
            print(" Let op hoofdletters!")
            print("")
            continue

#Stukje_14
while stukje_14 == True:
        print(" Goeie keuze!")
        print(" Nederland is een goed land voor vluchtelingen. Jullie zijn naar vluchtelingenwerk Nederland gestuurd.")
        print(" Hun helpen mensen die zijn gevlucht uit hun geboorte land. Met een huis zoeken en de nederlandse taal leren")
        print(" Ze konden ook helpen met de moeder van Ruwanda naar, maar de vader van Ruwanda wou het niet uit handen geven want hij was bang")
        print(" Wat zou moeten ze doen?")
        print("  A = Zelf blijven proberen. ")
        print("  B = Uit handen geven aan vluchtelingen werk. ")
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
        print(" Jullie kozen ervoor om toch nn Duitseland te blijven.")
        print(" Jullie wisten niet waar te beginnen en gingen naar het dichtsbijzijnde politie bureau")
        print(" Die namen jullie mee naar een gebouw maar jullie wisten niet wat voor gebouw. Wat dus blijkbaar een gevangenis was.")
        print(" Ruwanda en haar vader merkte het snel op en vluchten weg voor de Duitse politie. De rest van jullie groep was te laat.")
        print(" Jullie vluchten zo ver mogelijke en vragen aan iemand langs de weg voor een lift in het engels.")
        print(" Waar moet ze jullie heen brengen?")
        print("  A = Berlijn station ")
        print("  B = Dichtsbijzijnde snelweg.")
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
        print(" Een hele goede keuze om het uit handen te geven! ")
        print(" Jullie hebben gevraagd aan Vluchtelingenwerk Nederland om te helpen met jullie moeder naar Nederland halen.")
        print(" Zijn meteen aan de slag gegaan.")
        print(" De volgende dag werden jullie naar een kantoor gestuurd van de Nederlandse ambassade.")
        print(" Ze vroegen om de naam en woonplaats etc.")
        print(" Ruwanda's vader had nogsteeds een onderbuik gevoel maar gaf het toch. ")
        print(" Hij moest week wachten. Om te horen hoe of wat.")
        print(" (wat voor nieuws krijgen jullie te horen?")
        print("  A = Goed nieuws!")
        print("  B = Slecht nieuws :(")
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

# stukje_19
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
        print("")
        print("Dit was het einde!")
        print("Wil je nog een keertje?")
        print("")
        print(" A = Ja!")
        print(" B = Nee")
        Antwoord_E1 = input(">>>")
        if Antwoord_E1 == "A":
            inleiding = True
            einde_1 = False
        elif Antwoord_E1 == "B":
            print("Bedankt voor het spelen van mijn spel!")
            print("Cya later!")
            spelletje = False
            einde_1 = False
        else:
            print("Let op hoofdletters")
            print("")
            continue
#einde2
while einde_2 == True:
        print(" Deze route naar Spanje is veel te gevaarlijk en te lang. Het eten wat jullie hadden meegenomen is op en zijn er nog lang niet")
        print(" Na 2 dagen kan niemand meer en iedereen overlijd door vermoeidheid. ")
        print("")
        print("Dit was het einde!")
        print("Wil je nog een keertje?")
        print("")
        print(" A = Ja!")
        print(" B = Nee")
        Antwoord_E2 = input(">>>")
        if Antwoord_E2 == "A":
            inleiding = True
            einde_2 = False
        elif Antwoord_E2 == "B":
            print("Bedankt voor het spelen van mijn spel!")
            print("Cya later!")
            spelletje = False
            einde_2 = False
        else:
            print("Let op hoofdletters")
            print("")
            continue
#einde3
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
#einde4
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
