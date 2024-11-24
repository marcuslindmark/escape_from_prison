# ***** IMPORT AV EXTERNA MODULER TILL SPELET *****
# msvcrt behövs till pausfunktionen 
# os behövs för att kunna rensa skäremen
import msvcrt, os


# ***** VARIABLER I SPELET *****
spelet_körs = True                  # Används i spelets huvudloop och är True om spelet ska fortsätta köras
aktuellt_rum = "rum_1"              # Håller reda på i vilket rum spelaren befinner sig i

# RUM 1
tagit_nyckeln = False               # Kontrollerar om nyckeln finns i rummet

# RUM 3
tagit_barnteckningen = False        # Kontrollerar om barnteckningen finns i rummet
gåtan_löst = False                  # Kontrollerar om spelaren skrivit rätt svar i datorterminalen            

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
            print(f"Du kommer in i en mörkt och fuktigt korridor med märken på väggarna.")
            
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
        elif (spelarens_val == "3"):
        
            # Sätter aktuellt rum till det rum som spelaren vill gå till
            aktuellt_rum = "rum_1"
            
            # Skickar tillbaka aktuellt rum till spelloopen.
            return aktuellt_rum  
        elif (spelarens_val == "4"):
            print ("\nMärkena påminner dig om en streckgubbe som håller i något fyrkantigt.")
    
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
            return aktuellt_rum, tagit_barnteckningen
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
def rum_4():
    print("Du är i rum 4")


### RUM 5 ###
# Funktion som hanterar allt som händer i rum 5
def rum_5():
    print("Du är i rum 5")

# Spelet fortsätter köras så länge som spelaren inte hittat ut ur fängelset
while (spelet_körs):
    # När spelaren är klar i rummet och går till nästa rum 
    # uppdateras rumvariabeln till den nya platsen  
  
    if aktuellt_rum == "rum_1":
        aktuellt_rum, tagit_nyckeln = rum_1(aktuellt_rum, tagit_nyckeln)
    elif aktuellt_rum == "rum_2":
        aktuellt_rum = rum_2(aktuellt_rum)
    elif aktuellt_rum == "rum_3":
        aktuellt_rum, tagit_barnteckningen, gåtan_löst = rum_3(aktuellt_rum, tagit_barnteckningen, gåtan_löst)
    else:
        print("Spelet är slut.")
        break

        