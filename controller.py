# controller.py
# Dieses Skript steuert das Verhalten des Bootsystems, basierend auf Sensordaten, 
# und implementiert grundlegende Steuerungslogik. Es verwendet die `sensoren.py`, 
# um auf Sensordaten zuzugreifen.

# Import der gesamten Datei sensoren.py, um alle Sensor-Klassen zu verwenden
import sensoren
import time

# Klasse, die den Controller definiert
class BoatController:
    """
    Hauptklasse zur Steuerung des Bootssystems.
    Diese Klasse verwaltet die Sensoren und implementiert eine Logik zur Bootsteuerung.
    """

    def __init__(self):
        # Initialisierung der Sensoren aus der sensoren.py
        self.heading_sensor = sensoren.HeadingSensor()
        self.wind_dir_sensor = sensoren.WindDir()
        self.wind_spd_sensor = sensoren.WindSpd()
        self.sog_sensor = sensoren.SoGSensor()
        self.stw_sensor = sensoren.StWSensor()
        self.cog_sensor = sensoren.CoGSensor()
        self.rudder_sensor = sensoren.RudderSensor()

    def get_sensor_data(self):
        """
        Ruft Daten von allen Sensoren ab und gibt sie in einer geordneten Struktur zurück.
        """
        sensor_data = {
            "Heading": self.heading_sensor.get_data(),
            "Wind Direction": self.wind_dir_sensor.get_data(),
            "Wind Speed": self.wind_spd_sensor.get_data(),
            "Speed over Ground (SoG)": self.sog_sensor.get_data(),
            "Speed through Water (StW)": self.stw_sensor.get_data(),
            "Course over Ground (CoG)": self.cog_sensor.get_data(),
            "Rudder Angle": self.rudder_sensor.get_data(),
        }
        return sensor_data

    def control_logic(self):
        """
        Hauptlogik des Controllers. Basierend auf Sensordaten wird die Steuerung des Bootes angepasst.
        Beispiel: Hier kann die Logik implementiert werden, die den Rudder-Winkel anpasst,
        um Kursabweichungen zu korrigieren.
        """
        data = self.get_sensor_data()

        # Beispiel für eine einfache Steuerungslogik:
        # Wenn der Kurs (Heading) stark von der gewünschten Richtung abweicht, 
        # könnte der Rudder-Winkel angepasst werden.
        print("Aktuelle Sensordaten:")
        for key, value in data.items():
            print(f"{key}: {value}")
        
        # Beispiel: Steuerlogik (noch nicht vollständig implementiert)
        # Ziel könnte z. B. sein, Heading nahe bei 90° zu halten
        target_heading = 90
        heading_error = target_heading - data["Heading"]

        if abs(heading_error) > 5:  # Beispiel: Toleranz von 5°
            if heading_error > 0:
                print("Korrektur: Rudder nach Steuerbord (rechts)")
                # Steuerbord (positiver Winkel)
            else:
                print("Korrektur: Rudder nach Backbord (links)")
                # Backbord (negativer Winkel)
        else:
            print("Kurs stabil, keine Korrektur erforderlich.")

    def run(self):
        """
        Führt die Steuerungslogik in einem regelmäßigen Intervall aus.
        """
        try:
            while True:
                self.control_logic()
                time.sleep(1)  # Zeitintervall in Sekunden
        except KeyboardInterrupt:
            print("Steuerung beendet.")

# Hauptprogramm
if __name__ == "__main__":
    # Erstelle eine Instanz des BoatController
    controller = BoatController()
    # Starte die Steuerung
    controller.run()