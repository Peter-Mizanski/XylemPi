#main.py
#this class deals with bringing the other classes togather

from datetime import datetime
import tkinter as tk
from gui import GUI
from sensor_setup import SensorSetup
from sensors import Moisture, Temperature, Humidity, Pressure, Luminosity
from irrigation_logic import IrrigationLogic
from valve_controller import ValveController
from xylempi_database import XylemPiDatabase

class Main:
    def __init__(self, root):
        self.root = root
        self.gui = GUI(root)
        self.sensor_setup = SensorSetup()
        self.moisture = Moisture(self.gui.moisture_frame)
        self.luminosity = Luminosity(self.gui.luminosity_frame)
        self.temperature = Temperature(self.gui.temperature_frame)
        self.humidity = Humidity(self.gui.humidity_frame)
        self.pressure = Pressure(self.gui.pressure_frame)
        self.irrigation_logic = IrrigationLogic()
        self.valve_controller = ValveController()
        self.db = XylemPiDatabase('xylempidb', 'pi', '', 'localhost')
        
        self.timestamp_label = tk.Label(self.gui.timestamp_frame, text="Last Reading: ", font=("Impact", 14), bg="thistle3")
        self.timestamp_label.grid(row=0, column=0, padx=7, pady=7)
                
        self.irrigation_label = tk.Label(self.gui.irrigation_frame, text="Irrigation Status: ", font=("Impact", 14), bg="thistle3")
        self.irrigation_label.grid(row=0, column=0, padx=7, pady=7)
        
        self.valve_label = tk.Label(self.gui.valve_frame, text="Valve Status: ", font=("Impact", 14), bg="thistle3")
        self.valve_label.grid(row=0, column=0, padx=7, pady=7)
        
        self.score_label = tk.Label(self.gui.score_frame, text="Score Frame Text", font=("Impact", 14), bg="thistle3")
        self.score_label.grid(row=0, column=0, padx=7, pady=7)
        
        self.irrig_message = ""
        
        #bool to track valve status
        self.valve_opened = False
        
        self.update_readings()
        
    def update_readings(self):    
        moisture_status = self.sensor_setup.read_moisture()
        temperature = self.sensor_setup.read_temperature()
        humidity = self.sensor_setup.read_humidity()
        pressure = self.sensor_setup.read_pressure()
        luminosity = self.sensor_setup.read_luminosity()
        
        irrig_message = ""
        
        if not self.valve_opened:
            irrig_message = self.irrigation_logic.check_conditions(moisture_status, temperature, humidity, luminosity)
            
            now = datetime.now()
            timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")
            self.timestamp_label.config(text="Last Reading: " + timestamp_str)
            
            irrig_score = self.irrigation_logic.x
            irrig_thresh = self.irrigation_logic.threshold
            
            self.moisture.update_moisture_reading(moisture_status)
            self.temperature.update_temperature_reading(temperature)
            self.humidity.update_humidity_reading(humidity)
            self.pressure.update_pressure_reading(pressure)
            self.luminosity.update_luminosity_reading(luminosity)
            self.irrigation_label.config(text=irrig_message)
            self.score_label.config(text="Irrigation Score is: " + str(irrig_score) + " out of " + str(irrig_thresh))
            
            self.db.insert_sensor_readings(moisture_status, temperature, humidity, pressure, luminosity, irrig_score, now)
        
        if irrig_message == "Time \nto water \nthe plants. \nActivate \nSolenoid!" and not self.valve_opened:
            valve_status = self.valve_controller.open_valve()
            self.valve_label.config(text=valve_status)
            self.valve_opened = True
            self.root.after(8000, self.close_valve_and_resume_reading)
        
        self.root.after(3000, self.update_readings)
        
        #re-init x
        self.irrigation_logic.x = 0
        
    def close_valve_and_resume_reading(self):
        valve_status = self.valve_controller.close_valve()
        self.valve_label.config(text=valve_status)
        self.valve_opened = False
            
    def exit_program(self):
        self.root.destroy()
        
    def show_db(self):
        db_data = self.db.fetch_sensor_data()
        self.db_window = tk.Toplevel(self.root)
        self.db_window.title("Historical Sensor Data")
        self.db_read_text = tk.Text(self.db_window, width=80, height=20)
        self.db_read_text.insert(tk.END, "Sensor Readings:\n")
        for reading in db_data:
            self.db_read_text.insert(tk.END, str(reading) + "\n")
        self.db_read_text.pack(padx=20, pady=20)
            
if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()
