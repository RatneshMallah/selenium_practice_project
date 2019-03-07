__author__ = 'Ratnesh Mallah'

import inspect
import logging

def customLogger(logLevel):
    #get the name of class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    print(loggerName)
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    #add console handaler
    # chandle = logging.StreamHandler()
    # chandle.setLevel(logLevel)

    # add file handaler
    fhandle = logging.FileHandler("automation.log",mode="a")
    fhandle.setLevel(logLevel)

    format = '%(asctime)s - %(name)s - %(levelname)s : %(message)s'
    formatter = logging.Formatter(format,datefmt='%m/%d/%Y %I:%M:%S %p')

    #add formatter  handelers
   # chandle.setFormatter(formatter)
    fhandle.setFormatter(formatter)

    #logger.addHandler(chandle)
    logger.addHandler(fhandle)

    return logger
