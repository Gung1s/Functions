def say_hello(): # nieko nepriima, nieko negrąžina
    print("Hello World")

say_hello()
say_hello()
say_hello()

def say_hi_to(name): #priima kintąmąjį, bet nieko negrąžina (neįstao į funkcijos vietą)
    print("Hello " + name)

say_hi_to("John")

def sim_pi(): # nieko nepriima, bet kažką grąžina
    return 3.14

print(sim_pi())
pi = sim_pi()
print(pi)

def sum(a, b): #priima du kintamuosius, grąžina reikšmę
    return a + b
res = sum(3, 4)
print(res)
print(sum(3, 4))

def make_initials(name, surname):
    return (name[0]+surname[0]).upper()

print(make_initials("John", "Smith"))
print(make_initials("sohn", "smith"))

def make_initials_v2(txt):
    parts = txt.split()
    init = ""
    for pt in parts:
        init += pt[0].upper()
    return init

print(make_initials_v2("John Brown Marks"))

def calc_age(birth_year = 2025): # po ženklo lygu parašom default reikšmę
    return 2025 - birth_year
age = calc_age()
print(age)
age = calc_age(1984)
print(age)

def print_info(name = "", surname = "", birt_year = 0):
    print(f"Mano vardas {name} pavardė {surname} gimimo metai {birt_year}")
print_info()
print_info("Tomas")
print_info()

