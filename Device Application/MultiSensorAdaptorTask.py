'''
Created on 16-Apr-2020

@author: Ranac
'''
from labs.module10.TempSensorAdaptorTask import TempSensorAdaptorTask
from labs.module10.HummiditySensorAdaptorTask import HumiditySensorAdaptorTask
from labs.module10.PressureSensor import PressureSensor
from labs.module10.SoilMoistureSensor import SoilMoistureSensor
from labs.module10.Luminance import LuminanceSensor
from labs.module10.GasSensor import GasSensor
from labs.module10.PhMeter import Phmeter
from time import sleep
from labs.common.DataUtil import DataUtil
from labs.module10.AllSensorData import AllSensorData
from labs.module10.SystempCpuUtilTask import SystemCpuUtilTask
from labs.module10.SmtpClientConnector import SmtpClientConnector

class MultiSensorAdaptorTask(object):

    def __init__(self):
        self.temp = TempSensorAdaptorTask()
        self.humidity = HumiditySensorAdaptorTask()
        self.pressure = PressureSensor()
        self.soilmoisture = SoilMoistureSensor()
        self.Luminance = LuminanceSensor()
        self.gas = GasSensor()
        self.phvalue = Phmeter()
        self.datautil = DataUtil()
        self.all = AllSensorData()
        self.cpuUtil = SystemCpuUtilTask()
        self.send = SmtpClientConnector()
        
    ''' getting all the sensor data from random value generator here with cpu utilization'''   
    def run(self):
        tempdata = self.temp.run()
        humidity = self.humidity.getHumidData()
        pressuredata = self.pressure.Pressure()
        soilmoisturedata = self.soilmoisture.SoilMoistureValue()
        light = self.Luminance.Luminance()
        gas = self.gas.gasSensorvalue()
        ph = self.phvalue.PhValue()
        cpu = self.cpuUtil.getDataFromSensor()
        mem = self.cpuUtil.getData()
        self.all.setTemperature(tempdata)
        self.all.setHumidity(humidity)
        self.all.setPressure(pressuredata)
        self.all.setSoilMoisture(soilmoisturedata)
        self.all.setGasValue(gas)
        self.all.setPhValue(ph)
        self.all.setLuminance(light)
        self.all.setCpuUtil(cpu)
        
        
        data = self.all.getAllData(tempdata, humidity, pressuredata, light, ph, gas, soilmoisturedata, cpu)
        print(data)
        
        self.send.publishMessage("Sensor Data", data)
        self.all.getAllData(tempdata, humidity, pressuredata, light, ph, gas, soilmoisturedata, cpu)
        return self.all