class Flota:
    def __init__(self, name, marka, model, kolor, pojemnosc, spalanie, vmax):
        self.name = name
        self.marka = marka
        self.model = model
        self.kolor = kolor
        self.pojemnosc = pojemnosc
        self.spalanie = spalanie
        self.vmax = vmax

    def spalanie(self):
        print(f"{self.name} spala {self.spalanie} na 100 km")

    def vmax(self):
        print(f"{self.name} pojedzie max {self.vmax}")


romantic = Flota("Romantic", "BMW", "e36", "Romantic Rot", "2500", "12/100", "180 kmh")
e91 = Flota("Diesel", "BMW", "e91", "Space Grey", "2000", "6/100", "200 kmh")
kompakt = Flota("Kompakt", "BMW", "e36", "Santorinblau", "1600", "12/100", "150 kmh")

print(Flota)
Flota.spalanie(romantic)
Flota.vmax(e91)
print(romantic.marka)


samochody = []
samochody.append(romantic)
samochody.append(e91)
samochody.append(kompakt)

for s in samochody:
    print(s.model, s.pojemnosc)

print(samochody)