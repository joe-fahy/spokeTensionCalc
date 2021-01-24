import math

frequency = input("Please enter the frequency of the spoke in Hz: ")
frequency = float(frequency)

spokeLen = input("Please enter the length of the spoke in metres: ")
spokeLen = float(spokeLen)


#f^2 * 4mL = T

#Spoke dia is 2mm or 0.002metres
spokeDia = 0.002

#spokeLen = 0.245
#Most spokes use 301 stainless steel which has a density of 7930 kg/m^3
densityOfStainlessSteel = 7930.0
print("Frequency of Spoke = {} Hz".format(frequency))
print("Diameter of Spoke = {} Metres".format(spokeDia))
print("Length of spoke = {} Metres".format(spokeLen))
volOfSpoke = spokeLen * ((spokeDia/2)**2) * math.pi
print("Volume Of Spoke = {} Metres Cubed".format(volOfSpoke))
massSpoke = volOfSpoke * densityOfStainlessSteel
print("Mass of Spoke = {} Kilograms".format(massSpoke))
#massOfSpoke = (math.pi * (0.02**2) * 0.26)
#print(massOfSpoke)
#6.2g in kg is 0.0062

newTensionNewtons = (frequency**2) * (4 * massSpoke * spokeLen)

tensionKgf = newTensionNewtons / 9.807

#print("New tension in newtons =  {}".format(newTensionNewons))

print("Tension = {} Newtons".format(newTensionNewtons))
print("Tension in kgf = {} kgf".format(tensionKgf))