s = "Guido van Rossum heeft programmeertaal Python bedacht."
for woord in s:
    for klinker in woord:
        if klinker == "a" or klinker == "e" or klinker == "o" or klinker == "i" or klinker == "u":
            print(klinker)