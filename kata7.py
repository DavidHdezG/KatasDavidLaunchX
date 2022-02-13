# Ejercicio 1

planetsList = []
planet = ""

while planet.lower() != "done":
    if planet:
        planetsList.append(planet)
    planet = input("Enter the name of the planet: ")


# Ejercicio 2

for planet in planetsList:
    print(planet)
