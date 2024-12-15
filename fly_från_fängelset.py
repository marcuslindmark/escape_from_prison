# ***** IMPORT AV EXTERNA MODULER TILL SPELET *****
# msvcrt behövs till pausfunktionen 
# os behövs för att kunna rensa skärmen
# random behövs för att lägga in slump i spelet
import msvcrt, os, random


# ***** VARIABLER I SPELET *****
spelet_körs = True                  # Används i spelets huvudloop och är True om spelet ska fortsätta köras
aktuellt_rum = "rum_1"              # Håller reda på i vilket rum spelaren befinner sig i

# RUM 1
tagit_nyckeln = False               # Kontrollerar om nyckeln finns i rummet

# RUM 3
tagit_barnteckningen = False        # Kontrollerar om barnteckningen finns i rummet
gåtan_löst = False                  # Kontrollerar om spelaren skrivit rätt svar i datorterminalen            

# HUVUDMENYN
gör_menyval = True

# ***** DICTIONARIES I SPELET *****
# Här är alla dictionaries (uppslagsverk) som används i spelet.

# ***** INVENTORY *****
# Inventory är en dictionary som håller reda på vilka föremål som spelaren bär på.
inventory = {}


# Dictionary som håller reda på om spelaren har besökt rummet tidigare
varit_i_rummet = {
    "rum_1": False,
    "rum_2": False,
    "rum_3": False,
    "rum_4": False,
    "rum_5": False,
}


# ***** FUNKTIONER I SPELET *****

### PAUSFUNKTION ###
# Funktion som lägger in en paus i spelet            
def tryck_på_valfri_tangent():            
    print("\nTryck på valfri tangent för att fortsätta...")
    msvcrt.getch()  # Väntar på att användaren trycker på en tangent
    print ("\n")


### RENSA SKÄRMEN ###
# Funktion som använder os modulen för att rensa skärmen.
def rensa_skärmen():
    # Om Windows är operativsystemet körs det första kommandot
    if os.name == 'nt':
        os.system('cls')
    else:                   
        os.system('clear')          # För Mac eller Linux körs istället clear


### RUM 1 ###
# Funktion som hanterar allt som händer i rum 1
def rum_1(aktuellt_rum, tagit_nyckeln):
    
    spelaren_väljer = True

    while (spelaren_väljer, tagit_nyckeln):
        # Rensar skärmen innan beskrivningen av rummet skrivs ut på nytt.
        rensa_skärmen()
    
        # Beskrivningen av rummet ändras om spelaren har varit där tidigare
        if varit_i_rummet["rum_1"]:
            print("Du återvänder till det smutsiga och kala rummet utan fönster.")
        else:
            print(f"Du befinner dig i ett smutsigt och kalt rum utan fönster med en dörr framför dig.")
            print ("Det luktar unket här och du förstår att någon eller något har tagit dig till fånga.")
        
        # Markera att spelaren har varit i rummet
        varit_i_rummet["rum_1"] = True

        print ("1. Öppna dörren.")
        print ("2. Genomsöka rummet.")
        print ("3. Se vad du bär på.")
        spelarens_val = input("Vad vill du göra? ")
        if (spelarens_val == "1"):
            # Kontrollera om spelaren har nyckeln
            if "nyckel" in inventory:
                print("\nDu använder nyckeln för att låsa upp dörren. Dörren öppnas!")
                print("Du lägger tillbaka nyckeln i dina rymliga fickor.")
                
                # Anropar pausfunktionen
                tryck_på_valfri_tangent()

                # Avslutar while-loopen
                spelaren_väljer = False 
                
                # Sätter aktuellet rum till rummet som spelaren går in i
                aktuellt_rum = "rum_2"
                
                # Returnerar det nya värdet för aktuellt_rum till spelloopen
                return aktuellt_rum, tagit_nyckeln
            else:
                print("\nDörren är låst. Du behöver en nyckel för att öppna den.")
                
                # Anropar pausfunktionen
                tryck_på_valfri_tangent()
        
        elif (spelarens_val == "2"):
            if tagit_nyckeln == False:
                # Ändrar så att nyckeln inte längre finns i rummet
                tagit_nyckeln = True
                
                # Lägger till föremålet "nyckel" till det som spelaren bär på.
                inventory["nyckel"] = "en rostig gammal nyckel."
                                   
                # Berättar för spelaren vad som händer
                print(f"\nDu hittar {inventory['nyckel']}")
                
                # Anropar pausfunktionen
                tryck_på_valfri_tangent()                
            else:
                print("\nDet finns inget mer att hitta här.")
                
                # Anropar pausfunktionen
                tryck_på_valfri_tangent()
        elif (spelarens_val == "3"):
            if inventory:
                print("\nDu tittar i dina fickor och hittar följande:")
                for föremål, beskrivning in inventory.items():
                    print(f"- {föremål.capitalize()} ({beskrivning})")
            else:
                print("\nDu tittar i dina fickor, men de är tomma.")
            
            # Anropar pausfunktionen
            tryck_på_valfri_tangent()   

