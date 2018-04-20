#-*- coding:utf-8 -*-
import json
import time
import os
import random
import threading

import hashlib
import requests
from bs4 import BeautifulSoup

class DouyinSpider(object):
    """ 通过分享的个人主页来抓取
    https://www.douyin.com/share/user/66149367342/?share_type=link
    # 在链接中二次跳转
    https://www.douyin.com/aweme/v1/aweme/post/?user_id=66149367342&count=21&max_cursor=0&aid=1128&_signature=ZlAWvRATPIsSlm7gIEXZxmZQFq
    max_cursor为下一页起始位置,由上一个给出
    https://www.douyin.com/aweme/v1/aweme/post/?user_id=66149367342&count=21&max_cursor=1520925629000&aid=1128&_signature=1vnSRBASjDeiP6oZ4Nq1K9b50l

    _signature 字段为验签字段，有效时长大概为5分钟，该值的生成由node中的模块有关，待破解
    """
    def __init__(self, arg):
        super(DouyinSpider, self).__init__()
        self.arg = arg

if __name__ == '__main__':
    dy = DouyinSpider.__doc__
    print dy