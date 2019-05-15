# save sensor logs, start weatherStation script
import os

# use mock data for testing
os.system("./simDHT22.py > dht22.log")
os.system("./simBMP180.py > bmp180.log")
os.system("./simPHOTO.py > photo.log")

# log data in firebase
os.system("weatherStation.py")
