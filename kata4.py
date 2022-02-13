# Ejercicio 1

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

words=["average","temperature","distance"]

parts=text.split(".")

for sent in parts:
    for word in words:
        if word in sent:
            print(sent.replace(("C"), "Celsius"))

print("\n")
# Ejercicio 2

planet="Mars"
gravity=0.00143
name="Ganimedes"

title=f"Gravity data about {name}."

facts=f""" {'-'*50}
Planet: {planet}
Grabity on {name}: {gravity*1000} m/s^2
"""

template = f"""{title.title()}
{facts}"""

print(template.format(name=name, planet=planet, gravity=gravity))