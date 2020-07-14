'''
Created on 18-Apr-2020

@author: Ranac
'''
import threading
import paho.mqtt.client as mqtt
from labs.module10.MqttClientConnector import MqttClientConnector
from labs.common import DataUtil
from time import sleep
import logging
from paho.mqtt.client import MQTTMessage

class subscriber():
    
    def __init__(self):
        logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG) # logging basic data
#         self.broker_address = "broker.hivemq.com"
        self.broker_address = "mqtt.eclipse.org"
        self.port = 1883
        self.client_id = "charm"
        self.qos = 1
        ''' instances from classes'''
        self.datautil = DataUtil.DataUtil()
        '''all callbacks'''
        self.connector = MqttClientConnector()
    #   qos = 1 # for Publish Ack 
    
    ''' subscribe the channel to get data and send it to actuate'''
    def run(self, topic):
        logging.info("Running subscriber")
        client = mqtt.Client("charm")
        client.on_connect = self.connector.on_connect
        client.connect(self.broker_address, self.port)
        client.loop_start()
        while True:
            sleep(3)
            client.on_subscribe= self.connector.on_subscribe
            client.on_message = self.connector.on_message
            client.subscribe(topic , 1)
