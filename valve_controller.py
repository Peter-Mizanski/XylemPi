#valve_controller.py
#handles the opening and closing of the solenoid valve

import smbus

class ValveController:
    def __init__(self, device_addr=0x10):
        self.device_addr = device_addr
        self.bus = smbus.SMBus(1)
    
    def open_valve(self):
        self.bus.write_byte_data(self.device_addr, 4, 0xFF)
        return "Opening \nSolenoid \nValve!"
    
    def close_valve(self):
        self.bus.write_byte_data(self.device_addr, 4, 0x00)
        return "Closing \nSolenoid \nValve; \nResuming \nSensor \nReading."