while True:
    woord = input('doe mij een woord: ')
    if woord == 'stop':
        break
    if woord == 'volgende':
        continue
    print(len(woord))