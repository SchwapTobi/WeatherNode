import sys
import random

temp = random.randint(1000, 2800) / 100.0
humidity = random.randint(3000, 10000) / 100.0
print("Temp=" + str(temp) + "*  Humidity=" + str(humidity) + "%")
sys.exit()
