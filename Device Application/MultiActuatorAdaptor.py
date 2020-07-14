'''
Created on 18-Apr-2020

@author: Ranac
'''
from labs.common.ActuatorData import ActuatorData
from labs.module10.SenseHatLedActivator import SenseHatLedActivator
from google.protobuf.internal.test_bad_identifiers_pb2 import message
import logging
from labs.module10.SmtpClientConnector import SmtpClientConnector
from time import sleep
from labs.module10.SystempCpuUtilTask import SystemCpuUtilTask

class MultiActuatorAdaptorTask():
    
    def __init__(self): 
        self.LedActivate = SenseHatLedActivator()
        self.acdata = ActuatorData()
        self.sendMessage = SmtpClientConnector()
        logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG) # logging basic data
        self.cpuUtil = SystemCpuUtilTask()
            
    '''update command for activation of led'''    
    def UpdateActuator(self, topic, value):
        sensehat = SenseHatLedActivator()
        if(topic == "/v1.6/devices/greenhousehandler/temperatureactuator"):
            if(int(value) == 90):
                logging.info("Temperature Value is greater than plant capacity, Decrease Temperature!!!")
                message = "TempIncreased"
                sensehat.Activate_Led(message)
                sleep(2)
                data = self.cpuUtil.getDataFromSensor()
                DeviceUtil = "Device Utilization /n" + data + "Lower the temperature" 
                self.sendMessage.publishMessage("Decreased temperature and Device Util", DeviceUtil)
                
            else:
                logging.info("Temperature has been decreased!! Increaase the Temperature!!!")
                message = "TempDecreaased"
                sensehat.Activate_Led(message)
                sleep(2)
                self.sendMessage.publishMessage("Decreased temperature", int(value))
                DeviceUtil = "Device Utilization /n" + data + "Increse the temperature" 
                self.sendMessage.publishMessage("Increased temperature and Device Util", DeviceUtil)
                
                
        elif(topic == "/v1.6/devices/greenhousehandler/humidityactuator"):
            if(int(value) == 100):
                logging.info("Humidity value has been increased!! Please turn on the fan!!")
                message = "HumidityIncreased"
                sensehat.Activate_Led(message)
                sleep(2)
                self.sendMessage.publishMessage("Decreased temperature", int(value))
                
            else:
                logging.info("Humidity value has been decreased!! Spray some water please!!")
                message = "HumidityDecreased"
                sensehat.Activate_Led(message)
                sleep(2)
                self.sendMessage.publishMessage("Decreased temperature", int(value))
                
        elif(topic == "/v1.6/devices/greenhousehandler/pressureactuator"):
            if(int(value) == 1500):
                logging.info("Pressure value has been increased!! Control Temperature and Humidity!!")
                message = "PressurevalueIncreased"
                sensehat.Activate_Led(message)
                sleep(2)
                self.sendMessage.publishMessage("Decreased temperature", int(value))
                
            else:
                logging.info("Humidity value has been decreased!! Please turn on the fan!!")
                message = "PressurevalueDecresed"
                sensehat.Activate_Led(message)
                sleep(2)
                self.sendMessage.publishMessage("Decreased temperature", int(value))
                
        elif(topic == "/v1.6/devices/greenhousehandler/gasactuator"):
            if(int(value) == 1600):
                logging.info("Gas value has been increased!! Increase Co2 value!!")
                message = "Co2Increased"
                sensehat.Activate_Led(message)
                sleep(2)
                self.sendMessage.publishMessage("Decreased temperature", int(value))
                
            else:
                logging.info("Gas value has been decreased!! Decrease Co2 value!!")
                message = "Co2Decreased"
                sensehat.Activate_Led(message)
                sleep(2)
                self.sendMessage.publishMessage("Decreased temperature", int(value))
                
        elif(topic == "/v1.6/devices/greenhousehandler/lightactuator"):
            if(int(value) == 800):
                logging.info("Light Level value has been increased!! Dim the lights!!")
                message = "LightLevelIncresed"
                sensehat.Activate_Led(message)
                sleep(2)
                self.sendMessage.publishMessage("Decreased temperature", int(value))
                
            else:
                logging.info("Gas value has been decreased!! Bright the lights!!")
                message = "LightLevelDecresed"
                sensehat.Activate_Led(message)
                sleep(2)
                self.sendMessage.publishMessage("Decreased temperature", int(value))
                
        elif(topic == "/v1.6/devices/greenhousehandler/soilphactuator"):
            if(int(value) == 7):
                logging.info("PH value has passed 6.5!!  Time to add sulfur")
                message = "PhIncreased"
                sensehat.Activate_Led(message)
                sleep(2)
                self.sendMessage.publishMessage("Decreased temperature", int(value))
                
            else:
                logging.info("PH value has been decreased!! Time to add wood Ashes!! ")
                message = "PhDecreased"
                sensehat.Activate_Led(message)
                sleep(2)
                self.sendMessage.publishMessage("Decreased temperature", int(value))
                
        elif(topic == "/v1.6/devices/greenhousehandler/soilmoistureactuator"):
            if(int(value) == 800):
                logging.info("Soil is too wet!! Decrease Co2 value!!")
                message = "SoilmoistureIncreased"
                sensehat.Activate_Led(message)
                sleep(2)
                self.sendMessage.publishMessage("Decreased temperature", int(value))
                
            else:
                logging.info("Soil is too dry!! Turn on the Water pump!!")
                message = "soilmoistureDecreased"
                sensehat.Activate_Led(message)
                sleep(2)
                self.sendMessage.publishMessage("Decreased temperature", int(value))
            
        return True
