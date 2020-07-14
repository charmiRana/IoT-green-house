'''
Created on 16-Apr-2020

@author: Ranac
'''
from labs.common.SensorData import SensorData
from labs.module10.SensorValueGenerator import SensorValueGenerator
import logging
import threading

class LuminanceSensor(threading.Thread):
    
    def __init__(self):
        self.data = SensorData()
        self.sendata = SensorValueGenerator()
        logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG) # logging basic data
        
        ''' if(Luminance < 589 and Luminance > 495):
                print("\n Intensity of green and yellow is good!!")         
        elif(Luminance < 627 and Luminance > 589):
                print("\n Intensity of Orange is good for maximum Photosynthesis!!")         
        elif(Luminance < 770 and Luminance > 627):        
                print("\n Intensity enhancing flowering")
        else:
            print("\n Luminance is harmful !! plant will burn!!!")
        '''
    def Luminance(self):
        Luminance = self.sendata.LuminanceEmulator()
        self.data.setName('luminance') #setting sensor name with setName method            
        return Luminance
