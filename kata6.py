# Ejercicio 1

planets=["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

print("Planets: "+str(planets))

planets.append("Pluto")

print("Number of planets: "+str(len(planets)))
print("Last Planet: "+str(planets[-1]))

print("\n")
# Ejercicio 2

planets=["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

user=input("Enter the name of the planet: ")
planet_index=planets.index(user)
print("Planets closer to the sun than "+user+":")
print(planets[0:planet_index])
print("Planets farther to the sun than "+user+":")
print(planets[planet_index+1:])