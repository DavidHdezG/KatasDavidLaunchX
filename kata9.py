# Ejercicio 1  
def average(values):
    total=sum(values)
    nValues=len(values)
    return total/nValues

def report(tank1, tank2,tank3):   
    return f"""Fuel report:
    Total Average: {average([tank1, tank2, tank3])}%
    Tank 1: {tank1}%
    Tank 2: {tank2}%
    Tank 3: {tank3}%"""
    
print(report(10,20,30))

# Ejercicio 2
def missionReport(destination,*minutes,**fuel):
    report= f"""Mission report:
    Total travel time: {sum(minutes)} minutes
    Destination: {destination}
    Total fuel left: {sum(fuel.values())} liters\n"""
    for tankName,gallons in fuel.items():
        report+=f"Fuel left in {tankName} tank: {gallons} liters\n"
        
    return report
    
print(missionReport("Mars",10,15,51,main=100000,external=50000))