#-*- coding:utf-8 -*-
import json
import time
import os
import random
import requests
import threading

class PinancaifubaoSpider(object):
    """docstring for PinancaifubaoSpider"""
    def __init__(self):
        super(PinancaifubaoSpider, self).__init__()

    # author:songpeng.huang
    # 2018年04月11日17:56:17
    # 平安财富短信验证接口
    # 同一个手机号，1分钟内之内只能发一次
    @classmethod
    def send_sms_verify_code(cls,phone):
        url = "https://cfb.pingan.com/ncfb/v3/nts_cfb_intf_mop.mopSmsSend"
        querystring = {"_":"1523435457993"}
        payload = {
            "_request_id":"D95EED74-8DB5-4879-BC76-54213FE17187",
            "_channel_id":"04",
            "encFlag":0,
            "_version_no":"3.1.0",
            "deviceId":"CFBH5|1E8F97E4-86CC-4508-8C39-9BD38981FF66",
            "activeId":"763xim",
            "mobile":"",
            "smsType":"11"
        }
        payload["mobile"] = str(phone)
        headers = {
            'deviceid': "CFBH5|1E8F97E4-86CC-4508-8C39-9BD38981FF66",
            'pragma': "no-cache",
            'origin': "https://cfb.pingan.com",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
            'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
            'content-type': "application/json; charset=UTF-8",
            'accept': "application/json",
            'cache-control': "no-cache",
            'x-requested-with': "XMLHttpRequest",
            'cookie': "WEBTRENDS_ID=4.0.4.33-1284388608.30658927; WT-FPC=id=4.0.4.33-1284388608.30658927:lv=1523435424421:ss=1523435408771:fs=1523435408771:pn=2:vn=1",
            'connection': "keep-alive",
            'referer': "https://cfb.pingan.com/m/campaigns/m2017-hqy-newHand.html?WT.mc_id=cfb-pingan-763xim-003",
            'postman-token': "ac0b07d8-13b4-8241-3a10-e542de5f4063"
            }
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers, params=querystring)
        print response.text
        json_text = json.loads(response.text)
        if json_text["responseMsg"] == u"成功":
            return True
        else:
            return False

if __name__ == '__main__':
    print PinancaifubaoSpider.send_sms_verify_code("")
