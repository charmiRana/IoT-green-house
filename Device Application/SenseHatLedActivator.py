'''
Created on 18-Apr-2020

@author: Ranac
'''
from sense_hat import SenseHat #importing SenseHAT

class SenseHatLedActivator():
    
    global sense
    sense = SenseHat() #Created instance of SenseHat
    
    '''method for activating LED and create actuation using commands given from gateway'''
    def Activate_Led(self, command): 
        green = (0,255,0)
        blue = (0,0,255)
            
        if (command == "TempIncreased"): 
            print("temp increased")
#             sense.clear() #using clear for no color
#             logging.info("temp actuator led is active -- Temperature Increased") 
#             sense.clear(blue)
        elif (command == "TempDecreaased"):
            print("temp decreased")
#             sense.clear()
#             logging.info("temp Actuator led is active -- Temperature decreased")
#             sense.show_message("Decreased")
#             sense.clear(green)
        elif (command == "HumidityIncreased"):
            print("Turning the fan on!!")
        elif (command == "HumidityDecreased"):
            print("Water Sprayed!!")
            
        elif (command == "PressurevalueIncreased"):
            print("Decreasing Pressure")
        elif (command == "PressurevalueDecresed"):
            print("Increasing pressure")
            
        elif (command == "Co2Increased"):
            print("Decreasing Co2")
        elif (command == "Co2Decreased"):
            print("Increasing Co2")
            
        elif (command == "LightLevelIncresed"):
            print("Dimmed the Lights")
        elif (command == "LightLevelDecresed"):
            print("Turned lights on")

