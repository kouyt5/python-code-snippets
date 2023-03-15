from typing import Union
import functools
import random
import time
import random
from log import get_logger

logger = get_logger()


def sleep_func(sleep_time: Union[float, str] = 0.1):
    """
    Params:
        sleep_time: 睡眠时间或者随机rand
        
    接口请求休息一定时间
    """
    if isinstance(sleep_time, float):

        def decorator(func):

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                if isinstance(sleep_time, float):
                    func(*args, **kwargs)
                    logger.info(f"interface sleep time: {format(sleep_time, '.1f')}s")
                    time.sleep(sleep_time)

            return wrapper

        return decorator
    else:

        def decorator(func):

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                func(*args, **kwargs)
                sleep_time = 0.1 + random.random() * 0.3
                logger.info(f"interface sleep time: {format(sleep_time, '.1f')}s")
                time.sleep(sleep_time)

            return wrapper

        return decorator

def catch_except(sleep_time:float=0):
    """
    抓取异常
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                logger.debug(e.args, exc_info=False)
                # logger.warn(f"发现异常, 休眠 {sleep_time} s")
                time.sleep(sleep_time)
        return wrapper
    return decorator