### RUM 2 ###
# Funktion som hanterar allt som händer i rum 2
def rum_2(aktuellt_rum): 
    spelaren_väljer = True
    while (spelaren_väljer):
         # Rensar skärmen innan beskrivningen av rummet skrivs ut på nytt.
        rensa_skärmen()
        
        # Beskrivningen av rummet ändras om spelaren har varit där tidigare
        if varit_i_rummet["rum_2"]:
            print("Återigen är du i det mörka och fuktiga rummet med märkena på väggarna.")
        else:
            print(f"Du kommer in i en mörk och fuktig korridor med märken på väggarna.")
            
        # Markera att spelaren har varit i rummet
        varit_i_rummet["rum_2"] = True
        
        print ("1. Gå höger.")
        print ("2. Gå vänster.")
        print ("3. Bakåt till cellen igen.") 
        print ("4. Titta på märkena på väggarna.")
        print ("5. Se vad du bär på.")
        spelarens_val = input("Vad vill du göra? ")
        if (spelarens_val == "1"):
            print("\nDu går åt höger.")

            # Anropar pausfunktionen
            tryck_på_valfri_tangent()

            # Avslutar while-loopen
            spelaren_väljer = False 
                
            # Sätter aktuellet rum till rummet som spelaren går in i
            aktuellt_rum = "rum_3"
                
            # Returnerar det nya värdet för aktuellt_rum till spelloopen
            return aktuellt_rum
        elif (spelarens_val == "2"):
            print ("\nDu går åt vänster.")
            
            # Anropar pausfunktionen
            tryck_på_valfri_tangent()
        
            # Avslutar while-loopen
            spelaren_väljer = False 
                
            # Sätter aktuellet rum till rummet som spelaren går in i
            aktuellt_rum = "rum_4"
                
            # Returnerar det nya värdet för aktuellt_rum till spelloopen
            return aktuellt_rum
        elif (spelarens_val == "3"):
        
            # Sätter aktuellt rum till det rum som spelaren vill gå till
            aktuellt_rum = "rum_1"
            
            # Skickar tillbaka aktuellt rum till spelloopen.
            return aktuellt_rum  
        elif (spelarens_val == "4"):
            print ("\nNär du tittar närmare på märkena påminner den ena") 
            print("om en streckgubbe som håller i något fyrkantigt och pekar till höger.")
            print("Det vänstra ser ut som en indian som är på jakt efter något.")
            # Anropar pausfunktionen
            tryck_på_valfri_tangent()
        elif (spelarens_val == "5"):
            if inventory:
                print("\nDu tittar i dina väldigt rymliga fickor och hittar följande:")
                for föremål, beskrivning in inventory.items():
                    print(f"- {föremål.capitalize()} ({beskrivning})")
            else:
                print("\nDu tittar i dina fickor, men de är tomma.")
            
            # Anropar pausfunktionen
            tryck_på_valfri_tangent()   


