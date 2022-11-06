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

    
def choice1():
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
            choice1()

def choice2():
    print("Je staat buiten je huis en denkt na over hoe je gaat vluchten naar een betere plek...")
    
    print('''Ga je...
    1. met de trein
    2. lopend
    3. met de auto
    (1/2/3)
    ''')

    pickTransportationMethod = input(">>> ")

    while True:
        if pickTransportationMethod == '1':
            print('''Je komt aan op het station maar de trein is al vertrokken.
            Toevallig komt je vriend aan bij het station met de auto en pikt
            hij je op. Jullie gaan samen naar de grens.''')

            continueFunc()
            os.system('cls')
            break
        elif pickTransportationMethod == '2':
            print('''
            Je bent onderweg naar het plein en je vriend rijdt langs met de auto.
            Jullie rijden samen naar de grens.''')

            continueFunc()
            os.system('cls')
            break
        elif pickTransportationMethod == '3':
            badEndingNumberAchieved = 1
            print("Er zat een bom onder de auto en je bent doodgegaan in de explosie.")
            print("")
            retryOrExit()
        else:
            os.system('cls')
            print("Dat is geen geldig antwoord!")
            choice2()
        
def choice3():
    print('''
    Je stopt bij de grens.
    
    Ga je...
    1. bij de grens blijven?
    2. terug naar huis?
    3. door te voet?

    ''')

    whereYouGoin = input ("(1/2/3) >>> ")
    
    while True:
        if whereYouGoin == '1':
            badEndingNumberAchieved = 3
            print("Je bent gegijzeld door terroristen, en opgeleid tot terrorist.")
            print("Tijdens het plegen van een aanslag ben je overleden.")
            retryOrExit()
        elif whereYouGoin == '2':
            badEndingNumberAchieved = 3
            print("Je bent gegijzeld door terroristen, en opgeleid tot terrorist.")
            print("Tijdens het plegen van een aanslag ben je overleden.")
            retryOrExit()
        elif whereYouGoin == '3':
            print("Je besluit vanaf de grens door te lopen en komt na een uur lopen aan bij een treinstation")

            continueFunc()
            os.system('cls')
            break
        else:
            os.system('cls')
            print("Dat is geen geldig antwoord!")
            print("")
            choice3()

def choice4():
    print('''
    Nu je op het treinstation bent ga met de trein verder of niet? (J/N)

    ''')

    goWithTrainOrNah = input(">>> ")

    while True:
        if goWithTrainOrNah == 'J' or goWithTrainOrNah == 'j':
            print("Je pakt de trein naar Gaziantep in Turkije.")

            continueFunc()
            os.system('cls')
            break
        elif goWithTrainOrNah == 'N' or goWithTrainOrNah == 'n':
            badEndingNumberAchieved = 2
            print("Je bent gearresteerd op het station door militaire soldaten op verdenking van terrorisme")
            print("")
            retryOrExit()
        else:
            os.system('cls')
            print("Dat is geen geldig antwoord!")
            print("")
            choice4()

def choice5():
    print('''Na 2 uur ben je aangekomen in Gaziantep. Je herinnert je dat je een vriend hebt")
    die toevallig een huis in Gaziantep heeft. Je vraagt of je mag overnachten bij hem")
    en hij zegt ja. Je eet en gaat slapen. De volgende dag wordt je wakker maar je kan niet")
    altijd blijven. Ga je...
    
    1. verblijven in Gaziantep
    2. naar Italië
    3. naar Griekenland
    
    ''')

    whatDo = input("(1/2/3) >>> ")

    while True:
        if whatDo == '1':
            goodEndingNumberAchieved = 1
            os.system('cls')
            print("Je gaat wonen in Istanbul. Je leeft je leven in vrede verder in Gaziantep.")
            retryOrExit()
        elif whatDo == '2':
            boatorNah = input("Je kan alleen met de boot. Wil je het doen? (J/N) >>> ")

            if boatorNah == 'J' or 'j':
                badEndingNumberAchieved = 6
                print("De boot is onderweg naar Italië gezonken.")
                retryOrExit()
            elif boatorNah == 'N' or 'n':
                print("Je denkt 'vergeet het dan maar' en gaat maar gewoon naar Griekenland.")

                continueFunc()
                choice5_option2()
        elif whatDo == '3':
            choice5_option2()
        else:
            os.system('cls')
            print("Dat is geen geldig antwoord!")
            print("")
            choice5()

def choice5_option2():
    print("Je wilt naar Griekenland maar qua transport heb je maar 2 opties.")
    print('''
    Ga je met de (1) boot of door de (2) bergen?
    ''')

    boatOrMountains = input("(1/2) >>> ")

    while True:
        if boatOrMountains == '1':
            print("Je wordt door een smokkelaar per boot naar Griekenland gebracht en na een")
            print("lange en zware 2 daagse tocht kom je heel aan op het Griekse eiland Lesbos.")
            print("Je wordt opgenomen in een vluchtelingenkamp.")

            continueFunc()
            break
        elif boatOrMountains == '2':
            print("Tijdens je tocht in de bergen wordt je ontvoerd door radicale Koerden.")
            print("Een paar uur later val je bijna in slaap wanneer je iemand hoort praten.")
            print("Je turks is erg slecht maar je verstaat dat ze ergens naar toe willen gaan.")
            print("Je bent op je hoede en hoort ze op gegeven moment rennen.")
            print()
            print("Dit is je gouden kans, besluit je te rennen? (J/N")

            willYouRun = input(">>> ")

            if willYouRun == 'J' or 'j':
                print("")
            elif willYouRun == 'N' or 'n':
                print("Je bent gebleven en de koerden zijn terug gekomen. Ze maken jou tot slaaf en je")
                print("sterft 2 weken later aan complicaties door de mishandelingen.")

                retryOrExit()
            else:
                os.system('cls')
                print("Dat is geen geldig antwoord!")
                print("")
                choice5_option2()

def choice5_option3():
    print("")



def main():
    # Start
    start()
    introsequence()

    # Het daadwerkelijke spel
    choice1()
    choice2()
    choice3()
    choice4()
    choice5()

while running == True:
    main()

    retryOrExit()