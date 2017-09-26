def kleinste_veelvoud7(grenswaarde):
    """levert kleinste veelvoud van 7 die groter is dan 37"""
    som = 0
    while som < grenswaarde:
        som = som + 7
    return som
resultaat = kleinste_veelvoud7(700000)
print (resultaat)