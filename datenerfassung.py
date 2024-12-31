import json
import csv
import time
from datetime import datetime
from sensoren import HeadingSensor, CoGSensor, WindSpd, WindDir, SoGSensor, StWSensor, RudderSensor

def main():
    # Initialisiere Sensoren
    sensors = [
        HeadingSensor(),
        CoGSensor(),
        WindSpd(),
        WindDir(),
        SoGSensor(),
        StWSensor(),
        RudderSensor()
    ]

    # Erstelle Dateinamen mit Zeitstempel
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_filename = f"sensor_data_{timestamp}.json"
    csv_filename = f"sensor_data_{timestamp}.csv"

    # Initialisiere Datencontainer
    collected_data = []

    try:
        while True:
            # Lese Daten von allen Sensoren aus
            sensor_data = {sensor.name: sensor.get_data() for sensor in sensors}

            # Füge Zeitstempel hinzu
            sensor_data["timestamp"] = datetime.now().isoformat()

            # Sammle die Daten
            collected_data.append(sensor_data)

            # Schreibe Daten in JSON-Datei
            with open(json_filename, "w") as json_file:
                json.dump(collected_data, json_file, indent=4)

            # Schreibe Daten in CSV-Datei
            with open(csv_filename, "w", newline="") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=sensor_data.keys())
                if csv_file.tell() == 0:  # Wenn die Datei leer ist, schreibe die Header
                    writer.writeheader()
                writer.writerows(collected_data)

            # Warte 1 Sekunde bis zur nächsten Messung
            time.sleep(1)

    except KeyboardInterrupt:
        print("Datenerfassung beendet.")

if __name__ == "__main__":
    main()
