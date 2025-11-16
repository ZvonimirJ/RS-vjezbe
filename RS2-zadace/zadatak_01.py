kvadriraj = lambda x: x**2
zbroji_pa_kvadriraj = lambda x, y: (x+y)**2
kvadriraj_duljinu_niza = lambda x: len(x)**2
pomnozi_pa_potenciraj = lambda x, y: (y*5)**x
true_parni_none_neparni = lambda x : True if x%2==0 else None

print(kvadriraj(3))
print(zbroji_pa_kvadriraj(2, 3))
print(kvadriraj_duljinu_niza("abc"))
print(pomnozi_pa_potenciraj(2, 3))
print(true_parni_none_neparni(4))
print(true_parni_none_neparni(5))