#-*- coding:utf-8 -*-

import json
import requests

from common_bomber import CommonBomber

class XiaohezaixianBomber(CommonBomber):

    def __init__(self):
        super(XiaohezaixianBomber, self).__init__()
        self.name = self.__class__.__name__.replace('Bomber','')

    # author:songpeng.huang
    # 2018年04月20日18:01:52
    # 小荷在线短信验证接口
    # 同一个手机号，1分钟内之内只能发一次
    def send_sms_verify_code(self,phone):
        url = "https://www.xiaohe666.com/app_identify"

        payload = "json_get=1&telephone=%s&type=10" % (phone,)
        headers = {
            'pragma': "no-cache",
            'origin': "https://www.xiaohe666.com",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
            'user-agent': "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36",
            'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
            'accept': "application/json, text/javascript, */*; q=0.01",
            'cache-control': "no-cache",
            'x-requested-with': "XMLHttpRequest",
            'cookie': "JSESSIONID=91CD922BABDB493AE55ED8DC62B75C43",
            'connection': "keep-alive",
            'referer': "https://www.xiaohe666.com/new_p2p_web/xhRegister.html?Ton=1",
            }

        response = requests.request("POST", url, data=payload, headers=headers)

        json_text = json.loads(response.text)
        if json_text['message'] == u'成功':
            print self.name,"send_sms_verify_code success."
            return True
        else:
            return False

if __name__ == '__main__':
    bomber = XiaohezaixianBomber()
    print bomber.send_sms_verify_code("13197916576")