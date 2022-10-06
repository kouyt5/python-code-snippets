import logging
import logging.handlers
import random


def get_logger():
    formatter = logging.Formatter(
    "[%(asctime)s] - [%(threadName)s %(filename)s :%(lineno)d] - %(levelname)s: %(message)s"
    )
    logger = logging.getLogger("main")
    logger.setLevel(logging.DEBUG)
    console_handle = logging.StreamHandler()
    console_handle.setFormatter(formatter)
    file_handle = logging.FileHandler("log/log.log")
    tar_handle = logging.handlers.RotatingFileHandler(
                        "log/file_rotate.log", mode='a',
                        maxBytes=1024*1024*5, backupCount=10,
                        encoding='utf-8')
    
    folder = ''.join(random.choices(list("0123456789"), k=2))
    time_tar_handle = logging.handlers.TimedRotatingFileHandler(
            f"log/time/{folder}-time.log", "H", interval=1, backupCount=0, encoding='utf-8')
    time_tar_handle.setFormatter(formatter)
    tar_handle.setFormatter(formatter)
    file_handle.setFormatter(formatter)
    logger.addHandler(file_handle)
    logger.addHandler(console_handle)
    logger.addHandler(tar_handle)
    logger.addHandler(time_tar_handle)
    return logger