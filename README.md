# TetrisArduino
Projekt mit dem Arduino Nano BLE Sense, um Tetris im Browser mit Bewegungsteuerung spielen zu können

## Gliederung
1. Einleitung
2. Vorbereitung der Arduino IDE
3. Planung Bewegung
4. Bewegungen aufnehmen
5. Bewegungsdaten trainieren 
6. Bewegungserkennung
7. Tastenzuweisung
8. Trouble Shooting

<!-- ![Getting Started](readme_files/architecture_diagramm.png)  -->

## 1. Einleitung

## 2. Vorbereitung der Arduino IDE
Das Projekt wurde mit einem [Arduino Nano 33 BLE Sense](https://docs.arduino.cc/hardware/nano-33-ble-sense) durchgeführt.
Bevor mit dem Projekt begonnen werden kann, muss jedoch zunächst die Arduino IDE heruntergeladen und eingerichtet werden.
Dafür folgen Sie einfach den nachfolgenden Schritten:
- Downloade und installiere die Arduino IDE [hier](https://arduino.cc/downloads)
- Öffne die soeben installierte IDE
- Navigiere im IDE Menü zum Board Manager (Tools > Board > Boards Manager...)
- Suche "Nano BLE" und drücke Installieren
- Die Installation kann mehrere Minuten in Anspruch nehmen
- Nach Abschluss der Installation kann das Boards Manager Fenster geschlossen werden
- Nun navigieren sie zu Library Manager (Tools > Manage Libraries...)
- Suchen und installieren Sie die "Arduino_TensorFlowLite" Bibliothek
- Suchen und installieren Sie die "Arduino_LSM9DS1" Bibliothek
- Als nächstes können Sie ihr Arduino Board mithilfe von einem Micro USB Kabel mit Ihrem Computer verbinden
- Wählen Sie das Board (Tools > Board > Arduino 33 BLE)
- Wählen Sie den Port (Tools > Port > COM5 (Arduino Nano 33 BLE) -> *Port name könnte leicht abweichen*) 
Nun haben Sie die Vorbereitungen abgeschlossen und können mit dem Projekt fortfahren

Sollten Sie Probleme bei der Einrichtung haben können die folgenden Links möglicherweise weiterhelfen: [Getting Started](https://docs.arduino.cc/software/ide-v1/tutorials/getting-started/cores/arduino-mbed_nano) oder [Troubleshooting](https://support.arduino.cc/hc/en-us)

## 3. Planung Bewegung
Zuerst muss geplant werden, welche Bewegungen für Tetris nötig sind. Es muss eine Möglichkeit geben den Block nach links und rechts zu bewegen, sowie ihn nach links und rechts zu rotieren. Optionale bietet Tetris oft die Möglichkeit den Block sofort an die derzeitige Stelle nach unten zu bewegen und einen Block für später zu speichern. Allen Steuerungsmöglichkeiten muss im nächsten Schritt eine Bewegung zugeordnet werden. Dabei ist zu beachten, dass die Bewegungen möglichst gut voneinander unterschieden werden können. Geplant sind folgende Bewegungen

Block nach links bewegen = Hand nach links bewegen
Block nach rechts bewegen = Hand nach rechts bewegen
Block nach links rotieren = Hand nach links drehen
Block nach rechts rotieren = Hand nach rechts drehen
Block nach unten bewegen = Hand nach unten bewegen
Block für später speichern = Hand nach oben bewegen

## 4. Bewegung aufnehmen
Zunächst müssen die Bewegungsdaten erfasst werden, bevor diese maschinell trainiert werden können. In diesem Kapitel geht es darum, wie diese gestreamt, visualisiert und erfasst werden können. Dafür benötigt man die Arduino IDE und einen entsprechenden Sketch, den man auf das Arduino Board laden kann. 
- Öffnen Sie zunächst die IDE und erstellen einen neuen Sketch (File > New Sketch)
- Als nächstes öffnen Sie die im Ordner "MovementCapture" enthaltene "MovementCapture.ino" Datei und kopieren Sie den Code in den neu geöffneten Sketch

Mithilfe dieses Codes können Sie die Accelerometer- und Gyroscpedaten messen, welche das Arduinoboard erfassen kann. Damit das board nicht die ganze Zeit Daten erfasst gibt es einen "accelerationThreshold"-Parameter, welcher die Datenerfassung erst ab einer schnelleren Bewegung startet. Außerdem kann mithilfe vom "timeCaptured"-Parameter die zeitliche Länge der Datenerfassung angepasst werden.

### (Optional) Bewegunsdaten visualisieren
- Öfnnen Sie den Serial Plotter (Tools > Serial Plotter)
- Möglicherweise müssen sie erneut den Port auswählen (Tools > Port > portname(Arduino Nano 33 BLE))
- Laden sie den Code mithilfe vom "Upload" auf das Arduinoboard
- Nun können Sie das Board in die Hand nehmen und eine Bewegung durchführen, wobei diese idealerweise ruckartig und kurz sein sollte
Der Serial Plotter zeigt Ihnen mithilfe von 6 verschiedenen Parametern die erfassten Sensordaten an. Probieren Sie nach belieben herum.

### Bewegungsdaten erfassen
Nun müssen die Bewegungen aufgenommen werden, um im nächsten Schritt zu einem model trainiert werden zu können. Damit die Bewegungen später gut unterschieden werden können, führen Sie die diese am besten schnell und kurz aus. Außerdem ist es wichtig das Arduinoboard immer gleich zu halten, da die Sensordaten sonst vertauscht sein könnten.
- Öfnnen sie den Serial Monitor in der Arduino IDE (Tools > Serial Monitor)
- Nachdem der Code auf das Board geladen ist werden Ihnen bei Bewegung hier eine Menge an Sensordaten angezeigt
- Nun entscheiden Sie sich für eine Bewegung, welche Sie aufnehmen wollen und nehmen das Board in die Hand
- Falls bereits Sensordaten im Serial Monitor angezeigt werden klicken sie auf den kleinen weißen Knopf oben rechts vom Serial Monitor
- Führen sie die Bewegung aus und kehren Sie danach langsam wieder zurück in die Ausgangssituation, damit die Erfassung der Sensordaten nicht noch einmal ausgelöst wird
- Wiederholen Sie die Bewegung mehrmals, damit später ein genaues Model trainiert werden kann (Im Optimalfall mindestens 10 mal)
- Erstellen Sie eine neue Textdatei namens "Bewegungsname.csv" und kopieren Sie alle erfassten Bewegungsdaten rein
- Die erste Zeile der csv datei muss dabei wie folgt aussehen: "aX,aY,aZ,gX,gY,gZ"
- Leeren sie den Serial Monitor und wiederholen Sie diesen Vorgang mit allen Bewegungen

Nachdem Sie alle Bewegung aufgenommen und die csv dateien abgespeichert haben, fahren Sie mit dem nächsten Kapitel fort.

## 5. Bewegungsdaten trainieren

## 6. Bewegungserkennung

## 7. Tastenzuweisung

## 8. Trouble Shooting