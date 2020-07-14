'''
Created on 18-Apr-2020

@author: Ranac
'''

class AllSensorData(object):
    
    def __init__(self):#initializing
        self.temperature = 0;
        self.humidity =0;
        self.pressure =0;
        self.phvalue =0;
        self.soilmoisture =0;
        self.gasvalue =0;
        self.luminance =0;
        self.cpu =0;
    ''' all sensors which needs to be used in this project '''   
    def getTemperature(self):
        return self.temperature
    def getHumidity(self):
        return self.humidity
    def getPressure(self):
        return self.pressure
    def getPhValue(self):
        return self.phvalue
    def getSoilMoisture(self):
        return self.soilmoisture
    def getGasValue(self):
        return self.gasvalue
    def getLuminance(self):
        return self.luminance
    def getCpuUtil(self):
        return self.cpu
    
    def setTemperature(self, temp):
        self.temperature = temp
        
    def setHumidity(self, hum):
        self.humidity = hum
    def setPressure(self, pres):
        self.pressure = pres
    def setPhValue(self, ph):
        self.phvalue = ph
    def setSoilMoisture(self, soilmoisture):
        self.soilmoisture = soilmoisture
    def setGasValue(self, gas):
        self.gasvalue = gas
    def setLuminance(self, light):
        self.luminance = light
    def setCpuUtil(self, cpu):
        self.cpu = cpu
        
    def getAllData(self, temp, hum, press, light, ph, gas, soilmoisture, cpu):
        return '\n temperature: ' + str(temp) + '\n humidity: ' + str(hum) + '\n pressure: ' + str(press) + '\n phvalue: '+str(ph) + '\n soilmoisture: '+ str(soilmoisture) + '\n gasValue: ' + str(gas) + '\n luminance: ' + str(light) + '\n cpu Utilization' + str(cpu) 
        