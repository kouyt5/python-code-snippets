from collections import defaultdict
from typing import Union
import functools
import json
import random
import sys
import requests
import logging
from tqdm import tqdm
import time

from log import get_logger
from utils import delete_proxy, get_proxy, get_proxy_https

logger = get_logger()
API = "https://www.mailhho-cn.com/login"  # 141.164.43.216
LOC_API = "https://www.mail-mailsecure.com/api/comn/address/"


class VARS:
    count = 0
    timeout = 10.0
    proxy = {"https": ""}
    code = 200
    fail_proxy = defaultdict(int)
    all_provinces = []
    success_proxy = []


def cycle_connect(sleep_time=3.0):
    """
    Params:
        sleep_time: 睡眠时间
        
    异常重连

    Examples:
    >>> @cycle_connect(5)
    >>> def test():
    >>>     print("hello world)
    """

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            while (True):
                try:
                    func(*args, **kwargs)
                    args[2].fail_proxy[args[2].proxy['https']] = 0
                except requests.exceptions.ConnectionError as e:
                    logger.error(e.args, exc_info=True)
                    time.sleep(sleep_time)  # sleep_time秒后重新连接
                    logger.warning("尝试重新连接")
                    args[2].fail_proxy[args[2].proxy['https']] += 1
                    if args[2].fail_proxy[args[2].proxy[
                            'https']] > 5:
                        logger.warning(
                            f"delete a proxy : {args[2].proxy['https'].split('http://')[-1]}"
                        )
                        delete_proxy(
                            args[2].proxy['https'].split('http://')[-1])
                        args[2].fail_proxy[args[2].proxy['https']] = 1
                except KeyboardInterrupt as e:
                    logger.warning("程序被 Crtl+C 强制退出....")
                    sys.exit()
                except json.decoder.JSONDecodeError as e:
                    # 返回数据解析失败，接口可能没有权限
                    logger.error(e.args, exc_info=True)
                    args[2].fail_proxy[args[2].proxy['https']] += 1
                    if args[2].fail_proxy[args[2].proxy[
                            'https']] > 3 and not args[2].code == 200:
                        logger.warning(
                            f"delete a proxy : {args[2].proxy['https'].split('http://')[-1]}"
                        )
                        delete_proxy(
                            args[2].proxy['https'].split('http://')[-1])
                        args[2].fail_proxy[args[2].proxy['https']] = 1
                    
                except Exception as e:
                    args[2].fail_proxy[args[2].proxy['https']] += 1
                    if args[2].fail_proxy[args[2].proxy[
                            'https']] > 3 and not args[2].code == 200:
                        logger.warning(
                            f"delete a proxy : {args[2].proxy['https'].split('http://')[-1]}"
                        )
                        delete_proxy(
                            args[2].proxy['https'].split('http://')[-1])
                        args[2].fail_proxy[args[2].proxy['https']] = 1
                    logger.error(e.args, exc_info=True)
                    time.sleep(sleep_time)

        return wrapper

    return decorator


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
                    logger.info(f"interface sleep time: {sleep_time}")
                    time.sleep(sleep_time)

            return wrapper

        return decorator
    else:

        def decorator(func):

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                func(*args, **kwargs)
                sleep_time = 0.1 + random.random() * 0.3
                logger.info(f"interface sleep time: {sleep_time}")
                time.sleep(sleep_time)

            return wrapper

        return decorator


