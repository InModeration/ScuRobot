import logging
from enum import Enum


class AppLog:
    level = Enum('level',
                 {'debug':logging.DEBUG,
                  'info':logging.INFO,
                  'warning':logging.WARNING,
                  'error':logging.ERROR,
                  'critical':logging.CRITICAL})
    logger = None
    lvl = None

    def __init__(self, name):

        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        self.setLogHandle()

    def setLogHandle(self):
        fhandler = logging.FileHandler('log.txt','a','utf-8')
        formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

        fhandler.setFormatter(formatter)
        fhandler.setLevel(logging.INFO)

        console = logging.StreamHandler()
        console.setFormatter(formatter)
        console.setLevel(logging.INFO)

        self.logger.addHandler(fhandler)
        self.logger.addHandler(console)

    def __getattr__(self,name):
        if(name in ('debug','info','warn','error','critical')):
            self.lvl = self.level[name].value
            return self
        else:
            raise AttributeError('Attr not Correct')

    def __call__(self, msg):
        self.logger.log(self.lvl, msg)

if __name__ == '__main__':
    mylog = AppLog("test")
    mylog.info('xxx fail')