# -*- coding: utf8 -*-
import json
import requests
import time
import os



class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def pushplus(content):
    # 在网站中查询你的你的token
    token = os.environ.get('token')  # 在pushpush网站中可以找到
    title = '健康打卡'  # 改成你要的标题内容
    content = content  # 改成你要的正文内容
    url = 'http://www.pushplus.plus/send'
    data = {
        "token": token,
        "title": title,
        "content": content
    }

    body = json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type': 'application/json'}
    requests.post(url, data=body, headers=headers)

def report(user):
    data = {
        'username': user.username,
        'password': user.password,
    }
    url = "https://app.buaa.edu.cn/uc/wap/login/check"
    url_info = "https://app.buaa.edu.cn/buaaxsncov/wap/default/get-info"
    url_save = "https://app.buaa.edu.cn/buaaxsncov/wap/default/save"
    session = requests.Session()
    re = session.post(url=url, data=data)
    start = time.time()
    while "操作成功" not in re.content.decode():
        time.sleep(2)
        re = session.post(url=url, data=data)
        end = time.time()
        if (end - start) > 600:
            pushplus("打卡失败，请手动进行打卡")
            print("打卡失败，请手动进行打卡")
            return 0
    re = session.get(url=url_info)
    info = json.loads(re.text)['d']['info']
    info.update({'is_move': 0})
    info['area'] = "北京市 海淀区"
    info['city'] = "北京市"
    info['province'] = "北京市"
    info['address'] = "北京市海淀区花园路街道北京航空航天大学北京航空航天大学学院路校区"
    info['geo_api_info'] = "{\"type\":\"complete\",\"info\":\"SUCCESS\",\"status\":1,\"$Da\":\"jsonp_775059_\"," \
                           "\"position\":{\"Q\":39.98212,\"R\":116.34557000000001,\"lng\":116.34557," \
                           "\"lat\":39.98212},\"message\":\"Get ipLocation success.Get address success.\"," \
                           "\"location_type\":\"ip\",\"accuracy\":null,\"isConverted\":true,\"addressComponent\":{" \
                           "\"citycode\":\"010\",\"adcode\":\"110108\",\"businessAreas\":[{\"name\":\"五道口\"," \
                           "\"id\":\"110108\",\"location\":{\"Q\":39.99118,\"R\":116.34157800000003," \
                           "\"lng\":116.341578,\"lat\":39.99118}},{\"name\":\"大钟寺村\",\"id\":\"110108\",\"location\":{" \
                           "\"Q\":39.965569,\"R\":116.339877,\"lng\":116.339877,\"lat\":39.965569}}]," \
                           "\"neighborhoodType\":\"生活服务;生活服务场所;生活服务场所\",\"neighborhood\":\"北京航空航天大学\"," \
                           "\"building\":\"\",\"buildingType\":\"\",\"street\":\"学院路\",\"streetNumber\":\"37-6号\"," \
                           "\"country\":\"中国\",\"province\":\"北京市\",\"city\":\"\",\"district\":\"海淀区\"," \
                           "\"township\":\"花园路街道\"},\"formattedAddress\":\"北京市海淀区花园路街道北京航空航天大学北京航空航天大学学院路校区\"," \
                           "\"roads\":[],\"crosses\":[],\"pois\":[]} "
    re = session.post(url=url_save, data=info)
    start = time.time()
    while "操作成功" not in re.content.decode() and "今天已经填报了" not in re.content.decode():
        time.sleep(2)
        re = session.post(url=url_save, data=info)
        end = time.time()
        if (end - start) > 600:
            pushplus("打卡失败，请手动进行打卡")
            print("打卡失败，请手动进行打卡")
            return 0

    pushplus("恭喜你打卡成功！")
    print("恭喜你打卡成功！")

# 你的账号
name="15111122"
# 你的密码
key="15111122key"
user = User(name, key)
report(user)