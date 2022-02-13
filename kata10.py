#Ejercicio 1
def readConfig():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")


#Ejercicio 2

def waterLeft(astronauts,waterLeft,daysLeft):
    for argument in [astronauts,waterLeft,daysLeft]:
        try:
          argument/2
        except TypeError:
            raise TypeError(f"Arguments must be of type int, but received: '{argument}'")
    
    dailyUsage=astronauts*11
    totalUsage=dailyUsage*daysLeft
    totalWater=waterLeft-totalUsage
    if totalWater<0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {daysLeft} days.")
    if astronauts<=0:
        raise RuntimeError(f"Astronauts must be greater than 0, but received: '{astronauts}'")
    return f"""{totalWater} liters of water left after {daysLeft} days."""



print(waterLeft(3,100,2))