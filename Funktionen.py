import sensoren_self as s
import errechnete_Daten as D

# Funktion, um Sensorwerte zu erhalten
def get_sensor_data():
    sensor_data = {
        "SoG": s.SoGSensor(),
        "CoG": s.CoGSensor(),
        "Heading": s.HeadingSensor(),
        "TWS": D.TrueWindSpeed(),
        "TWA": D.TrueWindAngle(),
        "StW": s.StWSensor(),
        "AWS": s.ApWindSpeedSensor(),
        "AWA": s.ApWindAngleSensor(),
        "Rudder": s.RudderAngleSensor(),
        "Current": D.Current()

    }
    return sensor_data

print(get_sensor_data())