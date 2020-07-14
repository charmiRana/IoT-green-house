'''
Created on 19-Apr-2020

@author: Ranac
'''
import psutil #importing psutil lib
import logging

class SystemCpuUtilTask:
    '''checkign cpu utilization'''
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG) # logging basic data
    
    def getDataFromSensor(self):
        cpu_usage = psutil.cpu_percent() #using psutil for getting cpu_percentage value
        logging.info("Cpu Utilization: " + str(cpu_usage))
        return cpu_usage
    
    def getData(self):
        memory_info = psutil.virtual_memory().percent #using psutil for memory utilisation percentage
        logging.info("Memory Utilization: " + str(memory_info))
        return memory_info