import sys
import random

temp = random.randint(1000, 2800) / 100.0
pressure = random.randint(30000, 100000) / 100.0

print("Temperature: " + str(temp) + " C")
print("Pressure:    " + str(pressure) + " hPa")
print("Altitude:    50.83")
sys.exit()
