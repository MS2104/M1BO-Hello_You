from time import sleep

import sys
import os
import random

badEndingNumberAchieved = 0
goodEndingNumberAchieved = 0
running = True

def ending_dead():
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

def ending_survived():
    if goodEndingNumberAchieved == 1:
        print("Je gaat wonen in Istanbul. Je leeft je leven in vrede verder in Istanbul. Je bent misschien geen dokter,")
        print("maar je hebt wel liefde gevonden!")
    elif goodEndingNumberAchieved == 2:
        print("Je asielaanvraag is aangenomen dus kan je in Italië gaan wonen waar je op een wijngaarde gaat werken.")

def start():
    print("TEKSTBASED APPLICATIE M1 BO")
    print("Gemaakt door Milad Sahar uit SD1A")
    print("Oktober 2022")
    sleep(5)
    os.system('clear')

def introsequence():
    print("Jouw naam is Dahmane Kolli")
    print("Je bent een medisch student op de Universiteit van Damascus en bezig met je studie wanneer er oorlog uitbreekt.")
    print("Er is geen andere keuze dan vluchten. Je pakt je spullen in en maakt een plan. Je gaat naar Nederland emigreren.")

def choice1():
    print("x")

while running == True:
    start()
    introsequence()


    ending_dead()
    ending_survived()
    
    while True:
        print("Wil je opnieuw beginnen? (J/N)")
        restart = input("> ")

        if restart == 'J' or restart == 'j':
            break
        elif restart == 'N' or restart == 'n':
            print("Bedankt voor het spelen!")
            sleep(3)
            sys.exit()
        else:
            print("Dat is geen geldig antwoord!")
            continue
