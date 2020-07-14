'''
Created on 19-Apr-2020

@author: Ranac
'''
from labs.module10.Subscriber import subscriber
from time import sleep
from threading import Thread

class DeviceSubscriberApp():
    
    def __init__(self):
        self.subscribe = subscriber()
        
    def run(self):
        self.subscribe.run("temp")

if __name__ == '__main__':
    app = DeviceSubscriberApp()
    app.run()