### RUM 3 ###
# Funktion som hanterar allt som händer i rum 3
def rum_3(aktuellt_rum, tagit_barnteckningen, gåtan_löst): 
    spelaren_väljer = True
    
    while (spelaren_väljer):
         # Rensar skärmen innan beskrivningen av rummet skrivs ut på nytt.
        rensa_skärmen()
        
        # Beskrivningen av rummet ändras om spelaren har varit där tidigare
        if varit_i_rummet["rum_3"]:
            print("Återigen är du i rummet med datorterminalen och dörren till vänster.")
        else:
            print("Du kommer in i ett rum med en dörr till vänster.")
            print("Bredvid dörren ser du en datorterminal.")
            print("Bakom dig har du dörren tillbaka till korridoren du kom ifrån.")
        # Markera att spelaren har varit i rummet
        varit_i_rummet["rum_3"] = True
        
        print ("1. Gå vänster.")
        print ("2. Gå bakåt till korridoren igen.")
        print ("3. Genomsök rummet.")
        print ("4. Använd datorterminalen.")
        print ("5. Se vad du bär på.")
        spelarens_val = input("Vad vill du göra? ")
        if (spelarens_val == "1"):
            if (gåtan_löst == False):
                print("\nDörren är låst.")
                
                # Anropar pausfunktionen
                tryck_på_valfri_tangent()
            else:
                print("\nDörren är öppen och du går igenom den.")    
            
                # Anropar pausfunktionen
                tryck_på_valfri_tangent()

                # Avslutar while-loopen
                spelaren_väljer = False 
                
                # Sätter aktuellet rum till rummet som spelaren går in i
                aktuellt_rum = "rum_5"
                
                # Returnerar det nya värdet för aktuellt_rum till spelloopen
                return aktuellt_rum, tagit_barnteckningen, gåtan_löst
        elif (spelarens_val == "2"):
            print ("\nDu går tillbaka till korridoren.")
            
            # Anropar pausfunktionen
            tryck_på_valfri_tangent()

            # Sätter aktuellt rum till det rum som spelaren vill gå till
            aktuellt_rum = "rum_2"
            
            # Skickar tillbaka aktuellt rum till spelloopen.
            return aktuellt_rum, tagit_barnteckningen, gåtan_löst
        elif (spelarens_val == "3"):
            if (tagit_barnteckningen == False): 
                print("Du hittar en barnteckning på någon som badar.")
                behålla_teckning = input("Vill du behålla den?(ja/nej)" ).lower()
                if (behålla_teckning == "ja"):
                    print ("Du viker ihop teckningen och lägger den i din ficka.")
                    tagit_barnteckningen = True    
                    # Lägger till föremålet "barnteckning" till det som spelaren bär på.
                    inventory["barnteckning"] = "en barnteckning på någon som badar."
            else:
                print("Det finns inget mer att hitta här.")        
            
            # Anropar pausfunktionen
            tryck_på_valfri_tangent()
        elif (spelarens_val == "4"):
            print ("\nDu slår på datorn och möts av en skärm med frågan:")
            print ("\nVad blir blötare ju mer man torkar? ")
            svaret_på_gåtan = input ("Vad svarar du? ").lower()
    
            if (svaret_på_gåtan == "handduk" or svaret_på_gåtan == "handduken" or svaret_på_gåtan == "handuken" or svaret_på_gåtan == "handuk"):
                print("Du har svarat rätt står det på skärmen.")
                print("Du har ett märkligt surrande från dörren till vänster.")
                gåtan_löst = True
            else:
                print("Du svarade fel står det på skärmen.")
            # Anropar pausfunktionen
            tryck_på_valfri_tangent()
        elif (spelarens_val == "5"):
            if inventory:
                print("\nDu tittar i dina jättestora fickor och hittar följande:")
                for föremål, beskrivning in inventory.items():
                    print(f"- {föremål.capitalize()} ({beskrivning})")
            else:
                print("\nDu tittar i dina fickor, men de är tomma.")
            
            # Anropar pausfunktionen
            tryck_på_valfri_tangent()       

