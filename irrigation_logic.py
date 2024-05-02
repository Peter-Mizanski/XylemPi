#irrigation_logic.py
#handles irrig decision-making based on sensor data

#from sensors import Moisture, Temperature, Humidity

# The logic algorithm uses a point-based scheme
# points are added/subtracted from a total based on
# the values obtained from the sensors. This way,
# the program implements a more sophisticated
# response to the various environmental conditions

class IrrigationLogic:
    def __init__(self):
        self.x = 0
        self.threshold = 30
    
    def check_conditions(self, moisture_status, temperature, humidity, luminosity):
        #adjusting score based on soil moisture:
        if moisture_status == "Soil is Dry":
            self.x += 15
        elif moisture_status == "Soil is Wet":
            self.x -= 15
            
        #adjusting score based on whether it's bright or dark
        if luminosity == "Light Detected":
            self.x += 5
        elif luminosity == "Darkness Detected":
            self.x -= 5
            
        #adjusting score based on temperature:
        if temperature <= 0:
            self.x -= 1000
        elif 0 < temperature and temperature <= 4.9:
            self.x -= 60
        elif 4.9 < temperature and temperature <= 9.9:
            self.x -= 15
        elif 9.9 < temperature and temperature <= 14.9:
            self.x += 0
        elif 14.9 < temperature and temperature <= 19.9:
            self.x += 5
        elif 19.9 < temperature and temperature <= 24.9:
            self.x += 10
        elif 24.9 < temperature and temperature <= 29.9:
            self.x += 15
        elif 29.9 < temperature and temperature <= 34.9:
            self.x += 20
        elif temperature > 34.9:
            self.x += 25
            
        #adjusting score based on humidity:
        if 0 <= humidity < 10:
            self.x += 35
        elif 10 <= humidity and humidity < 20:
            self.x += 30
        elif 20 <= humidity and humidity < 30:
            self.x += 25
        elif 30 <= humidity and humidity < 40:
            self.x += 15
        elif 40 <= humidity and humidity < 50:
            self.x += 10
        elif 50 <= humidity and humidity < 60:
            self.x += 5
        elif 60 <= humidity and humidity < 70:
            self.x += 0
        elif 70 <= humidity and humidity < 80:
            self.x -= 10
        elif 80 <= humidity and humidity < 90:
            self.x -= 15
        elif humidity >= 90:
            self.x -= 25
            
        # point score safeguards:
        # minimum = 0, maximum = 60
        self.x = max(0, self.x)
        self.x = min(60, self.x)
        
        print(self.x)
        
        if self.x >= self.threshold:
            return "Time \nto water \nthe plants. \nActivate \nSolenoid!"
        else:
            return "The plants \nare hydrated!"
