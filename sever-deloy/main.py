import json
import requests
import time
import schedule
from tomato import *
if __name__ == '__main__':
    ############ 你的账号 ############
    name = "****"
    ############ 你的密码 ############
    key = "****"
    ############ 你的token指令 ############
    token = '****'

    # 打卡函数
    user = User(name, key, token)
    schedule.every().day.at("17:01").do(report, user)
    # schedule.every().minutes.do(report, user)
    while (1):
        schedule.run_pending()
