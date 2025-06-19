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

print()
print("-------------------Devintas uždavinys-------------")
print()

# Sukurkite Funkciją kuri priimtų du skaičius ir atspausdintų stačiakampį užpildytą žvaigždutėmis. Pirmas skaičius- išoriniam ciklui, antras vidiniam.

def rct(x, y):
    for i in range(y):
        print("*" * x)

rct(10, 5)

print()
print("-------------------Dešimtas uždavinys-------------")
print()

# Sukurkite Funkciją kuri priimtų sakinį kaip kintamąjį ir atspausdintų kiek jame yra raidžių(simbolių) ir tarpų.
# Sakinys - “Šiandien labai graži diena”. (kodas turi veikti padavus bet kokį sakinį) (simboliu yra 23, tarpu yra 3)

def cnt_smb(sentence):
    cnt_spc = 0
    cnt_symbol = 0
    for i in sentence:
        if i == " ":
            cnt_spc += 1
        else:
            cnt_symbol += 1
    print(f"Sakinyje tarpų yra {cnt_spc} ir simbolių (raidžių) {cnt_symbol}")

cnt_smb("Šiandien labai graži diena")

print()
print("-------------------Vienuoliktas uždavinys-------------")
print()

# Sukurkite Funkciją kuri priimtų sakinį, jį užkoduotų ir grąžintų. Kodavimas - sakinį apsukame iš kitos pusės. Pvz “Naglis” turi gautis “silgaN”

def rvrs(word):
    return word[::-1]

vardas = "Naglis"
print(rvrs(vardas))
print()

print()
print("-------------------Dvyliktas uždavinys-------------")
print()

# Sukurti funkciją, kuri apsuka tik žodžius. “Labas rytas” -> “sabal satyr”

def rvrs_word(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

sakinys = "Šiandien labai graži diena"
print(rvrs_word(sakinys))

print()
print("-------------------Tryliktas uždavinys-------------")
print()

# Sukurkite funkciją, kuri priimtų masyvą ir atspausdintų tik tuos elementus kurie yra skaičiai.

def print_nmb(array):
    for i in array:
        if isinstance(i, (int, float)):
            print(i, end=" ")
    print()

print_nmb([1, "gražu", 5, 2.5])
print()

print()
print("-------------------Keturioliktas uždavinys-------------")
print()

# Sukurkite funkciją, kuri iš paduoto masyvo atspausdina tik sveikuosius skaičius. (jei pavyks, patobulinkite,
# kad funkcija priimtų antrą parametrą True/False kuris nuspręstų ar spausdins tik sveikuosius skaičius ar skaičius su kableliu.

def print_nmb_v2(array, integer = True):
    for i in array:
        if isinstance(i, (int, float)):
            if integer and isinstance(i, int):
                print(i, end=" ")
            if not integer and isinstance(i, float):
                print(i, end=" ")
    print()

print_nmb_v2([1, "gražu", 5, 2.5], True)
print()

print()
print("-------------------Penkioliktas uždavinys-------------")
print()

# Sukurkite funkciją word_count kuri priimtų textą ir gražintų kiek jame yra žodžių.

def word_count(sentence):
    words = sentence.split()
    return len(words)

sakinys = "Šiandien labai graži diena"
print(word_count(sakinys))

print()
print("-------------------Šešioliktas uždavinys-------------")
print()

# Sukurkite funkciją kuri priima du parametrus. Skaičių masyvą ir boolean. Funkcija gražina prafiltruotą masyvą.
# Kai antras parametras True/tik poriniais skaičiais, False/tik neporiniais skaičiais

def even_nmb(array, even = True):
    for i in array:
        if even and i % 2 == 0:
            print(i, end=" ")
        if not even and i % 2 == 1:
            print(i, end=" ")
    print()

masyvas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nmb(masyvas, False)
print()

print()
print("-------------------Septynioliktas uždavinys-------------")
print()

# Sukurkite funkciją number_is_prime. Funkcija priima skaičių, gražina True/False ar skaičius pirminis.

def number_is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number = 2
print(number_is_prime(number))

print()
print("-------------------Aštuonioliktas uždavinys-------------")
print()

# Sukurkite funkciją kuri priima du argumentus. Gražina pirmąjį skaičių pakeltą laipsniu tokiu kaip antras skaičius.

def sqr_nmb(x, y):
    return print(x ** y)

sqr_nmb(2, 3)

print()
print("-------------------Devynioliktas uždavinys-------------")
print()

# Sukurkite funkciją kuri priima skaičių masyvą ir gražina tik nepasikartojančius elementus

def unique_nmb(array):
    new_array = []
    for i in array:
        if i not in new_array:
            new_array.append(i)
    return new_array

masyvas = [1, 2, 3, 1, 5, 9, 8, 7, 7]

print(unique_nmb(masyvas), end=" ")
print()

print()
print("-------------------Dvidešimtas uždavinys-------------")
print()

# Sukurkite funkciją kuri priima tekstą ir atspausdina tekste daugiausiai pasikartojantį simbolį.


def cnt_smb(sentence):
    return print(f"Daugiausiai pasikartojantis simbolis tekste: {max(sentence, key=sentence.count)}")

sakinys = "Šiandien labai graži diena"
cnt_smb(sakinys)

print()
print("-------------------Dvidešimt pirmas uždavinys-------------")
print()

# Sukurkite funkciją kuri priima tekstą ir atspausdina jame esantį ilgiausią žodį.

def long_txt(sentence):
    words = sentence.split()
    return max(words, key=len)

sakinys = "Šiandien labai graži diena"
print(f"Ilgiausis žodis tekste: {long_txt(sakinys)}")
print()
