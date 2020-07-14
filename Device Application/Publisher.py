'''
Created on 16-Apr-2020

@author: Ranac
'''
import logging
import paho.mqtt.client as mqtt
from time import sleep
from labs.module10.MqttClientConnector import MqttClientConnector
from labs.common.DataUtil import DataUtil
from labs.module10.MultiSensorAdaptorTask import MultiSensorAdaptorTask
from labs.common.SensorData import SensorData

class publisher():
    
    def __init__(self):
        logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        self.connector = MqttClientConnector()
        self.datautil = DataUtil()
        self.broker_address = "broker.hivemq.com"
        self.port = 1883
        self.client_id = "Charmi"
        self.password = None
        self.mul = MultiSensorAdaptorTask()
    
    '''connecting with mqtt client and defining callbacks on class MqttClientConnector
    and publushing data after checking topic'''            
    def publish(self ):
        logging.info("Running publisher")
        client = mqtt.Client("Charmi")
        client.username_pw_set(self.client_id, self.password)
        client.connect(self.broker_address, self.port)
        logging.info("Connected !!!")
        client.loop_start()
        while True: #comment this for PING control Packets
            sleep(2)
            data = self.datautil.toJsonFromSensorData(self.mul.run())
            print(data)
            client.on_connect = self.connector.on_connect(client, self.mul.run())
            client.publish("test", data, 2,True)