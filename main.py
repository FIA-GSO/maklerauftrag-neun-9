#Globale Variablen
STATE_ADDING = True
i = 0
raeume = {}
gesamtflaeche = 0
    
#Eigene Raumklasse um später flexibel auf die eingetragenen Raum Daten zuzugreifen 
class raum:
    flaeche = 0
    def __init__(self, name, breite, laenge):
        self.name = name
        self.breite = breite
        self.laenge = laenge
        self.raumflaeche = breite * laenge

    @property
    def flaeche(self):
        return self.raumflaeche
    
    
    
while STATE_ADDING:
        print("Hat der Raum mehr als vier Ecken?")
        tempInput = input().lower()
        if(tempInput == "ja"):
            print("Geben sie einen Raumnamen ein! Und geben sie danach die Länge und Breite der Teilräume ein!")
            neuer_raum = raum(input("Raumname: "),0,0)
            raeume[f"raum{i}"] = neuer_raum
            anzahl_teilraueme = 0
            print("Geben sie folgend die einzelnen Teilräume ein!")
            while tempInput == "ja" and  anzahl_teilraueme < 2:
                print(f"Geben sie die Infos für Teilraum_{anzahl_teilraueme} an!")
                anzahl_teilraueme += 1 
                unterraum = raum(f"{raeume[f"raum{i}"].name}_{anzahl_teilraueme}",float(input("Teilraumbreite: ")), float(input("Teilraumlänge: ")))
                raeume['raum'+str(i)].raumflaeche += unterraum.flaeche
                if(anzahl_teilraueme > 2 ):
                    print("Gibt es weitere Teilräume in diesem Raum? (ja/nein): ")
                    tempInput = input().lower() 
        else:
            print("Geben sie einen Raumnamen, Raumbreite und Raumlänge ein:")   
            neuer_raum = raum(input("Raumname: "), float(input("Raumbreite: ")), float(input("Raumlänge: ")))
            raeume[f"raum{i}"] = neuer_raum
       
        
        
        
        i += 1    
        weiter = input("Möchten sie einen weiteren Raum hinzufügen? (ja/nein): ")
        if weiter.lower() != 'ja':
            anzahl_raeume = i
            STATE_ADDING = False    
            
for j in range(anzahl_raeume):
    print(raeume.get(f"raum{j}").name + ": " + str(raeume.get(f"raum{j}").flaeche) + " m^2")
    
print("Möchten sie die Gesamtfläche aller Räume berechnen? (ja/nein): ")

if input().lower() == 'ja':
    for j in range(anzahl_raeume):
        gesamtflaeche += raeume.get(f"raum{j}").flaeche
    print("Ihre Wohnung hat insgesamt " + str(anzahl_raeume) + " Räume.")
    print("Die Gesamtfläche aller Räume beträgt: " + str(gesamtflaeche) + " m^2")    


