# Raspberry Pi Shutdown Button

----
## Aufbau und Verdrahtung ##
Zum Aufbau werden folgende Teile benötigt:
- 1kOhm Widerstand
- 10 kOhm Widerstand
- Taster (Schließer)
- Drähte zum verkabeln

Den *3.3V* GPIO Port mit einem Eingang vom Taster verbinden und mit einem *1 kOhm Widerstand* zum GPIO Port *24*.
Mit einem zwischengeschaltetem *10 kOhm Widerstand* vom GPIO Port *24* auf *GND* (Ground bzw. *Minus* *-*).
Somit ist der Port immer auf *high* und geht in den Status *low* wenn der Taster betätigt wird.

![Aufbau](https://raw.githubusercontent.com/BaileySN/Raspberry-Pi-Shutdown-Button/master/gpio-numbers-pi2.png)

----------


## Download ##
**Raspberry Pi Shutdown Button**  unter */opt* downloaden.

>    git clone https://github.com/BaileySN/Raspberry-Pi-Shutdown-Button.git

## Skript ##
- Skript *shutdown_script.py* Ausführbar machen.

>    chmod +x shutdown_script.py

- GPIO Port *24* mit der richtigen Port Nummer an 2 Stellen im Skript ersetzen.

>    #config

>    #change the GPIO Port number

>    gpioport=24

- Programm Starten und Testen

>    python /opt/Raspberry-Pi-Shutdown-Button/shutdown_script.py

Zum Testen einfach den Knopf am Raspberry Pi drücken für ca. 3 Sekunden und der Pi fährt Automatisch runter.
Das Skript schreibt erstellt einen Log unter */var/log/* eine Datei, wo jedesmal wenn GPIO Port auf *LOW* ist einen eintrag macht (inkl. Datum).
Somit ist es leichter zu erkennen, warum der Pi aus ist.

## Autostart ##

In **/etc/rc.local** vor dem **#** folgenden Eintrag hinzufügen.

>    python /opt/Raspberry-Pi-Shutdown-Button/shutdown_script.py &

Somit wird nach jedem Start das Script im Pi gestartet.

 ![enter image description here](http://wiki.pratznschutz.com/images/thumb/f/f6/Logo_raspberry_pi.png/100px-Logo_raspberry_pi.png)
