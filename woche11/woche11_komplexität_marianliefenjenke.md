
#Pro2
#Woche10
#BigO

    @classmethod
    def _number_uppercase_letters(cls, text):
        return sum(1 for c in text if c.isupper())/len(text)
        
#Komplexität 0(n).
#Die Schleife durchläuft alle Elemente des Eingabetextes und filtert alle Großbuchstaben.
#Die Funktion formt den Eingabetext in einen Integer um, der nur die (für die Funktion) relevanten Inhalte ausgibt bzw. durch die log-Funktion in einer anderen Datei speichert.
#Die Arbeit mit einem Generator wäre im Vergleich zum bestehenden Code ineffizient.
        

