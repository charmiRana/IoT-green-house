'''
Created on 16-Apr-2020

@author: Ranac
'''
from labs.common.DataUtil import DataUtil
import paho.mqtt.client as mqtt
import logging
from labs.module10.AllSensorData import AllSensorData
import json
from labs.module10.MultiActuatorAdaptor import MultiActuatorAdaptorTask

class MqttClientConnector():
    
    def __init__(self):
        self.datautil = DataUtil()
        self.all = AllSensorData()
        self.updater = MultiActuatorAdaptorTask()
        
    def on_connect(self, client, data):
        print("\n \n")
        logging.info("Connected !!!")
        
    ''' set PUBACK flag true when message ack received'''
    def on_message(self, client, userdata, message): 
        print("message::")
        print("message received " + str(message.payload.decode("utf-8")))
        payload = str(message.payload.decode("utf-8"))
        data = json.loads(payload)
        print(data)
        print(data["Topic"])
        print(data["value "])
        self.updater.UpdateActuator(data["Topic"], data["value "])
        return data["Topic"]
         
    '''when unsubscribe set UNSUBSCRIBE flag true'''
    def on_unsubscribe(self, topic):
        mqtt.UNSUBSCRIBE = True  
        print("device has successfully unsubscribe to the channel")
    
    def on_subscribe(self, client, userdata, mid, granted_qos):
        print("Subscribed: "+str(mid)+" "+str(granted_qos) +"" + str(userdata))
        logging.info("Subscribed")