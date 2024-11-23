
# ***** VARIABLER I SPELET *****
spelet_körs = True                  # Används i spelets huvudloop och är True om spelet ska fortsätta köras
aktuellt_rum = "rum_1"              # Håller reda på i vilket rum spelaren befinner sig i

# ***** DICTIONARIES I SPELET *****


# ***** INVENTORY *****
# Inventory är en dictionary som håller reda på vilka föremål som spelaren bär på.
inventory = {}


# ***** RUM *****
# Rum är en dictionary som håller reda på vilket rum spelaren är i.
# Först kommer rummets id, som är rum_1, rum_2, rum_3 osv... 
# beskrivning: Hur rummet beskrivs för spelaren.
# utgångar: kan vara framåt, bakåt, höger, vänster
# föremål: saker som finns i rummet som spelaren kan interagera med
rum = {
    "rum_1": 
    {
        "beskrivning": "ett smutsigt och kalt rum utan fönster med en dörr framför dig.",
        "utgångar": {"framåt": "rum_2"},
        "föremål": ["nyckel"],
        "vakter": [],
    },
    
    "rum_2": 
    {
        "beskrivning": "ett mörkt och fuktigt korridor med märken på väggarna.",
        "utgångar": {"bakåt": "rum_1", "höger": "rum_3", "vänster": "rum_4"},
        "föremål": [],
        "vakter": [],
    },
    
    "rum_3": 
    {
        "beskrivning": "Ett rum där det står en svartnisse.",
        "utgångar": {"bakåt": "rum_2", "vänster": "rum_5"},
        "föremål": [],
        "vakter": ["En svartnisse."],    
    },   
    
    "rum_4": 
    {
        "beskrivning": "Ett rum med ett pussel i.",
        "utgångar": {"bakåt": "rum_2", "höger": "rum_5"},
        "föremål": [],
        "vakter": [],    
    },

    "rum_5": 
    {
        "beskrivning": "Ett rum med en boss i.",
        "utgångar": {"bakåt": "rum_2", "höger": "rum_5"},
        "föremål": [],
        "vakter": ["Ett stort troll!"],    
    }   
}

# Dictionary som håller reda på om spelaren har besökt rummet tidigare
varit_i_rummet = {
    "rum_1": False,
    "rum_2": False,
    "rum_3": False,
    "rum_4": False,
    "rum_5": False,
}


# ***** FUNKTIONER I SPELET *****

# RUM 1
def rum_1(aktuellt_rum):
    spelaren_väljer = True

    while (spelaren_väljer):
        
        # Beskrivningen av rummet ändras om spelaren har varit där tidigare
        if varit_i_rummet["rum_1"]:
            print("\nDu återvänder till det smutsiga och kala rummet utan fönster.\n")
        else:
            print(f"\nDu befinner dig i {rum['rum_1']['beskrivning']}")
            print ("Det luktar unket här och du förstår att någon eller något har tagit dig till fånga.")
        
        # Markera att spelaren har varit i rummet
        varit_i_rummet["rum_1"] = True

        print ("1. Öppna dörren.")
        print ("2. Genomsöka rummet.")
        spelarens_val = input("Vad vill du göra? ")
        if (spelarens_val == "1"):
            # Kontrollera om spelaren har nyckeln
            if "nyckel" in inventory:
                print("\nDu använder nyckeln för att låsa upp dörren. Dörren öppnas!\n")
                
                # Avslutar while-loopen
                spelaren_väljer = False 
                
                # Byt till rum_2, genom att returnera ett nytt värde till aktuellt_rum i spelloopen
                return "rum_2"
            else:
                print("\nDörren är låst. Du behöver en nyckel för att öppna den.\n")
        elif (spelarens_val == "2"):
            # Kontrollerar om nyckeln finns i rummet
            if "nyckel" in rum["rum_1"]["föremål"]:
                # Lägger till föremålet "nyckel" till det som spelaren bär på.
                inventory["nyckel"] = {"beskrivning": "en rostig gammal nyckel."}
                    
                # Tar bort nyckeln från rummet eftersom spelaren har plockat upp den.
                rum["rum_1"]["föremål"].remove("nyckel")  # Ta bort nyckeln från rummet
                
                # Berättar för spelaren vad som händer
                print (f"\nDu hittar {inventory["nyckel"]["beskrivning"]} \n")
            else:
                print("\nDet finns inget mer att hitta här.\n")    


# RUM 2
def rum_2(aktuellt_rum): 
    spelaren_väljer = True
    while (spelaren_väljer):
        # Beskrivningen av rummet ändras om spelaren har varit där tidigare
        if varit_i_rummet["rum_2"]:
            print("\nÅterigen är du i det mörka och fuktiga rummet med märkena på väggarna.\n")
        else:
            print(f"Du kommer in i {rum["rum_2"]["beskrivning"]}")
            
        # Markera att spelaren har varit i rummet
        varit_i_rummet["rum_2"] = True
        
        print ("Du kan gå:")
        print ("1. Gå höger.")
        print ("2. Gå vänster")
        print ("3. Bakåt till cellen igen.")
        print ("\nDu kan också:")
        print ("4. Genomsöka rummet.")
        spelarens_val = input("Vad vill du göra? ")
        if (spelarens_val == "1"):
            print("\nDu går åt höger.\n")
        elif (spelarens_val == "2"):
            print ("\nDu går åt vänster.\n")
        elif (spelarens_val == "3"):
            # Byt till rum_1
            return "rum_1"  
        elif (spelarens_val == "4"):
            print ("\nDet finns inget att hitta här.\n")
        

# Spelet fortsätter köras så länge som spelaren inte hittat ut ur fängelset
while (spelet_körs):
    # När spelaren är klar i rummet och går till nästa rum 
    # uppdateras rumvariabeln till den nya platsen  
  
    if aktuellt_rum == "rum_1":
        aktuellt_rum = rum_1(aktuellt_rum)
    elif aktuellt_rum == "rum_2":
        aktuellt_rum = rum_2(aktuellt_rum)
    else:
        print("Spelet är slut.")
        break

        