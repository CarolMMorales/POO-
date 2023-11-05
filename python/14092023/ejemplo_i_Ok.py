from abc import ABC
class Animal(ABC):
    def correr():
        pass

class AnimalVolador(ABC):
    def volar():
        pass

class AnimalQueRespirarSinAire(ABC):
    def respirarSinAire():
        pass
#Un perro no podría ni volar ni respirar sin aire
class Perro(Animal):
    def correr(self):
        print("Perro corriendo")
        
class Aguila(AnimalVolador):
    def volar(self):
        print("Aguila volador")


perro1 = Perro()
perro1.correr()
aguila = Aguila()
aguila.volar()