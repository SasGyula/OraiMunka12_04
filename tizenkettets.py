def tk():
    adatokListaja=[]
    beFile = open("fajlok/allas.txt", "r", encoding="utf-8")
    for sor in beFile:
        daraboltSor = sor.strip().split("  ")
        #print(daraboltSor)
        adatokListaja.extend(daraboltSor)
    beFile.close()
    index = 0
    db = 0
    while index < len(adatokListaja):
        if adatokListaja[index] == "0":
            db += 1
        index += 1
    print(f"A ledöntött bábuk száma:{db}")

