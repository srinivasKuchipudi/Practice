import logging

FORMAT = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'

def logger():
    logging.basicConfig(format=FORMAT,
                    level=logging.INFO,
                    handlers=[logging.FileHandler("TestLogs.log"),
                              logging.StreamHandler()])
    return logging