#sensors.py
#these classes represent the sensor readings in gui

import tkinter as tk

class Moisture:
    def __init__(self, frame):
        self.moisture_label = tk.Label(frame, text="Moisture Status: ", font=("Impact", 14), bg="thistle3")
        self.moisture_label.grid(row=0, column=0, padx=7, pady=7)
    def update_moisture_reading(self, moisture_status):
        self.moisture_label.config(text=moisture_status)
        
        
class Temperature:
    def __init__(self, frame):
        self.temperature_label = tk.Label(frame, text="Temperature Status: ", font=("Impact", 14), bg="thistle3")
        self.temperature_label.grid(row=0, column=0, padx=7, pady=7)
    def update_temperature_reading(self, temperature):
        self.temperature_label.config(text="Temperature = {0:0.1f}ºC".format(temperature))
        
        
class Humidity:
    def __init__(self, frame):
        self.humidity_label = tk.Label(frame, text = "Humidity Status: ", font=("Impact", 14), bg="thistle3")
        self.humidity_label.grid(row=0, column=0, padx=7, pady=7)
    def update_humidity_reading(self, humidity):
        self.humidity_label.config(text="Humidity = {0:0.1f}%".format(humidity))


class Pressure:
    def __init__(self, frame):
        self.pressure_label = tk.Label(frame, text = "Pressure Status: ", font=("Impact", 14), bg="thistle3")
        self.pressure_label.grid(row=0, column=0, padx=7, pady=7)
    def update_pressure_reading(self, pressure):
        self.pressure_label.config(text="Pressure = {0:0.1f}hPa".format(pressure))
        
        
class Luminosity:
    def __init__(self, frame):
        self.luminosity_label = tk.Label(frame, text = "Light Levels Go Here", font=("Impact", 14), bg="thistle3")
        self.luminosity_label.grid(row=0, column=0, padx=7, pady=7)
    def update_luminosity_reading(self, luminosity):
        self.luminosity_label.config(text=luminosity)