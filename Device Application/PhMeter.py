'''
Created on 16-Apr-2020

@author: Ranac
'''
from labs.module10.SensorValueGenerator import SensorValueGenerator
import logging
import threading

class Phmeter(threading.Thread):
    
    def __init__(self):
        self.sensdata = SensorValueGenerator()
        logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG) # logging basic data
    
    '''generating values for ph value of soil
    if ph is greater than 6.5 and less than 5.5 it is harmfull for plants''' 
    def PhValue(self):
        phdata = self.sensdata.PHValueEmulator()
        return phdata