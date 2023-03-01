import logging
import logging.handlers
import os


def init_logger(name):
    logger = logging.getLogger(name)
    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(FORMAT))
    sh.setLevel(logging.DEBUG)
    if not os.path.exists('logs'):
        os.makedirs('logs')
    fh = logging.FileHandler(filename=f'logs/{name}')
    fh.setFormatter(logging.Formatter(FORMAT))
    fh.setLevel(logging.INFO)
    logger.addHandler(sh)
    logger.addHandler(fh)
    logger.debug(f'logger inited')
    return logger     
