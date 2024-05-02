#sensor_setup.py
#this class is for sensor setup and reading

import RPi.GPIO as GPIO
import bme280
import smbus2

class SensorSetup:
    
    #constructor
    def __init__(self):
        #bme280 + i2c setup
        self.sensor_address = 0x76
        self.i2c_bus = smbus2.SMBus(1)
        self.calibration_params = bme280.load_calibration_params(
            self.i2c_bus, self.sensor_address)
        #GPIO pin setup
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.IN)
        GPIO.setup(23, GPIO.IN)
   
    def read_moisture(self):
        if (GPIO.input(4)) == 0:
            return "Soil is Wet"
        else:
            return "Soil is Dry"
    
    def read_luminosity(self):
        if (GPIO.input(23)) == 0:
            return "Light Detected"
        else:
            return "Darkness Detected"
    
    def read_temperature(self):
        data = bme280.sample(self.i2c_bus, self.sensor_address, self.calibration_params)
        return data.temperature
        
    def read_humidity(self):
        data = bme280.sample(self.i2c_bus, self.sensor_address, self.calibration_params)
        return data.humidity
        
    def read_pressure(self):
        data = bme280.sample(self.i2c_bus, self.sensor_address, self.calibration_params)
        return data.pressure
