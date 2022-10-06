import random


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