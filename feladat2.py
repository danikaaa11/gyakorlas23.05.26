class Diak:
    def __init__(self,nev,osztaly,szuletesiev):
        self.nev = nev
        self.osztaly = osztaly
        self.szuletesiev = szuletesiev

    def hanyeves(self):
        a = 2023-szuletesiev

    def szoveg(self):
        return "Szia,"+nev+"vagyok, a"+osztaly+"osztályba járok,"+str(self.ev)+"éves vagyok"




lista = []
nev = input("Adja meg a nevét: ")
osztaly = input("Adja meg hogy melyik osztályba jár éppen: ")
szuletesiev = int(input("Adja meg a születési évét: "))
info = Diak(nev,osztaly,szuletesiev)
lista.append(info)

print(info)




