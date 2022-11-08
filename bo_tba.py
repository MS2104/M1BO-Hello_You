from re import X
from time import sleep

import sys
import os
import random
import keyboard

inventory = []
badEndingNumberAchieved = 0
goodEndingNumberAchieved = 0
isDead = False
running = True

def continueFunc():
    print("")
    print("DRUK OP SPATIE OM DOOR TE GAAN")
    keyboard.wait("spacebar")
    os.system('cls')

def retryOrExit():
    while True:
        print("")
        print("Wil je opnieuw beginnen? (J/N)")
        restart = input("> ")

        if restart == 'J' or restart == 'j':
            os.system('cls')
            main()
        elif restart == 'N' or restart == 'n':
            print("Bedankt voor het spelen!")
            sleep(3)
            sys.exit()
        else:
            print("Dat is geen geldig antwoord!")
            continue

def ending_dead():
    if isDead == True:
        if badEndingNumberAchieved == 1:
            print("Er zat een bom onder de auto en je bent doodgegaan in de explosie.")
        elif badEndingNumberAchieved == 2:
            print("Je bent doodgeschoten door militaire soldaten op verdenking van terrorisme")
        elif badEndingNumberAchieved == 3:
            print("Je bent gegijzeld door terroristen, en opgeleid tot terrorist.")
            print("Tijdens het plegen van een aanslag ben je overleden.")
        elif badEndingNumberAchieved == 4:
            print("Je sterft de hongerdood!")
        elif badEndingNumberAchieved == 5:
            print("Je wordt gespot en vermoord door radicale koerden.")
        elif badEndingNumberAchieved == 6:
            print("De boot zinkt met jou erin. Je verdrinkt.")
        elif badEndingNumberAchieved == 7:
            print("Je wordt beroofd en vermoord.")
        elif badEndingNumberAchieved == 8:
            print("De boot zinkt voor de kust en je verdrinkt.")
        else:
            return

def ending_survived():
    if goodEndingNumberAchieved == 1:
        print("Je gaat wonen in Istanbul. Je leeft je leven in vrede verder in Istanbul.")
    elif goodEndingNumberAchieved == 2:
        print("Je asielaanvraag is aangenomen dus kan je in Italië gaan wonen waar je op een wijngaarde gaat werken.")
    elif goodEndingNumberAchieved == 3:
        print("")
    else:
        return

### DE ECHTE CODE BEGINT HIER!!!!!!!!!!!!!!!!!!!!!!!!

def start():
    print("TEKSTBASED APPLICATIE M1 BO")
    print("Gemaakt door Milad Sahar uit SD1A")
    print("Oktober 2022")
    
    print("DRUK OP SPATIE OM TE BEGINNEN")
    keyboard.wait("spacebar")
    os.system('cls')

def introsequence():
    print("Jouw naam is Dahmane Kolli")
    print("Je bent een medisch student op de Universiteit van Damascus en bezig met je studie wanneer er oorlog uitbreekt.")
    print("Er is geen andere keuze dan vluchten. Je pakt je spullen in en maakt een plan. Je gaat naar Nederland vluchten.")
    print("")
    continueFunc()
    
def grabID():
    grabID = input("Ga je je ID meenemen? (J/N)" + "\n" + ">>> ")

    while True:
        if grabID == 'J' or grabID == 'j':
            inventory.append("ID")
            print("Je neemt je ID mee.")

            continueFunc()
            return
        elif grabID == 'N' or grabID == 'n':
            print("Je laat je ID liggen en gaat het huis uit.")

            continueFunc()
            return
        else:
            os.system('cls')
            print("Dat is geen geldig antwoord!")
            grabID()

def q1():
    print("Je staat buiten je huis en denkt na over hoe je gaat vluchten naar een betere plek...")
    
    print('''Ga je...
    1. Turkije
    2. Egypte
    (1/2)
    ''')

    pickTransportationMethod = input(">>> ")

    while True:
        if pickTransportationMethod == '1':
            print('Je start de motor en rijdt de snelweg op. Je rijdt via Libanon naar Turkije. Na 8 uur zit je rit erop en ben je in Gaziantep.')

            continueFunc()
            os.system('cls')
            inGaziantep()
        elif pickTransportationMethod == '2':
            print("Nou, je wilt naar Egypte, maar dat kan dus niet omdat je dan om Israël heen moet rijden.")
            print("Je moet dus naar Turkijë")

            continueFunc()
            os.system('cls')
            inGaziantep()
        else:
            os.system('cls')
            print("Dat is geen geldig antwoord!")
            q1()

def inGaziantep():
    print("Je bent aangekomen in Gaziantep. Eenmaal in Gaziantep voel je je niet helemaal lekker.")

    goToDoctor = input('Wil je naar een dokter gaan? (J/N) >>> ')

    if goToDoctor == 'J' or 'j':
        print("Je gaat naar de dokter.")

        continueFunc()
        opgeknapt()
    elif goToDoctor == 'N' or 'n':
        print("Je bent niet naar de dokter gegaan, en daarom ben je tragisch aan een onbekende")
        print("ziekte gestorven. Rust in Vrede.")
        print("SLECHT EINDE 1 BEREIKT!")

        continueFunc()
        retryOrExit()
    else:
        os.system('cls')
        print("Dat is geen geldig antwoord!")
        inGaziantep()

