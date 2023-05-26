class Negyzet:
    def __init__(self,negyoldal):
        self.negyoldal = negyoldal

    def kerulet(self):
        return 4*negyoldal

    def terulet(self):
        return negyoldal*negyoldal

lista=[]
negyoldal=int(input("Adja meg a egyik oldalt: "))
oldal=Negyzet(negyoldal)
lista.append(oldal)

print("A kerülete: ",oldal.kerulet(),"cm")
print("A területe: ",oldal.terulet(),"cm2")




















