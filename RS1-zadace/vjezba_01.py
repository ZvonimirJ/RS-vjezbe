a = float(input("Unesite prvi broj: "))
b = float(input("Unesite drugi broj: "))

op = input("Unesite operator (+, -, *, /): ").strip()

if op == "+":
    result = a + b
    print(f"Rezultat operacije {a} + {b} je {result}")
elif op == "-":
    result = a - b
    print(f"Rezultat operacije {a} - {b} je {result}")
elif op == "*":
    result = a * b
    print(f"Rezultat operacije {a} * {b} je {result}")
elif op == "/":
    if b == 0:
        print("Dijeljenje s nulom nije dozvoljeno!")
    else:
        result = a / b
        print(f"Rezultat operacije {a} / {b} je {result}")
else:
    print("Nepodržani operator!")


