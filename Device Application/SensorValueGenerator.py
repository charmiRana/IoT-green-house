'''
Created on 16-Apr-2020

@author: Ranac
'''
from labs.common.SensorData import SensorData
import random
import logging

class SensorValueGenerator(object):

    def __init__(self):
        self.data = SensorData()
        self.newValue = 0
        logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG) # logging basic data
    
    
    ''' generated random wave length of light (quantum sensor)
        light intensity between 400 to 700 nm is defined as good for photosynthesis.
        intensity  > 770 nm have heating effect
        green (495-566nm), yellow (566-589nm) - both for photosynthesis, 
        orange (589-627 nm) - for max photosynhesis, 
        red light (627-770 nm)- for enhance flowering        
    '''
    def LuminanceEmulator(self):
        self.newValue = random.uniform(300, 800)
        logging.info("Luminance value: " + str(self.newValue))
        data = "Luminance value : " + str(self.newValue)
        return self.newValue
    
    ''' generated random soil moisture value
        20 to 300 = dry soil
        300 to 700 = wet soil
        > 700 = water
    '''
    def SoilMoistureEmulator(self):
        self.newValue = random.randint(0, 950)
        logging.info("Soil moisture value: " + str(self.newValue))
        data = "SoilMoisture: " + str(self.newValue)
        return self.newValue
    
    ''' co2 sensor MG-811 random values range - 400 to 1000 ppm means 0.04% and 1%
        PPM value > 2000 is toxic for plants
        PPM > 5000 is harmful for people
        PPM = 1500 is maximum for plant growth
        ppm level between 1000 to 1500 is good range for plants
    '''
    def GasEmulator(self):
        self.newValue = random.randint(500, 2100)
        logging.info("Gas value: " + str(self.newValue))
        data = " Gas value : " + str(self.newValue)
        return self.newValue
    
    ''' Generating random ph valus between 5 to 7 
        Ph value between 5.5 to 6.5 is consired as optimum for most of the plants
        Ph value less than 5.5 is more acidic and describes deficiency for soil nutrition nitrogen and phosphorus
    '''
    def PHValueEmulator(self):
        self.newValue = random.uniform(5, 7)
        logging.info("Ph value: "+ str(self.newValue))
        data = "PH value of soil : " + str(self.newValue)
        return self.newValue
        