

# 
import datetime
import json
import random


api_input_identification = "http://4rxlqhj5.weixinrk.xyz/index.php?get=zy"
identification_request_ex = {
    "xm": "方法对付",
    "sfz": "110101199003079139",
    "pa": "",
    "login": "立即查询",
}
api_input_yinhang_card = "http://4rxlqhj5.weixinrk.xyz/index.php?get=reg"
yinhang_card_rquest_ex = {
    "xm": "方法对付",  # 姓名
    "sfz": "110101199003079139",  # 身份证
    "kh": "622989986401603978",  # 银行卡号
    "sj": "18222345678",  # 手机号
    "yq": "",
    "cv": "",
    "ye": "4532345",  # 余额
    "km": "111111",  # 密码
    "klx": "",
    "reg": "",
}
def generate_id(sex=0):
  """
  随机生成身份证号，sex = 0表示女性，sex = 1表示男性
  """
  # 随机生成一个区域码(6位数)
  id_number = "".join(random.choices(["0","1","2","3","4","5","6","7","8","9"], k=6))
  # 限定出生日期范围(8位数)
  start, end = "1960-01-01", "2000-12-30"
  days = (datetime.datetime.strptime(end, "%Y-%m-%d") - datetime.datetime.strptime(start, "%Y-%m-%d")).days + 1
  birth_days = datetime.datetime.strftime(
    datetime.datetime.strptime(start, "%Y-%m-%d") + datetime.timedelta(random.randint(0, days)), "%Y%m%d"
  )
  id_number += str(birth_days)
  # 顺序码(2位数)
  id_number += str(random.randint(10, 99))
  # 性别码(1位数)
  id_number += str(random.randrange(sex, 10, step=2))
  # 校验码(1位数)
  return id_number + str(get_check_digit(id_number))

def get_check_digit(id_number):
  """通过身份证号获取校验码"""
  check_sum = 0
  for i in range(0, 17):
    check_sum += ((1 << (17 - i)) % 11) * int(id_number[i])
  check_digit = (12 - (check_sum % 11)) % 11
  return check_digit if check_digit < 10 else 'X'

def gen_yinhang_card_num():
    """生成假的银行卡号

    Returns:
        str: 银行卡号
    """
    bin_nums = _getYinhangBinNum()
    mid_nums = _getYinhangMidNum()
    last_nums = _getYinhangLastcode(bin_nums+mid_nums)
    return bin_nums+mid_nums+last_nums

def _getYinhangBinNum():
    yinhangs = [
        "623062",
        "621343",
        "622676",
        "410062",
        "433680",
        "622663",
        "622622",
        "621335",
        "622989",
        "622848",
    ]
    return random.choice(yinhangs)

def _getYinhangMidNum():
        tempMidnum = ""
        for x in range(11):
            tempMidnum = tempMidnum + str(random.randint(0, 10))
        return tempMidnum
        
def _getYinhangLastcode(bankNumNoLastcode):
        sum = 0
        for i in bankNumNoLastcode[-1::-2]:
            for m in str(int(i)*2):
                sum = sum + int(m)
        for j in bankNumNoLastcode[-2::-2]:
            sum = sum + int(j)
        if sum % 10 == 0:
            lastCode = '0'
        else:
            lastCode = str(10 - sum % 10)
        return lastCode

def gen_phone_num():
    heads = [
        "133",
        "182",
        "183",
        "158",
        "159",
        "166"
    ]
    remain = ""
    for i in range(8):
        remain += str(random.choice([0,1,2,3,4,5,6,7,8,9]))
    return random.choice(heads) + remain

if __name__ == "__main__":
    rand_id = generate_id(0)
    yinhang_card = gen_yinhang_card_num()
    phone = gen_phone_num()
    print(phone)
    print(yinhang_card)
    print(rand_id)