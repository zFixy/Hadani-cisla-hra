import random
cislo = random.randint(0, 100)

print("Uhádni číslo od 0 do 100.")

while True:
    hadani = int(input("Zadej číslo: "))

    if hadani < cislo:
        print("Hádané číslo je vyšší.")
    elif hadani > cislo:
        print("Hádané číslo je nižší.")
    else:
        print("Uhodl jsi správně.")
        break 
