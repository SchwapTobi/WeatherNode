# WeatherNode- Automatisierte Wettermessung

Automatisierte Erfassung der aktuellen Wetterlage für das Projekt [WeatherNet](https://github.com/SchwapTobi/WeatherNet)

![](https://github.com/SchwapTobi/WeatherNode/blob/master/case/case_final/WeatherNode.jpg)

![](https://www.youtube.com/watch?v=mQ-7IHEHv-0&feature=youtu.be)

Als Wetterstation dient in unserem Prototyp ein Raspberry Pi Zero w mit folgendne Sensoren:

| Modul         | Funktion                                            | Doku                                                         |
| ------------- | --------------------------------------------------- | ------------------------------------------------------------ |
| BMP180        | Barometric Pressure / Temperature / Altitude Sensor | [Datasheet](https://cdn-shop.adafruit.com/datasheets/BST-BMP180-DS000-09.pdf) |
| DHT22         | Humidity / Temperature Sensor                       | [Datasheet](https://www.sparkfun.com/datasheets/Sensors/Temperature/DHT22.pdf) |
| Photoresistor | Luminance measurement                               | [Datasheet](https://www.kth.se/social/files/54ef17dbf27654753f437c56/GL5537.pdf) |
| ...           | ...                                                 | ...                                                          |

Diese werden auch vorerst für den Betrieb im WeatherNet vorausgestzt. Mögliche andere Sensoren werden wenn Zeit bleibt ergänzt.

### Ziel
Das Ziel ist die Messung und das Logging der erhobenen Daten um den Prototyp für ein Netzwerk zu bilden, welches dezentral an verschiedenen Orten Wetter & Umweltdaten misst. Die Daten sollen in beliebigen Zeitintervallen aufgezeichnet werden können und an unseren Backend-Server geschickt werden um sie dann in der App [WeatherNet](https://github.com/SchwapTobi/WeatherNet) darzustellen. Dazu wird eine Internetverbindung und konstante Stromversorgung vorausgesetzt. Im Laufe unseres Projekts werden wir auch den Betrieb mit Akku-Modulen (und wenn Zeit bleibt auch mit Solar-Panels) testen um die Station eigenständig z.B im Garten mit WIFI-Empfang betreiben zu können. 

### Setup
eine Schritt für Schritt- Anleitung folgt im Wiki.

###  Links:
- [Wiki](https://github.com/SchwapTobi/WeatherNode/wiki)
- [Demo](http://projects.tobias-schwap.at/weatherNet)

  

