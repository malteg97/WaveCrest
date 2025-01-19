import time
import os
import csv
import Funktionen as F
filename = None

def round_values(sensor_data):
    # Runde alle relevanten Werte auf zwei Nachkommastellen
    return {key: round(value, 2) if isinstance(value, (int, float)) else value
            for key, value in sensor_data.items()}

def get_current_time():
    return time.strftime("%Y-%m-%d_%H-%M-%S")  # Ersetze : durch _ für Dateinamen

def initialize_filename():
    global filename
    # Erstelle einen einzigartigen Dateinamen basierend auf der aktuellen Zeit, nur beim ersten Start
    if filename is None:
        filename = f"sensordaten_{get_current_time()}.csv"

def save_data_to_file():
    global filename
    # Sicherstellen, dass der Dateiname initialisiert ist
    initialize_filename()
    sensor_data=F.get_sensor_data()
    sensor_data = round_values(sensor_data)
    
    # Daten zur Datei hinzufügen
    with open(filename, mode="a", newline="") as file:
        fieldnames = ["Time", "SoG", "CoG", "Heading", "TWS", "TWA", "StW", "AWS", "AWA", "Rudder", "Current"]     # Definiere die Felder, die dem Dictionary entsprechen
        writer = csv.DictWriter(file, fieldnames=fieldnames)                    # Erstelle ein DictWriter-Objekt
        if file.tell() == 0:                                                    # Wenn die Datei leer ist, schreibe die Kopfzeile
            writer.writeheader()
        writer.writerow(sensor_data)                                                   # Schreibe das Dictionary als neue Zeile

def periodic_save():
    while True:
        save_data_to_file()
        time.sleep(0.5)  # Speichere alle 500ms