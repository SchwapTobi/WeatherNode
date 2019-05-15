# save sensor logs, start weatherStation script
#WRITE DHT22 DATA
python3 ./simDHT22.py > dht22.log
#WRITE BMP DATA
python Adafruit_BMP085_example.py  > bmp180.log
#WRITE PHOTO
python3 ./simPHOTO.py > photo.log

python3 weatherStation.py









