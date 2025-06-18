import random
print()
print("-------------------Lengvesnės funkcijų užduotys-------------")
print()

print()
print("-------------------Pirmas uždavinys-------------")
print()

# Sukurkite Funkciją kuri priima du kintamuosius, skaičius. Juos susumuoja ir atspausdina.

def suma(a, b):
    print(a + b)

suma(2, 3)

print()
print("-------------------Antras uždavinys-------------")
print()

# Sukurkite Funkciją kuri vadinasi PISq. Funkcija gražina reikšmę. Reikšmė yra : 9.8596; Gautą reikšmę atspausdinkite.
def PISq():
    return 9.8596

print(PISq())

print()
print("-------------------Trečias uždavinys-------------")
print()

# Sukurkite Funkciją kuri priima du kintamuosius. Funkcija gražina skaičių sandaugą.; Gautą reikšmę atspausdinkite.

def san(a, b):
    return a * b

print(san(2, 3))
print()

print()
print("-------------------Ketvirtas uždavinys-------------")
print()

# Sukurkite Funkciją kuri priima masyvą, prasuka ciklą ir atspausdina kiekvieną narį vienoje eilutėje.

def print_array (array):
    for i in array:
        print(i, end=" ")
    print()

print_array([1, 2, 3])

print()
print("-------------------Penktas uždavinys-------------")
print()

# Sukurkite Funkciją kuri priima du kintamuosius, min ir max reikšmėms nustatyti ir sugeneruoja random int skaičių ir jį gražintų.

def rnd_nmb(min, max):
    return random.randint(min, max)

print(rnd_nmb(1, 10))
print()

print()
print("-------------------Šeštas uždavinys-------------")
print()

# Sukurkite Funkciją kuri sugeneruotų random skaičių masyvą ir jį gražintų. Funkcija priima tris kintamuosius, min, max ir length reikšmėms nustatyti.

def rnd_arr(min, max, length):
    return [random.randint(min, max) for i in range(length)]

print(rnd_arr(1, 10, 5))
print()

print()
print("-------------------Septinas uždavinys-------------")
print()

# Sukurkite Funkciją kuri panaudotų 6toje užduotyje sugeneruotą masyvą (priimtų kaip kintamąjį), susumuotų ir gražintų reikšmę.

def sum_arr(rnd_arr):
    suma = 0
    for i in rnd_arr:
        suma += i
    return suma

array = rnd_arr(1,5,2)
print(array)
suma = sum_arr(array)
print(suma)
print()

print()
print("-------------------Aštuntas uždavinys-------------")
print()

# Sukurkite Funkciją kuri priimtų 6toje užduotyje sugeneruotą masyvą ir gražintų jos skaičių vidurkį.

def avg_arr(rnd_arr):
    suma = 0
    for i in rnd_arr:
        suma += i
    return suma / len(rnd_arr)

array = rnd_arr(1,5,2)
print(array)
print(avg_arr(array))