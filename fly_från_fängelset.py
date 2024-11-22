
# ***** VARIABLER I SPELET *****
spelet_körs = True
aktuellt_rum = "rum_1"  # Håller reda på i vilket rum spelaren befinner sig i


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


# ***** FUNKTIONER I SPELET *****

# RUM 1
def rum_1(aktuellt_rum):
    spelaren_väljer = True
    while (spelaren_väljer):
        print(f"Du befinner dig i {rum["rum_1"]["beskrivning"]}")
        print ("Det luktar unket här och du förstår att någon eller något har tagit dig till fånga.")
        print ("1. Öppna dörren.")
        print ("2. Genomsöka rummet.")
        spelarens_val = input("Vad vill du göra? ")
        if (spelarens_val == "1"):
            # Kontrollera om spelaren har nyckeln
            if "nyckel" in inventory:
                print("\nDu använder nyckeln för att låsa upp dörren. Dörren öppnas!\n")
                
                # Avslutar while-loopen
                spelaren_väljer = False 
                
                # Byt till rum_2
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
        print(f"Du befinner dig i {rum["rum_2"]["beskrivning"]}")
        print ("Du vill inte gå bakåt därifrån du kom. Då återstår följande val.")
        print ("1. Gå höger.")
        print ("2. Gå vänster")
        print ("3. Genomsöka rummet.")
        spelarens_val = input("Vad vill du göra? ")
        if (spelarens_val == "1"):
            print("\nDu går åt höger.\n")
        elif (spelarens_val == "2"):
            print ("\nDu går åt vänster.\n")
        elif (spelarens_val == "3"):
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
        