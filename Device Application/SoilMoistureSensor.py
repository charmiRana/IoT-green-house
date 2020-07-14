'''
Created on 16-Apr-2020

@author: Ranac
'''
from labs.common.SensorData import SensorData
from labs.module10.SensorValueGenerator import SensorValueGenerator
import logging
import threading

class SoilMoistureSensor(threading.Thread):

    def __init__(self):
        self.data = SensorData()
        self.Moisture = SensorValueGenerator()
        logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG) # logging basic data
        
        ''' if(moistureValue > 20 and moistureValue < 300):
            print("\n Soil is DRY !! ADD WATER !!")
            logging.info(" *** SOIL IS DRY!!  Opening water valve!!! ***")
        if(moistureValue > 300 and moistureValue < 700):
            print("\n soil is wet enough!! ")
            logging.info(" *** SOIL IS WET ENOUGH !! WATER VALVE IS CLOSED!! ***")
        '''
        
    def SoilMoistureValue(self):
        moistureValue = self.Moisture.SoilMoistureEmulator()
        return moistureValue
