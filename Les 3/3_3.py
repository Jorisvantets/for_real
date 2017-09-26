leeftijd = int(input('geef je leeftijd'))
nederlander = input('Heb je een nederlands paspoort?')
if leeftijd >17 and nederlander == str('ja'):
    print("Gefeliciteerd, Je mag stemmen")
if not leeftijd >17 or not nederlander == str('ja'):
    print("helaas, Je mag niet stemmen")