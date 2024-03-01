import logging
import sys


class LogGen:
    static_logger = None

    @staticmethod
    def loggen():
        logger = logging.getLogger(__name__)
        filehandler = logging.FileHandler(filename=sys.path[0]+"\\Logs\\logfile.log", mode='w')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        LogGen.static_logger = logger

