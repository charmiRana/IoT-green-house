'''
Created on 16-Apr-2020

@author: Ranac
'''
from labs.common.ConfigUtil import ConfigConst, ConfigUtil
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class SmtpClientConnector():
    
    def __init__(self):
        self.config =  ConfigUtil()
        
    def publishMessage(self, topic, data):
        
        self.config.loadConfig()
        ''' getting data from ConfigConst '''
        host = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.HOST_KEY)
        port = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.PORT_KEY)
        fromAddr = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.FROM_ADDRESS_KEY)
        toAddr = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.TO_ADDRESS_KEY)
        authToken = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.USER_AUTH_TOKEN_KEY)
        
        '''to give data in message'''
        msg = MIMEMultipart()
        msg['From'] = fromAddr
        msg['To'] = toAddr
        msg['subject'] = topic
        msgBody = str(data)
        msg.attach(MIMEText(msgBody))
        
        msgText = msg.as_string()
        
        '''send e-mail notification'''
        server = smtplib.SMTP_SSL(host, port) 
        server.ehlo()
        server.login(fromAddr, authToken)
        server.sendmail(fromAddr, toAddr, msgText)
        
        server.close()