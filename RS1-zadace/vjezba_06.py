print("1) Suma svih parnih brojeva od 1 do 100 (for):")
s = 0
for i in range(2, 101, 2):
    s += i
print(s)

print("1) Suma svih parnih brojeva od 1 do 100 (while):")
s = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        s += i
    i += 1
print(s)

print()
print("2) Prvih 10 neparnih brojeva u obrnutom redoslijedu (for):")
for x in range(19, 0, -2):
    print(x)

print("2) Prvih 10 neparnih brojeva u obrnutom redoslijedu (while):")
count = 10
val = 19
while count > 0:
    print(val)
    val -= 2
    count -= 1

print()
print("3) Fibonaccijev niz do 1000 (for):")
a, b = 0, 1
for _ in range(1000):
    if a > 1000:
        break
    print(a)
    a, b = b, a + b

print("3) Fibonaccijev niz do 1000 (while):")
a, b = 0, 1
while a <= 1000:
    print(a)
    a, b = b, a + b
