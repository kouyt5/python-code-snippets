import requests


def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()

def get_proxy_https():
    return requests.get("http://127.0.0.1:5010/get/?type=https").json()

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))
    
def get_count():
    return requests.get("http://127.0.0.1:5010/count/").json()['count']

if __name__ == "__main__":
    # result = get_count()
    # result = get_proxy_https()
    origin_result = requests.get("https://www.mail-mailsecure.com/")
    # http_result = requests.get("https://www.mail-mailsecure.com/", proxies={"https":"http://"+get_proxy()['proxy']})
    result = requests.get("https://www.mail-mailsecure.com/", proxies={"https":"http://"+get_proxy_https()['proxy']})
    pass