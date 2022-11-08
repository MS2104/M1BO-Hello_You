
from time import sleep
import sys
import os
import random
import keyboard

inventory = ['geld']
balance = 0
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

### DE ECHTE CODE BEGINT HIER!!!!!!!!!!!!!!!!!!!!!!!!

def start():
    print("TEKSTBASED APPLICATIE M1 BO")
    print("Gemaakt door Milad Sahar uit SD1A")
    print("Oktober 2022")
    
    print("DRUK OP SPATIE OM TE BEGINNEN")
    keyboard.wait("spacebar")
    os.system('cls')

def introsequence():
    print('''Jouw naam is Dahmane Kolli
    Je bent een medisch student op de Universiteit van Damascus en bezig met je studie wanneer er opeens aanslagen worden gepleegd.
    Een radicale groep terroristen heeft besloten een staatsgreep te plegen en oorlog breekt uit in Syrië. Je doet de tv aan en kijkt
    naar het nieuws. IS is nu aan de macht en er ontstaat chaos door het hele land. Mensen worden overal door terroristen
    vermoord en winkels worden overvallen. Je kan niet meer naar school omdat er steeds meer mensen worden gegijzeld.
    Mensen vluchtten massaal uit huis naar een betere plek toe, Syrië is niet meer veilig. Je moet vluchten. Je besluit te 
    vluchten naar Nederland in de hoop dat je daar een beter leven kunt opbouwen.

    ''')
    continueFunc()
    
def grabID():
    grabID = input("Ga je je ID meenemen? (J/N)" + "\n" + ">>> ")

    while True:
        if grabID == 'J' or grabID == 'j':
            inventory.append("ID")
            print("Je neemt je ID mee en nog wat andere spullen en gaat het huis uit.")

            continueFunc()
            return
        elif grabID == 'N' or grabID == 'n':
            print("Je laat je ID liggen, pakt je spullen en gaat het huis uit.")

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
    1. via Istanbul naar Rome gaan met het vliegtuig.
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
        beroofd()
    else:
        os.system('cls')
        print("Dat is geen optie!")
        opgeknapt
    
def beroofd():
    print("In de trein naar Antalya ben je gezakkenrold en is je geld en ID gestolen!")
    inventory.clear()

    continueFunc()

def naarIstanbul():
    if "ID" in inventory:
        print("Je hebt je ID meegenomen dus je komt langs de douane!")

        continueFunc()
        inRomeAangekomen()
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
        drugsMeenemen()
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
        eerstovernachten()
        return
    else:
        print("Dat is geen geldig antwoord!")
        continueFunc()
        os.system('cls')
        naarAntalya()

def inRomeAangekomen():
    print("Na een korte reis ben je in Rome aangekomen. Je hebt een beetje rond gekeken door Rome en vindt")
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
    print("Onderweg naar Nederland is de tank leeg gegaan. Maar je realizeert je dat je portomonnee")
    print("Je bent beland in Munich, Duitsland. Maar je hebt geen geld meer en je portomonnee")
    print("is gestolen. Je hebt dus geen geld om te tanken. Je bent wel aangekomen in Parijs!")
    print("Je hebt 2 opties. Je kan snel een baantje doen of je kan naar een tankstation rijden en benzine stelen.")
    print('''
    
    1. Werk zoeken
    2. Benzine stelen.
    
    ''')

    getAJobOrStealFuel = input("(1/2) >>> ")

    if getAJobOrStealFuel == '1':
        print("Je hebt een snelle baan gevonden bij een restaurant, waar je 100 euro hebt verdient.")
        
        continueFunc()
        balance += 100
        tijdOmTeTanken()
    elif getAJobOrStealFuel == '2':
        print("Je rijdt naar een tankstation, vult je tank en rijdt weg. Een half uur later wordt je opgepakt")
        print("door de Franse politie en wordt je in de cel gezet. Na een ondervraging is je asiel getermineerd")
        print("en ben je teruggestuurd naar Syrië.")
        print("SLECHT EINDE 3 GEHAALD!")

        continueFunc()
        retryOrExit()
    else:
        print("Dat is geen geldig antwoord!")
        zelfrijdenmetauto()

def tijdOmTeTanken():
    print("Nu is het tijd om te tanken, maar je kan je auto niet vinden. Na even zoeken heb je hem")
    print("gevonden en onthoud je waar hij staat. Er zijn 3 tankstations met de volgende prijzen:")

    print('''
    1. Shell: €0,83/L
    2. BP: €1,02/L
    3. Esso: €1,15/L    
    
    ''')

    chooseGasStationBrand = input('(Shell/BP/Esso) >>> ')
    
    if chooseGasStationBrand == 'Shell' or 'SHELL' or 'shell':
        print("Je hebt bij de Shell getankt en je tank zit nu vol.")

        continueFunc()
        overdegrens()
    elif chooseGasStationBrand == 'BP' or 'bp':
        print("Bij BP kan je geen 50L tanken!")
        continueFunc
        tijdOmTeTanken()
    elif chooseGasStationBrand == 'Esso' or 'ESSO' or 'esso':
        print("De benzine bij esso is te duur voor 50L")
        continueFunc()
        tijdOmTeTanken()
    return

