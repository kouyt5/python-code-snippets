import requests
from mock_data import gen_data
from time import sleep
from proxy_utils import get_proxy
from log import logger
from connect_utils import sleep_func, catch_except


def main():
    URL = "https://ckde.lol/api/addMeil.php"
    for i in range(1000 * 1000):
        hack_once(URL)

@sleep_func(0.1)
@catch_except(10)
def hack_once(URL):
        data = {"username": gen_data()["email"],
                "password": gen_data()["password"]}
        proxy = {}
        proxy["http"] = "http://"+get_proxy()["proxy"]
        res = requests.post(URL, data=data, proxies=proxy)
        logger.info(f"注入信息: {data}")
        logger.info(res.text.strip())
        
if __name__ == "__main__":
    main()