import tkinter as tk  # Importiert das tkinter-Modul, das für die GUI-Erstellung verwendet wird.
import sensoren_self as s 
import errechnete_Daten as D

# Sensoren
SoG = round(s.SoGSensor(), 2)
CoG = round(s.CoGSensor(), 2)
heading = round(s.HeadingSensor(), 2)
wind_s = round(D.TrueWindSpeed(), 2)
wind_a = round(D.TrueWindAngle(), 2)
StW = round(s.StWSensor(), 2)

# Designkonfig
w_colour = "white"
b_colour = "black"
space_x = 10
space_y = 10
size_y = 100
size_x = 180

root = tk.Tk()
root.title('Sensordaten')

# SoG Anzeige
frame = tk.Frame(bg=b_colour, width=size_x, height=size_y)
frame.pack_propagate(False)
frame.grid(row=1, column=1, padx=space_x, pady=space_y)

label_title = tk.Label(frame, text='SoG', font=("Arial", 16), fg=w_colour, bg=b_colour)
label_title.pack()

label_value = tk.Label(frame, text=f"{SoG}kn", font=("Arial", 36, "bold"), fg=w_colour, bg=b_colour)
label_value.pack()

# CoG Anzeige
frame = tk.Frame(bg=b_colour, width=size_x, height=size_y)
frame.pack_propagate(False)
frame.grid(row=1, column=2, padx=space_x, pady=space_y)

label_title = tk.Label(frame, text='CoG', font=("Arial", 16), fg=w_colour, bg=b_colour)
label_title.pack()

label_value = tk.Label(frame, text=f'{CoG}°', font=("Arial", 36, "bold"), fg=w_colour, bg=b_colour)
label_value.pack()

# Heading Anzeige
frame = tk.Frame(bg=b_colour, width=size_x, height=size_y)
frame.pack_propagate(False)
frame.grid(row=2, column=2, padx=space_x, pady=space_y)

label_title = tk.Label(frame, text='Heading', font=("Arial", 16), fg=w_colour, bg=b_colour)
label_title.pack()

label_value = tk.Label(frame, text=f'{heading}°', font=("Arial", 36, "bold"), fg=w_colour, bg=b_colour)
label_value.pack()

# Wind Speed
frame = tk.Frame(bg=b_colour, width=size_x, height=size_y)
frame.pack_propagate(False)
frame.grid(row=1, column=3, padx=space_x, pady=space_y)

label_title = tk.Label(frame, text='TWS', font=("Arial", 16), fg=w_colour, bg=b_colour)
label_title.pack()

label_value = tk.Label(frame, text=f'{wind_s}kn', font=("Arial", 36, "bold"), fg=w_colour, bg=b_colour)
label_value.pack()

# Wind Angle
frame = tk.Frame(bg=b_colour, width=size_x, height=size_y)
frame.pack_propagate(False)
frame.grid(row=2, column=3, padx=space_x, pady=space_y)

label_title = tk.Label(frame, text='TWA', font=("Arial", 16), fg=w_colour, bg=b_colour)
label_title.pack()

label_value = tk.Label(frame, text=f'{wind_a}°', font=("Arial", 36, "bold"), fg=w_colour, bg=b_colour)
label_value.pack()

# Speed through Water
frame = tk.Frame(bg=b_colour, width=size_x, height=size_y)
frame.pack_propagate(False)
frame.grid(row=2, column=1, padx=space_x, pady=space_y)

label_title = tk.Label(frame, text='StW', font=("Arial", 16), fg=w_colour, bg=b_colour)
label_title.pack()

label_value = tk.Label(frame, text=f'{StW}kn', font=("Arial", 36, "bold"), fg=w_colour, bg=b_colour)
label_value.pack()

root.mainloop()