def fMasodik():
    beFajl = open("fajlok/tetszoleges.txt", "r", encoding="utf-8")
    beFajl.readline()
    masodikSor = beFajl.readline()
    print(masodikSor)
    beFajl.close()

    kiFajl = open("fajlok/tetszoleges.txt", "a", encoding="utf-8")
    kiFajl.write("negyedik")
    beFajl.close()

    beFajl = open("fajlok/tetszoleges.txt", "r", encoding="utf-8")
    kiir = beFajl.read()
    print(kiir)
