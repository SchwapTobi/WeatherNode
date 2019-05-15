# save sensor logs, start weatherStation script
python3 ./simDHT22.py > dht22.log
python3 ./simBMP180.py > bmp180.log
python3 ./simPHOTO.py > photo.log

python3 weatherStation.py









