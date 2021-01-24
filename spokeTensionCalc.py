import math

frequency = 440.0

lengthCm = 26

diaCm = 0.2

densityGmCm = 7.8

tensionIn = math.pi * (frequency**2) * (lengthCm**2) * (diaCm**2) * densityGmCm

#print(tensionIn)


#f^2 * 4mL = T
spokeDia = 0.002
spokeLen = 0.245
volOfSpoke = spokeLen * ((spokeDia/2)**2) * math.pi
print("volOfSpoke = {}".format(volOfSpoke))
massSpoke = volOfSpoke * 7480.0
print("massSpoke = {}".format(massSpoke))
#massOfSpoke = (math.pi * (0.02**2) * 0.26)
#print(massOfSpoke)
#6.2g in kg is 0.0062

newTensionNewtons = (frequency**2) * (4 * massSpoke * spokeLen)

#print("New tension in newtons =  {}".format(newTensionNewons))

print(newTensionNewtons)