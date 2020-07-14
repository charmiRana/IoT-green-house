'''
Created on 15-Apr-2020

@author: Ranac
'''
import threading
from sense_hat import SenseHat
import logging
from labs.common.SensorData import SensorData

class HumiditySensorAdaptorTask(threading.Thread):
    
    def __init__(self):
        logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG) # logging basic data
        self.data = SensorData()

    '''get humidity data with sensehat API'''
    def getHumidData(self):
        sensData = SenseHat() #instance of SenseHat
        sense = sensData.get_humidity() #calling method get_Temperature for SenseHat
        logging.info("Humidity Value: " + str(sense))
        return sense