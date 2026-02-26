#Globale Variablen
STATE_ADDING = True
i = 0
#Python Dictionary initialisiert als Raumverzeichnis.
raeume = {}
gesamtflaeche = 0
    
#Eigene Raumklasse um später flexibel auf die eingetragenen Raum Daten zuzugreifen 
class raum:
    flaeche = 0
    #Konstruktor der Raumklasse welche Name, Breite, Länge annehmen kann.
    def __init__(self, name, breite, laenge):
        self.name = name
        self.breite = breite
        self.laenge = laenge
        self.raumflaeche = breite * laenge

    @property
    def flaeche(self):
        return self.raumflaeche
    
print("Willkommen im Maklerprogramm.")
print("\nIm Folgenden können Sie Räume nach Bedarf bennen und die Maße angeben.")
print("\nSpezifizieren dabei zuerst, ob der Raum einfach Viereckig ist oder ein Polynom ist.")
print("Im Anschluss können Sie die Gesamtfläche berechnen lassen!")   
print("__________________________________________________________")
    
while STATE_ADDING:
        #Einstieg in das Program und Spezifizieren des Raumtyps
        print("__________________________________________________________")
        print("\n")
        print("Hat der Raum mehr als vier Ecken? (ja/nein)")
        tempInput = input().lower()
        
        if(tempInput == "ja"):
            
            #Fall eines komplexeren Raumes.
            #Zuerst wird hier ebenfalls ein neuer Raum initialisiert. 
            #Dabei wird der Raum erst dimensionslos mit Länge = 0 und Breite = 0 initialisiert.
            
            print("Geben sie einen Raumnamen ein! Und geben sie danach die Länge und Breite der Teilräume ein!")
            neuer_raum = raum(input("Raumname: "),0,0)
            raeume[f"raum{i}"] = neuer_raum
            anzahl_teilraueme = 1
            print("Geben sie folgend die einzelnen Teilräume ein!")
            
            while tempInput == "ja" and  anzahl_teilraueme < 3:
                
                #Hier wird derselbe Prozess wiederholt nur das statt einem Raum ein Unterraum initialisiert wird.
                
                print(f"Geben sie die Infos für Teilraum_{anzahl_teilraueme} an!")
                anzahl_teilraueme += 1 
                unterraum = raum(f"{raeume[f"raum{i}"].name}_{anzahl_teilraueme}",float(input("Teilraumbreite: ")), float(input("Teilraumlänge: ")))
                
                #Der Fläche wird folgend auf den Raum unter der aktuellen Laufvariable hinzugerechnet.
                raeume['raum'+str(i)].raumflaeche += unterraum.flaeche
                
                #Die Exit Kondition hier wird erst geprüft, wenn bereits mindestens zwei Unterräume eingetragen wurden.
                if(anzahl_teilraueme > 2 ):
                    print("Gibt es weitere Teilräume in diesem Raum? (ja/nein): ")
                    tempInput = input().lower() 
        else:
            #Fall einfaches Rechteck und Eingabe der Parameter.
            #Raumobjekt wird anschließend initialisiert und anschließend mit einem Key dem Räume Dictionary zugewiesen. 
            print("Geben sie einen Raumnamen, Raumbreite und Raumlänge ein:")   
            neuer_raum = raum(input("Raumname: "), float(input("Raumbreite: ")), float(input("Raumlänge: ")))
            raeume[f"raum{i}"] = neuer_raum
       
        #Key Laufvariable für das Raum Dictionary 
        i += 1    
        weiter = input("Möchten sie einen weiteren Raum hinzufügen? (ja/nein): ")
        
        if weiter.lower() != 'ja':
            #Für bessere Lesbarkeit. Neuzuweisung der Laufvariable zu einer allgemeinen 
            anzahl_raeume = i
            STATE_ADDING = False    
 
#Schleife über die Raumobjekte zur Ausgabe aller Namen und den Raumfächen.          
for j in range(anzahl_raeume):
    print(raeume.get(f"raum{j}").name + ": " + str(raeume.get(f"raum{j}").flaeche) + " m^2")
    
print("Möchten sie die Gesamtfläche aller Räume berechnen? (ja/nein): ")

if input().lower() == 'ja':
    #Schleife zur Summierung aller Raumflächen 
    for j in range(anzahl_raeume):
        gesamtflaeche += raeume.get(f"raum{j}").flaeche
    print("Ihre Wohnung hat insgesamt " + str(anzahl_raeume) + " Räume.")
    print("Die Gesamtfläche aller Räume beträgt: " + str(gesamtflaeche) + " m^2")    
