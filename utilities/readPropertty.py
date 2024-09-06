import configparser
import os

config = configparser.RawConfigParser()
config.read(filenames=os.curdir+"/configuration/config.ini")

print(os.curdir+"/configuration/config.ini")
def ReadConfig():

    @staticmethod
    def getApplication_url():
        url = config.get('commonInfo', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        user = config.get('commonInfo', 'email')
        return user

    @staticmethod
    def getPasswd():
        passwd = config.get('commonInfo', 'passwd')
