def hetedik():
    beFajl = open("fajlok/dal.txt", "r", encoding="utf-8")
    lista = []
    for sor in beFajl:
        lista.append(sor.strip())
    beFajl.close()
    for index in range(len(lista)-1, -1, -1):
        print(lista[index])