### RUM 4 ###
# Funktion som hanterar allt som händer i rum 4
def rum_4(aktuellt_rum):
    spelaren_väljer = True
    
    while (spelaren_väljer):
         # Rensar skärmen innan beskrivningen av rummet skrivs ut på nytt.
        rensa_skärmen()
        
        # Beskrivningen av rummet ändras om spelaren har varit där tidigare
        if varit_i_rummet["rum_4"]:
            print("Du är tillbaka i det prickiga rummet.") 
            print("Den fjäderklädda vakten sover och snarkar.")
            print("Det finns en ekdörr till höger och bakom dig ligger korridoren.")
        else:
            print("Du kommer in i ett prickigt rum med en ekdörr till höger.")
            print("En vakt med en indianfjäder i håret sitter och halvsover")
            print ("på en stol vid ett bord i mitten av rummet.")
            print("Bakom dig har du dörren tillbaka till korridoren du kom ifrån.")
        
        # Markera att spelaren har varit i rummet
        varit_i_rummet["rum_4"] = True
        
        print ("1. Gå bakåt till korridoren igen.")
        print ("2. Smyg förbi vakten (30% risk att den vaknar) och gå höger.")
        print ("3. Se vad du bär på.")
        spelarens_val = input("Vad vill du göra? ")
        if (spelarens_val == "1"):
            print ("\nDu går tillbaka till korridoren.")
            
            # Anropar pausfunktionen
            tryck_på_valfri_tangent()

            # Sätter aktuellt rum till det rum som spelaren vill gå till
            aktuellt_rum = "rum_2"
            
            # Skickar tillbaka aktuellt rum till spelloopen.
            return aktuellt_rum
        elif (spelarens_val == "2"):
            print("Du försöker smyga förbi vakten och...")
            slumptal = random.randint(1, 100)    
            
            if (slumptal <= 30):
                print ("Vakten vaknar och med blixtens hastighet drar den fram en pilbåge") 
                print ("och skjuter iväg en pil som naglar fast dina kläder mot väggen.")
                print ("\"Jaså en rymmare, men nu har jag dig fast!\", skrattar vakten.")
                print ("Vakten låser in dig i cellen igen och lämnar dig där.")
                
                # Anropar pausfunktionen
                tryck_på_valfri_tangent()

                # Sätter aktuellt rum till cellen
                aktuellt_rum = "rum_1"
            
                # Skickar tillbaka aktuellt rum till spelloopen.
                return aktuellt_rum
            else:
                print ("Vakten grymtar lite i sömnen, men vaknar inte.")
                print ("Du öppnar försiktigt ekdörren och går in i rummet bakom...")
                
                # Anropar pausfunktionen
                tryck_på_valfri_tangent()

                # Sätter aktuellt rum till cellen
                aktuellt_rum = "rum_5"
            
                # Skickar tillbaka aktuellt rum till spelloopen.
                return aktuellt_rum
        elif (spelarens_val == "3"):
            if inventory:
                print("\nDu tittar i dina gigantiska fickor och hittar följande:")
                for föremål, beskrivning in inventory.items():
                    print(f"- {föremål.capitalize()} ({beskrivning})")
            else:
                print("\nDu tittar i dina fickor, men de är tomma.")
            
            # Anropar pausfunktionen
            tryck_på_valfri_tangent()    
        
            

