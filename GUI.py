import tkinter as tk
import Funktionen as F

# Designkonfig
w_colour = "white"
b_colour = "black"
space_x = 10
space_y = 10
size_y = 100
size_x = 180

class SensorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sensordaten")
        self.labels = {}
        self.create_gui()

    def create_sensor_tile(self, row, column, title, unit):
        frame = tk.Frame(self.root, bg=b_colour, width=size_x, height=size_y)
        frame.pack_propagate(False)
        frame.grid(row=row, column=column, padx=space_x, pady=space_y)

        label_title = tk.Label(frame, text=title, font=("Arial", 16), fg=w_colour, bg=b_colour)
        label_title.pack()

        label_value = tk.Label(frame, text=f"0 {unit}", font=("Arial", 36, "bold"), fg=w_colour, bg=b_colour)
        label_value.pack()

        return label_value

    def create_gui(self):
        self.labels["SoG"] = self.create_sensor_tile(1, 1, "SoG", "kn")
        self.labels["CoG"] = self.create_sensor_tile(1, 2, "CoG", "°")
        self.labels["Heading"] = self.create_sensor_tile(2, 2, "Heading", "°")
        self.labels["TWS"] = self.create_sensor_tile(1, 3, "TWS", "kn")
        self.labels["TWA"] = self.create_sensor_tile(2, 3, "TWA", "°")
        self.labels["StW"] = self.create_sensor_tile(2, 1, "StW", "kn")

    def update_values(self, sensor_data):
        # Hier werden nur ausgewählte Werte im GUI angezeigt
        self.labels["SoG"].config(text=f"{sensor_data['SoG']:.2f} kn")
        self.labels["CoG"].config(text=f"{sensor_data['CoG']:.2f}°")
        self.labels["Heading"].config(text=f"{sensor_data['Heading']:.2f}°")
        self.labels["TWS"].config(text=f"{sensor_data['TWS']:.2f} kn")
        self.labels["TWA"].config(text=f"{sensor_data['TWA']:.2f}°")
        self.labels["StW"].config(text=f"{sensor_data['StW']:.2f} kn")

root = None
gui = None

# Aktualisiere die GUI in regelmäßigen Intervallen
def init_GUI():
    global root, gui
    root = tk.Tk()
    gui = SensorGUI(root)

def update_GUI():
    global root,gui
    sensor_data = F.get_sensor_data()
    gui.update_values(sensor_data)
    root.after(1000, update_GUI)  # Aktualisiere alle 1 Sekunde