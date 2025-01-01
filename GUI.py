import tkinter as tk
from sensoren import HeadingSensor, CoGSensor, WindSpd, WindDir, SoGSensor, StWSensor, RudderSensor
import time

# Sensoren initialisieren
sensors = {
    "Kompass (°)": HeadingSensor(),
    "CoG (°)": CoGSensor(),
    "Windgeschwindigkeit (kn)": WindSpd(),
    "Windrichtung (°)": WindDir(),
    "SoG (kn)": SoGSensor(),
    "StW (kn)": StWSensor(),
    "Ruderwinkel (°)": RudderSensor()
}

class SensorDashboard(tk.Tk):
    def __init__(self, sensors, interval=500):
        super().__init__()
        self.sensors = sensors
        self.interval = interval  # Intervall in Millisekunden
        self.title("Sensor Dashboard")
        self.geometry("800x400")
        self.configure(bg="black")

        self.labels = {}
        for i, (sensor_name, sensor) in enumerate(sensors.items()):
            frame = tk.Frame(self, bg="black")
            frame.grid(row=i//2, column=i%2, padx=20, pady=20)

            label_title = tk.Label(frame, text=sensor_name, font=("Arial", 16), fg="white", bg="black")
            label_title.pack()

            label_value = tk.Label(frame, text="0", font=("Arial", 36, "bold"), fg="white", bg="black")
            label_value.pack()

            self.labels[sensor_name] = label_value

        self.update_data()

    def update_data(self):
        for sensor_name, sensor in self.sensors.items():
            value = sensor.get_data()
            self.labels[sensor_name].config(text=f"{value}")
        self.after(self.interval, self.update_data)


if __name__ == "__main__":
    app = SensorDashboard(sensors)
    app.mainloop()