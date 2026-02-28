class Copia:
    def copyright(self):
        print("Infórmate del Copyright antes de nada...")

class Excusa(Copia):
    def copyright(self):
        print("Dificil solución")

class Obsoleto(Copia):
    def copyright(self):
        print("Es mi función")


c = Copia()
e = Excusa()
o = Obsoleto()

e.copyright()