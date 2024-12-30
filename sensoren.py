import random

class Sensor:
    """Grundlegende Sensor-Klasse."""
    def __init__(self, name: str):
        self.name = name

    def get_data(self):
        """Abstrakte Methode, die von spezifischen Sensoren überschrieben wird."""
        raise NotImplementedError("Diese Methode sollte in einer Unterklasse implementiert werden.")


class HeadingSensor(Sensor):
    """Simuliert einen Kompass-Sensor."""
    def __init__(self):
        super().__init__("Kompass")
        self.current_heading = random.uniform(0, 360)  # Initiale Zufallsrichtung

    def get_data(self):
        # Simulierte Änderung der Heading (z. B. durch Bootsdrehung)
        self.current_heading += random.uniform(-1, 1)  # Leichte Schwankung
        self.current_heading %= 360  # Wertebereich: 0–360 Grad
        return round(self.current_heading, 2)  # Rückgabe des Kurses


class WindSensor(Sensor):
    """Simuliert einen Wind-Sensor."""
    def __init__(self):
        super().__init__("Wind")
        self.wind_speed = random.uniform(5, 20)  # Windgeschwindigkeit in Knoten
        self.wind_direction = random.uniform(0, 360)  # Windrichtung

    def get_data(self):
        # Simulierte Schwankungen in Windrichtung und -geschwindigkeit
        self.wind_speed += random.uniform(-0.5, 0.5)
        self.wind_speed = max(0, self.wind_speed)  # Keine negativen Geschwindigkeiten
        self.wind_direction += random.uniform(-2, 2)
        self.wind_direction %= 360  # Wertebereich: 0–360 Grad
        return {
            "speed": round(self.wind_speed, 2),
            "direction": round(self.wind_direction, 2)
        }

class SoGSensor(Sensor):
    """Simuliert Geschwindigkeit über Grund."""
    def __init__(self):
        super().__init__("SoG")
        self.SoG = random.uniform(0, 15)  # Bootsgeschwindigkeit in Knoten

    def get_data(self):
        # Simulierte Schwankungen in Bootsgeschwindigkeit
        self.SoG += random.uniform(-0.5, 0.5)
        self.SoG = max(0, self.SoG)  # Keine negativen Geschwindigkeiten

        return round(self.SoG, 2)
    
class StWSensor(Sensor):
    """Simuliert Geschwindigkeit über Grund."""
    def __init__(self):
        super().__init__("StW")
        self.StW = random.uniform(0, 15)  # Bootsgeschwindigkeit in Knoten

    def get_data(self):
        # Simulierte Schwankungen in Bootsgeschwindigkeit
        self.StW += random.uniform(-0.5, 0.5)
        self.StW = max(0, self.StW)  # Keine negativen Geschwindigkeiten

        return round(self.StW, 2)
    
class CoGSensor(Sensor):
    """Simuliert einen Kompass-Sensor."""
    def __init__(self):
        super().__init__("CoG")
        self.CoG = random.uniform(0, 360)  # Initiale Zufallsrichtung

    def get_data(self):
        # Simulierte Änderung der Heading (z. B. durch Bootsdrehung)
        self.CoG += random.uniform(-1, 1)  # Leichte Schwankung
        self.CoG %= 360  # Wertebereich: 0–360 Grad
        return round(self.CoG, 2)  # Rückgabe des Kurses
    
class RudderSensor(Sensor):
    """Simuliert einen Kompass-Sensor."""
    def __init__(self):
        super().__init__("Rudder Angle")
        self.rudder = random.uniform(0, 90)  # Initiale Zufallsrichtung

    def get_data(self):
        # Simulierte Änderung der Heading (z. B. durch Bootsdrehung)
        self.rudder += random.uniform(-1, 1)  # Leichte Schwankung
        self.rudder %= 90  # Wertebereich: 0–360 Grad
        return round(self.rudder, 2)  # Rückgabe des Kurses

# Beispielhafte Verwendung der Sensoren
if __name__ == "__main__":
    compass = HeadingSensor()
    CoG_sensor = CoGSensor()
    wind = WindSensor()
    SoG_sensor=SoGSensor()
    StW_sensor=StWSensor()
    rudder_sensor=RudderSensor()

    for _ in range(5):  # Fünf Abfragen simulieren
        print(f"Kompass: {compass.get_data()}°")
        print(f"CoG: {CoG_sensor.get_data()}°")
        wind_data = wind.get_data()
        print(f"Wind: {wind_data['speed']} Knoten, {wind_data['direction']}°")
        print(f"SoG: {SoG_sensor.get_data()}kn")
        print(f"StW: {StW_sensor.get_data()}kn")
        print(f"Rudder Angle: {rudder_sensor.get_data()}°")
        print("-" * 30)