def opgeknapt():
    print('''
    Je bent naar de dokter gegaan en je bent opgeknapt en klaar voor de reis!
    Maar je tank is bijna leeg en nog goed voor 10 km. Je herinnert dat je nog
    een vriend hebt in Gaziantep. Hij biedt je aan om te helpen met ergens naar toe te gaan

    Je hebt 2 opties. Je kan:
    1. via Istanbul naar Rome gaan met het vliegtuig
    2. naar Antalya gaan met de Trein.
    ''')

    istanbulOfAntalya = input("(1/2) >>> ")

    if istanbulOfAntalya == '1':
        print("Je gaat dus naar Rome met het vliegtuig.")
        continueFunc()
        naarIstanbul()
    elif istanbulOfAntalya == '2':
        print("Je gaat naar Antalya met de trein.")
        continueFunc()
        naarAntalya()
    else:
        os.system('cls')
        print("Dat is geen optie!")
        opgeknapt

def naarIstanbul():
    if "ID" in inventory:
        print("Je hebt je ID meegenomen dus je komt langs de douane!")

        continueFunc()
        inIstanbulAangekomen()
    else:
        print("Je kan niet met het vliegtuig omdat je je ID niet mee hebt genomen!")

        continueFunc()
        naarAntalya()
    return

def naarAntalya():
    print("Na een lange treinreis ben je aangekomen in Antalya. Antalya is een prachtige stad maar")
    print("Je hebt via via gehoord dat je toch Italië kan binnen komen. Je vriend uit")
    print("Gaziantep heeft je in contact gebracht met een mensensmokkelaar. Je zit te")
    print("twijfelen... zal ik met de smokkelaar meegaan, in Antalya blijven of zelf verder reizen?")

    print('''
    1. Met de smokkelaar meegaan
    2. In Antalya blijven
    3. in m'n eentje verder reizen.
    ''')

    meegaanmetdesmokkelaar = input(">>> ")

    if meegaanmetdesmokkelaar == '1':
        print("Je gaat met de smokkelaar mee. Hij belooft je naar Griekenland te brengen")
        continueFunc()
        metSmokkelaarMeegaan()
    elif meegaanmetdesmokkelaar == '2':
        os.system('cls')
        print("Je bent de oorlog eigenlijk wel ontsnapt. Hier in Antalya is het veilig genoeg.")
        print("Het is een prachtige stad en een goed genoege plek om voor jou een toekomst op te bouwen.")

        print("GOED EINDE 1 GEHAALD!")
        continueFunc()
        retryOrExit()
    elif meegaanmetdesmokkelaar == '3':
        print("Je gaat zelf maar verder reizen. Je volgende bestemming wordt Istanbul. Hopelijk kan je")
        print("vanuit Istanbul verder naar Europa!")
        continueFunc()
        zelfReizen()
        return
    else:
        print("Dat is geen geldig antwoord!")
        sleep(3)
        os.system('cls')
        naarAntalya()

def inIstanbulAangekomen():
    print("Na een korte vliegreis ben je in Rome aangekomen. Je hebt een beetje rond gekeken door Rome en vindt")
    print("een baantje bij een restaurant. Ga je ...")

    print('''
    1. de baan nemen en in Rome vestigen.
    2. asiel aanvragen en hopelijk naar Nederland gaan.

    ''')

    jobOrContinue = input("(1/2) >>> ")

    if jobOrContinue == '1':
        print("Je neemt de baan en lijdt je leven in Rome in vrede.")
        print("GOED EINDE 2 GEHAALD!")

        continueFunc()
        retryOrExit()
    elif jobOrContinue == '2':
        os.system('cls')
        naarNederland()

def naarNederland():
        print("Je neemt de baan alsnog aan om geld te sparen voor je asielaanvraag.")
        print("Een paar maanden later ga je op reis naar Nederland met het geld")
        print("dat je hebt opgespaard en doe je bij een gemeente een asielaanvraag.")
        print("De aanvraag is geaccepteerd maar je moet nu nog naar Nederland zien te komen.")

        print('''
        Doe je dit door:
        1. een auto te kopen en zelf te rijden naar Amsterdam
        2. de bus te nemen
        ''')

        joc2 = input("")

        if joc2 == '1':
            zelfrijdenmetauto()
        elif joc2 == '2':
            ggyoumadeit()
        else:
            print("Dat is geen geldig antwoord!")
            continueFunc()
            naarNederland()

def zelfrijdenmetauto():
    print("Je bent onderweg naar Amsterdam in Frankrijk aangereden. Je bent doodgegaan.")
    print("SLECHT EINDE 3 GEHAALD!")

    continueFunc()
    retryOrExit()

def zelfReizen():
    print("")

def metSmokkelaarMeegaan():
    os.system('cls')
    print("Je stapt op de boot en na 7 uur varen zinkt de boot vlak voor de kust. Je hebt nooit geleerd")
    print("hoe je moest zwemmen dus je verdrinkt.")
    print("SLECHT EINDE 2 GEHAALD!")

    continueFunc()
    retryOrExit()

def ggyoumadeit():
    print("Je neemt de bus naar Amsterdam en na een hele dag reizen ben je aangekomen in Nederland! Hoera!!!!!!!!")
    print("HET CORRECTE EINDE GEHAALD!!!!!!!!!!!!!!!!!!!!!")
    
    continueFunc()
    retryOrExit()

def main():
    # Start
    start()
    introsequence()

    # Het daadwerkelijke spel
    grabID()

    q1()

while running == True:
    main()

    retryOrExit()