import logging
from loggerpy import Logger, Level


class LogGenclass():
    @staticmethod
    def loggenmethod():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
            logging.basicConfig(filename=r'C:\Users\Achal Trivedi\PycharmProjects\pythonproject\Logs\automation.log', format='%(asctime)s %(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
            logger = logging.getLogger()
        # logger.setLevel(logging.INFO)
        return logger

#logging.basicConfig(filename='../Logs/automation.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
# logging.basicConfig(format='%(asctime)s %(message)s')
# logging.basicConfig(filename='automation.log', encoding='utf-8', level=logging.DEBUG)
# logging.basicConfig(filename='myapp.log', level=logging.INFO)
# logging.basicConfig(filename='automation.log', filemode='w', level=logging.DEBUG)
# logging.basicConfig(filename='automation.log',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
