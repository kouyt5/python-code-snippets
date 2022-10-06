import requests
from mock_data import gen_data
from time import sleep
from proxy_utils import get_proxy
from log import logger


def main():
    URL = "https://ckde.lol/api/addMeil.php"
    for i in range(1000 * 100):
        data = {"username": gen_data()["email"],
                "password": gen_data()["password"]}
        proxy = {}
        proxy["http"] = "http://"+get_proxy()["proxy"]
        res = requests.post(URL, data=data, proxies=proxy)
        logger.info(f"注入信息: {data}")
        logger.info(res.text.strip())
        sleep(1)
if __name__ == "__main__":
    main()