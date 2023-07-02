import logging
#import logger

class logger:
    @staticmethod
    def setlogger():
        # logging.basicConfig(filename="C:\\Users\\admin\\PycharmProjects\\SeleniumWithPyTest\\logs\\testlogs.log",
        #                 format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m%d%Y %I:%M:%S %p',level=logging.INFO)

        logging.basicConfig(filename=".\\logs\\testlogs.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m%d%Y %I:%M:%S %p',
                            level=logging.INFO)
        logger=logging.getLogger()
        return logger
