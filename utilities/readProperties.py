import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+"\\configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('commonInfo', 'baseURL')
        return url
