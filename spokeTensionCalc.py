import math

frequency = 440.0



#f^2 * 4mL = T
spokeDia = 0.002
spokeLen = 0.245
volOfSpoke = spokeLen * ((spokeDia/2)**2) * math.pi
print("Volume Of Spoke = {} Metres Cubed".format(volOfSpoke))
massSpoke = volOfSpoke * 7480.0
print("Mass of Spoke = {} Kilograms".format(massSpoke))
#massOfSpoke = (math.pi * (0.02**2) * 0.26)
#print(massOfSpoke)
#6.2g in kg is 0.0062

newTensionNewtons = (frequency**2) * (4 * massSpoke * spokeLen)

#print("New tension in newtons =  {}".format(newTensionNewons))

print("Tension = {} Newtons".format(newTensionNewtons))