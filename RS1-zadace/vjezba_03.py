import random

cilj = random.randint(1, 100)
broj_je_pogoden = False
pokusaji = 0

while not broj_je_pogoden:
    unos = int(input("Pogodi broj od 1 do 100: "))
    pokusaji += 1

    if unos < cilj:
        print("Uneseni broj je manji od traženog broja.")
    elif unos > cilj:
        print("Uneseni broj je veći od traženog broja.")
    else:
        broj_je_pogoden = True

print(f"Bravo, pogodio si u {pokusaji} pokušaja")
