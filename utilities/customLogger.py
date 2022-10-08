import logging


class LogGenclass():
    @staticmethod
    def loggenmethod():      #call 'loggenmethod' method from 'LoGgenClass' class- return logger object
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
            logging.basicConfig(filename=r'C:\Users\achal\PycharmProjects\pythonproject\Logs\automation.log', format='%(asctime)s %(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
            logger = logging.getLogger()
        return logger

#logging.basicConfig(filename='../Logs/automation.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

# logging.basicConfig(filename='automation.log', encoding='utf-8', level=logging.DEBUG)
#logger.setLevel(logging.INFO) //-if not mentioned in basicconfig write by setlevel()
