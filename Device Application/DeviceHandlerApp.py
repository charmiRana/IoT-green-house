'''
Created on 16-Apr-2020

@author: Ranac
'''
from labs.module10.Publisher import publisher
from time import sleep
class DeviceHandlerApp():
    
    def __init__(self):
        self.publish = publisher()
    
    '''call publish from publisher app'''    
    def run(self):
        self.publish.publish()
        sleep(10)


if __name__ == '__main__':
    app = DeviceHandlerApp()
    app.run()