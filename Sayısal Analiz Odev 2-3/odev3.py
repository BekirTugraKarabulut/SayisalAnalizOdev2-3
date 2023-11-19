import math

x = 2

print("---3. Ödev b) Sorusu ---\n")

for i in range(0,4):

    fonk = (4*math.e**(-0.5 * x)) - x 

    turev = (-2*math.e**(-0.5 * x)) - 1 

    fxo = x - (fonk / turev)

    x = fxo

    print("Kökleri : " , fxo)