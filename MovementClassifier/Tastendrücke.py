# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 14:33:31 2023


"moveRight",
"moveLeft",
"rotateRight",
"rotateLeft",
"dropDown",
"safe"


@author: mawea
"""
# Importiere die benötigten Bibliotheken
import serial # Bibliothek zum Lesen der seriellen Daten vom Arduino
from pynput.keyboard import Key, Controller # Bibliothek zum Emulieren der Tastatur

# Öffne die serielle Verbindung mit dem Arduino an Port COM12 und einer Baudrate von 9600
ser = serial.Serial('COM12', 9600)

# Erstelle ein neues Keyboard-Objekt
keyboard = Controller()

# Schleife, die kontinuierlich auf serielle Daten vom Arduino wartet
while True:
            # Lese eine Zeile der seriellen Daten vom Arduino
            data = ser.readline()
    
            # Wenn die empfangene Zeile "dropDown" ist, simuliere das Drücken und Loslassen der "s"-Taste
            if data.decode().strip() == "dropDown":
                keyboard.press("s")
                keyboard.release("s")
    
            # Wenn die empfangene Zeile "moveRight" ist, simuliere das Drücken und Loslassen der "d"-Taste
            if data.decode().strip() == "moveRight":
                keyboard.press("d")
                keyboard.release("d")
    
            # Wenn die empfangene Zeile "moveLeft" ist, simuliere das Drücken und Loslassen der "a"-Taste
            if data.decode().strip() == "moveLeft":
                keyboard.press("a")
                keyboard.release("a")
    
            # Wenn die empfangene Zeile "safe" ist, simuliere das Drücken und Loslassen der "w"-Taste
            if data.decode().strip() == "safe":
                keyboard.press("w")
                keyboard.release("w")
            # Wenn die empfangene Zeile "rotateRight" ist, simuliere das Drücken und Loslassen der "h"-Taste
            if data.decode().strip() == "rotateRight":
                keyboard.press("h")
                keyboard.release("h")
            # Wenn die empfangene Zeile "rotateLeft" ist, simuliere das Drücken und Loslassen der "g"-Taste
            if data.decode().strip() == "rotateLeft":
                keyboard.press("g")
                keyboard.release("g")    