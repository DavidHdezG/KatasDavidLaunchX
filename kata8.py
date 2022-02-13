# Ejercicio 1
planet = {
    'name': 'Mars',
    'moons': 2
}

print(f"The planet {planet['name']} has {planet['moons']} moons.")

planet["circumference (km)"] = {
    'polar': 6752,
    'equatorial': 6792
}

print(
    f"The planet {planet['name']} has a polar circumference of {planet['circumference (km)']['polar']}.")

# Ejercicio 2
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

moons = planet_moons.values()

nPlanets = len(planet_moons)

totalMoons = 0
for i in moons:
    totalMoons += i

average = totalMoons/nPlanets

print(average)
