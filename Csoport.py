class Csoport:
    def __init__(self, nev: str, evfolyam: int, atlag: float):
        self.nev = nev
        self.evfolyam = evfolyam
        self.atlag = atlag

    def __str__(self)->str:
        return f"Név:{self.nev}, évfolyam{self.evfolyam}, átlag: {self.atlag}."