def drugsMeenemen():
    print("Iemand op straat benadert je, hij biedt je €10,000 als je voor hem drugs meesmokkelt.")
    print("Je kan het geld wel goed gebruiken om een leven op te bouwen in Nederland.")
    print("Doe je het?")

    doejehet = input('(J/N) >>> ')

    if doejehet == 'J' or 'j':
        inventory.append("drugs")
        print("Je neemt het geld aan en de drugs en gaat verder op reis.")
        continueFunc()
        metSmokkelaarMeegaan()
    elif doejehet == 'N' or 'n':
        print("Je slaat het aanbod af.")
        continueFunc()
        metSmokkelaarMeegaan()

def gepaktMetDrugs():
    print("De grenspolitie besloot je te staande te houden en vonden de drugs in je auto.")
    print("Je bent gearresteerd en je asiel is getermineerd.")
    print("SLECHT EINDE 4 GEHAALD!")
    retryOrExit()

def eerstovernachten():
    print("Je wilt eerst overnachten, je hebt immers niet veel geslapen door stress.")
    print("Je kan op 2 plekken slapen, bij de daklozenopvang of op straat.")
    print("1. daklozenopvang")
    print("2. op straat")
    print("")

    whereToSleep = input('(1/2) >>> ')

    if whereToSleep == '1':
        print("Je bent gaan slapen bij een daklozenopvang.")
        naarIstanbulMetTrein()
    elif whereToSleep == '2':
        print("Je besluit op straat te slapen.")
        continueFunc()
        naarIstanbulMetTrein()
    else:
        print("Dat is geen geldig antwoord!")
        eerstovernachten()
    return
    
def naarIstanbulMetTrein():
    print('''Na de overnachting ga je naar het treinstation. Je koopt een kaartje en gaat zitten. Nadat je bent aangekomen
    in Istanbul kom je erachter dat je portomonnee is gestolen in de trein. Je pakt vanaf het treinstation een bus richting
    de grens, maar je komt erachter dat de grens is gesloten. Je kan er niet doorheen omdat je ID kwijt is. Je besluit toch maar
    de smokkelaar om hulp te vragen. Hij gaat akkoord.
    ''')
    continueFunc()
    tochMaarMetSmokkelaarMeegaan()

def tochMaarMetSmokkelaarMeegaan():
    print('''De smokkelaar propt je op een boot samen met 30 anderen. Na een dagenlange bootreis komen jullie gelukkig heel aan vlakbij Athene.
    Daar meld je je aan bij een AZC. Een paar dagen later hoor je van iemand in de kantine dat er een boot naar Catania, Italië gaat.
    Wil je...
    1. met de boot naar Catania gaan?
    2. in het AZC blijven?''')

    boatorazc = input('(1/2) >>> ')

    if boatorazc == '1':
        print("Na een 11 uur lange bootreis kom je veilig aan in Catania, Italië. In Catanie zie je een bus die naar Rome gaat. Je koopt ook")
        print("daarvoor een kaartje.")
        continueFunc()
        inRomeAangekomen()
    elif boatorazc == '2':
        print("Je besluit toch maar in het AZC te blijven. Uiteindelijk kreeg je er genoeg van en besloot je asiel aan te vragen maar het werd")
        print("keer op keer geweigerd. Je zit vast in het AZC want je kan nergens anders meer heen.")

        print("SLECHT EINDE 4 GEHAALD!")
        retryOrExit()
    else:
        print('Dat is geen geldig antwoord!')
        continueFunc()
        tochMaarMetSmokkelaarMeegaan()
    return

def metSmokkelaarMeegaan():
    os.system('cls')
    print("Je stapt op de boot en na 7 uur varen zinkt de boot vlak voor de kust. Je hebt nooit geleerd")
    print("hoe je moest zwemmen dus je verdrinkt.")
    print("SLECHT EINDE 2 GEHAALD!")

    continueFunc()
    retryOrExit()

def overdegrens():
    print("Je komt aan bij de grens. Maar er is grenscontrole.")
    print("De politie nadert je en vraagt om documenten.")

    print("Druk op spatie om je ID te laten zien")
    keyboard.wait('spacebar')

    if "ID" in inventory:
        if "drugs" not in inventory:
            print("Je laat je ID zien en je wordt doorgelaten")

            continueFunc()
            aangekomenInNederland()
        elif "drugs" in inventory:
            print("De politie besluit je auto te doorzoeken.")
            gepaktMetDrugs()

def aangekomenInNederland():
    print("Je bent eindelijk aangekomen in Nederland.")
    TrueEnding()

def ggyoumadeit():
    print("Je neemt de bus naar Amsterdam en na een hele dag reizen ben je aangekomen in Nederland! Hoera!!!!!!!!")
    
    continueFunc()
    TrueEnding()

def TrueEnding():
    print('''Dus, het is je gelukt. Je bent eindelijk aangekomen in Nederland en je asiel is geaccepteerd. Je hebt je aangemeld
    bij een universiteit en je bent aangenomen. Je maakt je medische opleiding af en wordt dokter. Je denkt nog altijd terug aan
    je leven in Syrië maar je bent blij dat je de oorlog bent ontsnapt. Je vindt liefde en krijgt een paar jaar later een kind.
    Je hebt uiteindelijk een mooi leven met een prachtige familie opgebouwd. Je haalt uiteindelijk je 101e verjaardag en
    sterft aan ouderdom na een vredig leven.

    HET EINDE.
    ''')

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