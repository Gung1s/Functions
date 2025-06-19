import random

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

# Parašykite funkciją, kuri skaičiuotų, ir gražintų iš kiek sveikų skaičių jos argumentas dalijasi be liekanos (išskyrus vienetą ir patį save). Pvz padavus 10 turi grąžinti 2,  o padavus 20 gražintų 4.
