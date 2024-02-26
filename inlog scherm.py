#Importeer de GUI-module van appJar
from appJar import gui

#Definieer de functie die wordt uitgevoerd wanneer er op de knop wordt geklikt
def login():
    #Toon een welkomstbericht met de ingevoerde gebruikersnaam
    app.infoBox("Welkom", "Welkom, {}".format(app.getEntry("Gebruikersnaam")))

#Creëer een inlogscherm met afmetingen van 400x200 pixels
app = gui("Inlogscherm", "500x200")

#Label toevoegen met de tekst "Inloggen"
app.addLabel("title", "Inloggen")

#Voeg een invoerveld toe voor de gebruikersnaam
app.addLabelEntry("Gebruikersnaam")

#Voeg een beveiligd invoerveld toe voor het wachtwoord
app.addLabelSecretEntry("      Wachtwoord")

#Voeg een knop toe met de tekst "Inloggen" die de 'login'-functie activeert
app.addButtons(["Inloggen"], login)

#Start de GUI-loop om de applicatie uit te voeren
app.go()
