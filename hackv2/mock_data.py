import random
from webbrowser import get


def gen_data():
    rand_source_num = "0123456789"
    rand_source_str = "qwertyuiopasdfghjklzxcvbnm"
    rand_mail_list = [
        "std.ustc.edu.cn",
        "ustc.edu.cn",
        "uestc.edu.cn",
        "std.uestc.edu.cn",
        "std.uestc.edu.cn",
        "std.uestc.edu.cn",
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
        "cup.edu.cn",
        "std.cup.edu.cn",
        "ecust.edu.cn",
        "shisu.edu.cn",
        "shufe.edu.cn",
        "seu.edu.cn",
        "std.cugb.edu.cn",
        "cugb.edu.cn",
        "std.znufe.edu.cn",
        "scu.edu.cn",
        "std.scu.edu.cn",
        "snnu.edu.cn",
        "nwpu.edu.cn",
        "sdu.edu.cn",
        "scut.edu.cn",
        "std.swu.edu.cn",
        "lzu.edu.cn",
        "dlut.edu.cn",
        "ujs.edu.cn",
        "std.hhu.edu.cn",
        "std.aufe.edu.cn",
        "aufe.edu.cn",
        "scnu.edu.cn",  # 华南师范
        "std.scnu.edu.cn", 
        "fudan.edu.cn", # 复旦
        "std.fudan.edu.cn",
        "gxu.edu.cn",
        "std.gxu.edu.cn",  # 广西大学
        "csu.edu.cn",
        "std.csu.edu.cn",  # 中南大学
        "shnu.edu.cn",  # 
        "std.shnu.edu.cn",  # 上海大学
        "ynu.edu.cn",  # 
        "std.ynu.edu.cn",  # 云南大学
        "swu.edu.cn",  # 西南大学
        "std.swu.edu.cn",  # 
        "tju.edu.cn",  # 
        "std.tju.edu.cn",  # 天津大学
        "cqu.edu.cn",  # 
        "std.cqu.edu.cn",  # 重庆大学
        "hqu.edu.cn",  # 
        "std.hqu.edu.cn",  # 华侨大学
        "jlu.edu.cn",  # 
        "std.jlu.edu.cn",  # 吉林
        "hhu.edu.cn",  # 
        "std.hhu.edu.cn",  # 河海
        "fzu.edu.cn",  # 
        "std.fzu.edu.cn",  # 福州
        "nankai.edu.cn",  # 
        "std.nankai.edu.cn",  # 南开
        "suz.edu.cn",  # 
        "email.suz.edu.cn",  # 深圳
        "hust.edu.cn",  # 华中科技
        "bjkj.edu.cn",  # 北京科技大学
        "hnu.edu.cn",  # 湖南
        "hit.edu.cn",  #哈尔滨工业大学
        "tongji.edu.cn", # 同济大学
        "seu.edu.cn",  # 东南大学
        "sdu.edu.cn",  # 山东大学
        "nwpu.edu.cn",  # 西北工业大学
        "gdmc.edu.cn",  # 广东医学院

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
    usename += "@" + random.choice(rand_mail_list)

    # password
    password = ""
    password_len = random.randint(6, 10)
    if random.random() > 0.5:
        for i in range(password_len):
            password += random.choice(list(rand_source_num + rand_source_str))
    else:
        password = random.choice(rand_password_list)
    return {
        "email": usename,
        "password": password
    }
    
def gen_user_agent():
    agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
        "Opera/8.0 (Windows NT 5.1; U; en)",
        "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",

        "Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",

        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
         "MAC：Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
         "Windows：Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
         "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
         "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
         "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    ]
    
    get_one = random.choice(agent_list)
    get_one = list(get_one)
    get_one[int(random.randint(0, len(get_one))/2)] = str(random.randint(0, 9))
    get_one = ''.join(get_one)
    
    return get_one


if __name__ == "__main__":
    agent = gen_user_agent()
    print(agent)