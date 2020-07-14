'''
Created on 15-Apr-2020

@author: Ranac
'''
from labs.common.SensorData import SensorData
import threading
from sense_hat import SenseHat
import logging

class TempSensorAdaptorTask(threading.Thread):

    def __init__(self):
        self.data = SensorData()
        logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG) # logging basic data
        
    ''' get sensordata from senshat API'''
    def run(self):
        sensData = SenseHat() #instance of SenseHat
        sense = sensData.get_temperature() #calling method get_Temperature for SenseHat
#         self.data.setName('Temperature')
        self.data.addValue(sense) #updating values using addvalue method 
#         print(self.data.getRecord()) #printing record
        logging.info("Temperature Value: " + str(self.data.getCurrentValue()))
#         json = "Temperature Value:"+ str(self.data.getCurrentValue())
        data = self.data.getCurrentValue()
        return sense