@cycle_connect(3)
@sleep_func("rand")
def do_request(api_pass: str, api_loc: str, vars: VARS):
    data = gen_data()
    header = {
        "user-agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Content-Type": "application/json;charset=utf-8",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language":
        "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Authorization": "MDowOjM=",
        "Content-Length": "82",
        "Origin": "https://www.mailhho-cn.com",
        "Connection": "keep-alive",
        "Referer": "https://www.mailhho-cn.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers",
    }
    http_proxy = get_proxy()
    https_proxy = get_proxy_https()
    proxys = {}
    if 'proxy' in http_proxy.keys():
        proxys["http"] = "http://" + http_proxy['proxy']
    else:
        proxys["http"] = ""
    if 'proxy' in https_proxy.keys():
        proxys["https"] = "http://" + https_proxy['proxy']
    else:
        logger.warning(f"https代理暂时不可用")
        if random.random() > 0.2 and len(vars.success_proxy)>0:
            proxys = random.choice(vars.success_proxy)
            logger.info(f"使用历史成功代理{proxys['https']}")
            
        else:
            proxys["https"] = proxys["http"]

    logger.info(f"proxy={proxys}")
    vars.proxy = proxys
    # proxy ip -> data
    if random.random() > 0.5:
        data["clientIp"] = proxys["https"].split("http://")[-1].split(":")[0]
    logger.info(f"伪造数据: {str(data)}")
    result = requests.post(api_pass,
                           json=data,
                           headers=header,
                           proxies=proxys,
                           timeout=vars.timeout,
                           allow_redirects=False)
    result.close()
    vars.code = result.status_code
    if not vars.code == 200:
        logger.warning(f"请求响应码异常: {vars.code}")
        logger.warning(f"响应内容: {result.text}")
        return
    result = json.loads(result.text)
    if (result['code'] == 1):
        logger.info(f"请求正常: {result['code']}, {result}")
        logger.info(f"进度: 已发送{vars.count}条.....")
        vars.count = vars.count + 1
        vars.success_proxy.append(proxys)
    else:
        logger.warning(f"请求异常: {result['code']}, {result}")

    # 位置
    # if (len(vars.all_provinces) ==0 or random.random()>0.9):
    #     result = requests.post(api_loc,
    #                         json={"parent_id": 0},
    #                         proxies=proxys,
    #                         timeout=vars.timeout)
    #     result = json.loads(result.text)
    #     vars.all_provinces = result['data']['info']

    # if random.random()> 0.9:
    #     province = random.choice(vars.all_provinces)  # 省份
    #     logger.info(f"选择省份信息: {province}")
    #     result = requests.post(api_loc,
    #                         json={"parent_id": province['id']},
    #                         proxies=proxys,
    #                         timeout=vars.timeout)
    #     if result.text == '':
    #         logger.warning(f"请求省份下市级数据接口使用id {loc_id} 没有返回数据")
    #     else:
    #         logger.info(f"请求省份下市级数据接口响应: {json.loads(result.text)}")

    #     loc_id = random.randint(50, 5000)  # 选择一个数据
    #     result = requests.post(api_loc,
    #                         json={"parent_id": loc_id},
    #                         proxies=proxys,
    #                         timeout=vars.timeout)
    #     logger.info(f"loc地址id: {loc_id},request状态码: {result.status_code}")
    # loc_id = random.randint(50, 5000)
    # result = requests.post(api_loc,
    #                        json={"parent_id": loc_id},
    #                        proxies=proxys,
    #                        timeout=vars.timeout)
    # logger.info(f"loc地址id: {loc_id},request状态码: {result.status_code}")


def gen_data():
    import random

    rand_source_num = "0123456789"
    rand_source_str = "qwertyuiopasdfghjklzxcvbnm"
    rand_mail_list = [
        "qq.com",
        "126.com",
        "sina.com",
        "163.com",
        "gmail.com",
        "yahoo.com",
        "rinima.com",
        "shabi.com",
        "sohu.com",
        "91porn.com",
        "hotmail.com",
        "std.ustc.edu.cn",
        "ustc.edu.cn",
        "uestc.edu.cn",
        "std.pk.edu.cn",
        "std.teq.edu.cn",
        "sjtu.edu.cn",
        "std.sjtu.edu.cn",
        "ruc.edu.cn",
        "std.ruc.edu.cn",
        "pku.edu.cn",
        "std.pku.edu.cn",
        "tsinghua.edu.cn",
        "std.tsinghua.edu.cn",
        "buct.edu.cn",
        "bupt.edu.cn",
        "bnu.edu.cn",
        "cuc.edu.cn",
        "uibe.edu.cn",
        "buaa.edu.cn",
        "bfsu.edu.cn",
        "ecust.edu.cn",
        "shisu.edu.cn",
        "shufe.edu.cn",
        "seu.edu.cn",
        "cug.edu.cn",
        "znufe.edu.cn",
        "scu.edu.cn",
        "std.scu.edu.cn",
        "xjtu.edu.cn",
        "xjtu.edu.cn",
        "snnu.edu.cn",
        "nwpu.edu.cn",
        "sdu.edu.cn",
        "scut.edu.cn",
        "swu.edu.cn",
        "lzu.edu.cn",
        "dlut.edu.cn",
        "ujs.edu.cn",
        "hhu.edu.cn",
        "dhu.edu.cn",
        "bjfu.edu.cn",
    ]
    rand_password_list = [
        "123456",
        "123456789",
        "qwerty",
        "111111",
        "password",
        "admin",
        "123123",
        "qwertyuiop",
        "19960101",
        "7777777",
        "123321",
        "1q2w3e4r",
        "654321",
        "google",
        "1q2w3e",
        "qwert123",
        "000000",
        "1234567",
    ]
    # usename
    usename = ""
    username_len = random.randint(8, 11)
    if random.random() > 0.6:
        for i in range(username_len):
            usename += random.choice(list(rand_source_num + rand_source_str))
    else:
        for i in range(username_len):
            usename += random.choice(list(rand_source_num))
    # 邮箱名
    mail_name = ""
    if random.random() > 0.6:
        edu_mail_len = random.randint(3, 5)
        mail_name = ''.join(
            random.choices(list(rand_source_str), k=edu_mail_len)) + '.edu.cn'
        usename += "@" + mail_name
    else:
        usename += "@" + random.choice(rand_mail_list)

    # password
    password = ""
    password_len = random.randint(6, 10)
    if random.random() > 0.5:
        for i in range(password_len):
            password += random.choice(list(rand_source_num + rand_source_str))
    else:
        password = random.choice(rand_password_list)
    # ip
    ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
    return {
        "email": usename,
        "password": password
    }
    # return {
    #     "username": usename,
    #     "password": password,
    #     "clientIp": ip,
    # }


def main():
    do_request(API, LOC_API, VARS())


if __name__ == "__main__":
    main()