### RUM 5 ###
# Funktion som hanterar allt som händer i rum 5
def rum_5(aktuellt_rum):
    spelaren_väljer = True
    
    while (spelaren_väljer):
         # Rensar skärmen innan beskrivningen av rummet skrivs ut på nytt.
        rensa_skärmen()
        
        # Beskrivningen av rummet ändras om spelaren har varit där tidigare
        if varit_i_rummet["rum_5"]:
            print("Du är tillbaka i det randiga rummet med speglarna.") 
            print("Det hänger en lapp på en anslagstavla.")
            print("Bakåt finns rummet med vakten, framför dig ser du en väg ut.")
        else:
            print("Du kommer in i ett randigt rum fullt med speglar.")
            print("Du ser dig själv i spegeln och konstaterar att du sett bättre dagar.")
            print("Det finns en anslagstavla här med en lapp på.")
            print("På andra sidan rummet ser du en utgång.")
        
        # Markera att spelaren har varit i rummet
        varit_i_rummet["rum_5"] = True
        
        print ("1. Gå bakåt igen.")
        print ("2. Titta på lappen.")
        print ("3. Se vad du bär på.")
        print ("4. Gå rakt fram genom utgången.")
        spelarens_val = input("Vad vill du göra? ")
        if (spelarens_val == "1"):
            print ("\nDu går tillbaka till rummet innan.")
            print ("Men det skulle du inte ha gjort! För direkt när du öppnar dörren")
            print ("blir du haffad av en vakt med indianfjädrar i håret.")
            print ("\"Kom med här!\", säger den och du förs bryskt tillbaka till din cell.")
            # Anropar pausfunktionen
            tryck_på_valfri_tangent()

            # Sätter aktuellt rum till det rum som spelaren vill gå till
            aktuellt_rum = "rum_1"
            
            # Skickar tillbaka aktuellt rum till spelloopen.
            return aktuellt_rum
        elif (spelarens_val == "2"):
            print("Du går fram till anslagstavlan och läser lappen. Det står:")
            print("\"Här skulle det egentligen Bosse Fighter vaktat men han tog semester.\"")
    
            # Anropar pausfunktionen
            tryck_på_valfri_tangent() 
        elif (spelarens_val == "3"):
            if inventory:
                print("\nDu tittar i dina inte oansenliga fickor och hittar följande:")
                for föremål, beskrivning in inventory.items():
                    print(f"- {föremål.capitalize()} ({beskrivning})")
            else:
                print("\nDu tittar i dina fickor, men de är tomma.")
            
            # Anropar pausfunktionen
            tryck_på_valfri_tangent() 
        elif (spelarens_val == "4"):
            print ("\nDu går ut i friheten och känner den friska luften.")
            print ("Grattis du hittade en väg ut och har lyckats fly från fängelset!")
            
            # Anropar pausfunktionen
            tryck_på_valfri_tangent()

            # Sätter aktuellt rum till det rum som spelaren vill gå till
            aktuellt_rum = ""
            
            # Skickar tillbaka aktuellt rum till spelloopen.
            return aktuellt_rum

    
### SPEL-LOOPEN ###
# Spelet fortsätter köras så länge som spelaren inte hittat ut ur fängelset
def spel_loop(aktuellt_rum, tagit_nyckeln, tagit_barnteckningen, gåtan_löst):
    while (spelet_körs):
        # När spelaren är klar i rummet och går till nästa rum 
        # uppdateras rumvariabeln till den nya platsen  
    

        if aktuellt_rum == "rum_1":
            aktuellt_rum, tagit_nyckeln = rum_1(aktuellt_rum, tagit_nyckeln)
        elif aktuellt_rum == "rum_2":
            aktuellt_rum = rum_2(aktuellt_rum)
        elif aktuellt_rum == "rum_3":
            aktuellt_rum, tagit_barnteckningen, gåtan_löst = rum_3(aktuellt_rum, tagit_barnteckningen, gåtan_löst)
        elif aktuellt_rum == "rum_4":
            aktuellt_rum = rum_4(aktuellt_rum)
        elif aktuellt_rum == "rum_5":
            aktuellt_rum = rum_5(aktuellt_rum)
        else:
            print("Spelet är slut.")
            tryck_på_valfri_tangent()
            break


# Visar menyn
while (gör_menyval):
    rensa_skärmen()

    print ("FLY FRÅN FÄNGELSET")
    print ("1. Starta spelet")
    print ("2. Avsluta")
    print ("3. Visa instruktioner")
    meny_val = input ("Vad vill du göra: ")
    if (meny_val == "1"):
        spel_loop(aktuellt_rum, tagit_nyckeln, tagit_barnteckningen, gåtan_löst)
    elif (meny_val == "2"):
        break
    elif (meny_val == "3"):
        print("\n")
        # Filens namn
        filnamn = "readme.txt"

        try:
            # Öppna filen i läsläge
            with open(filnamn, "r", encoding="utf-8") as fil:
                # Läs innehållet
                innehåll = fil.read()
                # Skriv ut innehållet i konsolen
                print(innehåll)
                tryck_på_valfri_tangent()
        except FileNotFoundError:
            print(f"Filen '{filnamn}' kunde inte hittas.")
            tryck_på_valfri_tangent()
        except Exception as e:
            print(f"Ett fel inträffade: {e}")
            tryck_på_valfri_tangent()