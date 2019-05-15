from firebase import firebase
from datetime import datetime
import json
import re

# setup firebase connection
fireKey = open("firebase.key", "r")
fireURL = fireKey.read()
firebase = firebase.FirebaseApplication(fireURL, None)

# load weather station from json
settings = open("settings.json", "r")
weatherNode = json.loads(settings.read())

# isolate station ID
ID = json.dumps(weatherNode["nodeID"])

# check if firebase data exists
entry = firebase.get('/stations/', ID)

if entry is not None:
    print("#found station: " + json.dumps(entry))
else:
    result = firebase.patch('/stations/' + ID, weatherNode, {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'})
    print("#push station: " + json.dumps(result))

# create log
nodeLog = {
    "nodeID": weatherNode["nodeID"],
    "timestamp": datetime.now(),
    "sensors": ["BMP180", "DHT22", "Photoresistor"],
    "temperature": 0,
    "brightness": 0,
    "pressure": 0,
    "humidity": 0,
    "altitude": 0,
}

# get unique timestamp for log
now = datetime.now()
timestamp = datetime.timestamp(now)

# read data from dht22
FILE_BMP180 = open("dht22.log", "r")
dht22Res = re.findall(r"(\".*\"|[^\\s\\=\\ ]+)", FILE_BMP180.read())

dht22TEMP = str(dht22Res[1]).strip('*')
dht22HUMIDITY = str(dht22Res[3]).strip('%')
print("dht22TEMP: " + dht22TEMP)
print("dht22HUMIDITY: " + dht22HUMIDITY)

# read data from bmp180
FILE_BMP180 = open("bmp180.log", "r")
bmp180Res = re.findall(r"(\".*\"|[^\\\:\\\n\\ ]+)", FILE_BMP180.read())

bmp180TEMP = str(bmp180Res[1])
bmp180PRESSURE = str(bmp180Res[4])
bmp180ALTITUDE = str(bmp180Res[7])
print("bmp180TEMP: " + bmp180TEMP)
print("bmp180PRESSURE: " + bmp180PRESSURE)
print("bmp180ALTITUDE: " + bmp180ALTITUDE)

# read data from photores
FILE_PHOTO = open("photo.log", "r")
photoRes = FILE_PHOTO.read()

photoBrightness = str(photoRes)
print("photoBrightness: " + photoBrightness)

# calculating averages, support multiple sensor inputs
finalTemp = (float(bmp180TEMP) + float(dht22TEMP)) / 2
finalPressure = bmp180PRESSURE
finalAltitude = bmp180ALTITUDE
finalBrightness = photoBrightness
finalHumidity = dht22HUMIDITY

# update json
nodeLog["temperature"] = str(finalTemp).replace("\n", "")
nodeLog["pressure"] = str(finalPressure).replace("\n", "")
nodeLog["altitude"] = str(finalAltitude).replace("\n", "")
nodeLog["brightness"] = str(finalBrightness).replace("\n", "")
nodeLog["humidity"] = str(finalHumidity).replace("\n", "")

result = firebase.patch('/logs/' + ID + '/' + str(int(timestamp)), nodeLog, {'print': 'pretty'},
                        {'X_FANCY_HEADER': 'VERY FANCY'})
