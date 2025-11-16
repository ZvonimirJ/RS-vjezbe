import datetime
import math

#1
class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza
    
    def ispis(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Godina: {self.godina_proizvodnje}, Kilometraza: {self.kilometraza}")
    
    def starost(self):
        trenutna_godina = datetime.datetime.now().year
        print(f"Automobil je star {trenutna_godina - self.godina_proizvodnje} godina")

auto = Automobil("Fiat", "Punto", 2008, 67000)
auto.ispis()
auto.starost()


#2
class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def zbroj(self):
        return self.a + self.b
    
    def oduzimanje(self):
        return self.a - self.b
    
    def mnozenje(self):
        return self.a * self.b
    
    def dijeljenje(self):
        if self.b != 0:
            return self.a / self.b
        return "Dijeljenje s nulom"
    
    def potenciranje(self):
        return self.a ** self.b
    
    def korijen(self):
        return math.sqrt(self.a), math.sqrt(self.b)


#3
class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene
    
    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

studenti_objekti = [Student(s["ime"], s["prezime"], s["godine"], s["ocjene"]) for s in studenti]

najbolji_student = max(studenti_objekti, key=lambda s: s.prosjek())
print(f"Najbolji student: {najbolji_student.ime} {najbolji_student.prezime}, prosjek: {najbolji_student.prosjek()}")


#4
class Krug:
    def __init__(self, r):
        self.r = r
    
    def opseg(self):
        return round(2 * math.pi * self.r, 2)
    
    def povrsina(self):
        return round(math.pi * self.r ** 2, 2)

krug = Krug(67)
print(f"Opseg: {krug.opseg()}, Povrsina: {krug.povrsina()}")


#5
class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa
    
    def work(self):
        print(f"Radim na poziciji {self.pozicija}")

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department
    
    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}")
    
    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje
        print(f"Plaća {radnik.ime} povećana za {povecanje}; Nova plaća: {radnik.placa}")

radnik = Radnik("Emily", "Assistant", 5000)
manager = Manager("Miranda", "CEO", 90000, "Executive")

radnik.work()
manager.work()
manager.give_raise(radnik, 0.99)