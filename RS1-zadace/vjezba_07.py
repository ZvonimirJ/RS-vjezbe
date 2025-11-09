def provjera_lozinke(lozinka):
    if not (8 <= len(lozinka) <= 15):
        print("Lozinka mora sadržavati između 8 i 15 znakova")
        return

    ima_veliko = any(c.isupper() for c in lozinka)
    ima_broj = any(c.isdigit() for c in lozinka)
    if not (ima_veliko and ima_broj):
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
        return

    lower = lozinka.lower()
    if "password" in lower or "lozinka" in lower:
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
        return

    print("Lozinka je jaka!")


loz = input("Unesite lozinku: ")
provjera_lozinke(loz)
