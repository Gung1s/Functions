import random
from itertools import count

print()
print("-------------------Sunkesni funkcijų užduotys-------------")
print()

print()
print("-------------------Pirmas uždavinys-------------")
print()

# Parašykite funkciją, kurios argumentas būtų tekstas, kuris būtų atspausdinamas konsolėje pridedant “---” pradžioje ir gale. PVZ (---labas---)

def arg(sentence):
    print(f"---{sentence}---")
arg("<NAME>")
print()

print()
print("-------------------Antras uždavinys-------------")
print()

# Sugeneruokite atsitiktinį stringą iš raidžių ir skaičių (10 simbolių). Atspausdinkite simbolius stulpeliu.
# Jei tai skaičius apgaubkite “ [ 7 ]”. Jei skaičiai eina keli iš eilės, apgaubkite juos kartu. [75].
# (apačioje yra funkcija, ją nusikopijuokite ir paleiskite, ji sugeneruos stringą, su kuriuo dirbsite)
def generate_rnd_str(length):
  symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890"
  text = ""
  for i in range(length):
    text += symbols[random.randint(0,len(symbols) -1)]
  return text

def clm_rnd_str(gnr_arr):
  nmb_arr = ""
  for i in gnr_arr:
    if i.isdigit():
      nmb_arr += i
    else :
      if nmb_arr:
        print(f"[{nmb_arr}]")
        nmb_arr = ""
      print(i)
  if nmb_arr:
    print(f"[{nmb_arr}]")

masyvas = generate_rnd_str(10)
clm_rnd_str(masyvas)

print()
print("-------------------Trečias uždavinys-------------")
print()

# Parašykite funkciją, kuri skaičiuotų, ir gražintų iš kiek sveikų skaičių jos argumentas dalijasi be liekanos
# (išskyrus vienetą ir patį save). Pvz padavus 10 turi grąžinti 2,  o padavus 20 gražintų 4.

def dvs_prt_cnt(x):
  count = 0
  for i in range(2, x):
    if x % i == 0:
      count += 1
  return count

print(dvs_prt_cnt(18))

print()
print("-------------------Ketvirtas uždavinys-------------")
print()

# Sugeneruokite masyvą iš 100 elementų, kurio reikšmės atsitiktiniai skaičiai nuo 33 iki 77.
# Išrūšiuokite masyvą pagal daliklių be liekanos kiekį mažėjimo tvarka, panaudodami trečio uždavinio funkciją.

def gnr_arr_100():
  masyvas = [random.randint(33,77) for i in range(100)]
  rkt_arr = sorted(masyvas, key = dvs_prt_cnt, reverse = True)
  return rkt_arr

print(gnr_arr_100())
print()

print()
print("-------------------Penktas uždavinys-------------")
print()

# Sugeneruokite masyvą iš 100 elementų, kurio reikšmės atsitiktiniai skaičiai nuo 333 iki 777.
# Naudodami 3 uždavinio funkciją iš masyvo suskaičiuokite kiek yra pirminių skaičių.

def gnr_arr_prime():
  masyvas = [random.randint(333,777) for i in range(100)]
  new_array = []
  count = 0
  for i in masyvas:
    if dvs_prt_cnt(i) == 0:
      count += 1
      new_array.append(i)
  return new_array, count

print(gnr_arr_prime())

print()
print("-------------------Aštuntas uždavinys-------------")
print()

# Sugeneruokite masyvą iš trijų elementų, kurie yra atsitiktiniai skaičiai nuo 1 iki 33.
# Jeigu tarp trijų paskutinių elementų yra nors vienas ne pirminis skaičius, prie masyvo pridėkite dar vieną elementą-
# atsitiktinį skaičių nuo 1 iki 33. Vėl patikrinkite pradinę sąlygą ir jeigu reikia pridėkite dar vieną elementą.
# Kartokite, kol sąlyga nereikalaus pridėti elemento.

# visi trys galutiniai skaičiai ne pirminiai

def gnr_arr_not_prime():
  masyvas = [random.randint(1,33) for i in range(3)]
  while True:
    if all(dvs_prt_cnt(i) for i in masyvas[-3:]):
      break
    masyvas.append(random.randint(1,33))
  return masyvas

print(gnr_arr_not_prime())

# visi trys galutiniai skaičiai pirminiai

def gnr_arr_all_prime():
  masyvas = [random.randint(1,33) for i in range(3)]
  while True:
    if all(dvs_prt_cnt(i) == 0 for i in masyvas[-3:]):
      break
    masyvas.append(random.randint(1,33))
  return masyvas

print(gnr_arr_all_prime())

print()
print("-------------------Devintas uždavinys-------------")
print()

# Sugeneruokite masyvą iš 10 elementų, kurie yra masyvai iš 10 elementų, kurie yra atsitiktiniai skaičiai nuo 1 iki 100.
# Jeigu tokio didelio masyvo (ne atskirai mažesnių) pirminių skaičių vidurkis mažesnis už 70, suraskite masyve mažiausią
# skaičių (nebūtinai pirminį) ir prie jo pridėkite 3. Vėl paskaičiuokite masyvo pirminių skaičių vidurkį ir jeigu mažesnis
# nei 70 viską kartokite.

def is_prime(n):
  if n < 2:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True

def rnd_arr_arr():
  arr_arr = [[random.randint(1,100) for i in range(10)] for i in range(10)]
  # print(arr_arr)
  count = 0
  while True:
    count += 1
    prime = [i for x in arr_arr for i in x if is_prime(i)]
    # print(prime)
    if prime:
      avg = sum(prime) / len(prime)
      # print(avg)
    else:
      avg = 0
    if avg >= 70:
      break
    min_value = 101
    min_i = 0
    min_j = 0
    for i in range(len(arr_arr)):
      for j in range(len(arr_arr[i])):
        if arr_arr[i][j] < min_value:
          min_value = arr_arr[i][j]
          min_i = i
          min_j = j
    arr_arr[min_i][min_j] += 3
  return arr_arr, round(avg, 2), count

print(rnd_arr_arr())


