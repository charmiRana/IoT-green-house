'''
Created on 16-Apr-2020

@author: Ranac
'''
from labs.module10.SensorValueGenerator import SensorValueGenerator
import logging
from labs.common.SensorData import SensorData

class GasSensor(object):

    def __init__(self):
        self.sendata = SensorValueGenerator()
        self.data = SensorData()
        logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG) # logging basic data
    
    '''if(gasValue > 1000 | gasValue < 1500):
            print(" Healthy environment --  Enough CO2 for plants")             
        if(gasValue > 2000):
            print("GAS ALERT!! Co2 exceeding in the air")          
        else:
            print(" please increase the co2 value for good growth of plants!!!")
    '''
    def gasSensorvalue(self):
        gasValue = self.sendata.GasEmulator()
        self.data.setName('gasValue') #setting sensor name with setName method
        self.data.getCurrentValue()            
        return gasValue