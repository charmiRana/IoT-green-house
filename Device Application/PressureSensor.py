'''
Created on 16-Apr-2020

@author: Ranac
'''
from labs.common.SensorData import SensorData
from sense_hat import SenseHat
import logging
import threading

class PressureSensor(threading.Thread):
    
    def __init__(self):
        self.data = SensorData()
        logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG) # logging basic data
    '''generating pressure from sense hat API '''    
    def Pressure(self):
        sensData = SenseHat()
        sense = sensData.get_pressure()
        logging.info("Pressure Value:: " + str(sense))
        return sense
        