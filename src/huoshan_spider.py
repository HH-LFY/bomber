#-*- coding:utf-8 -*-
import json
import threading
import time
import os
import random
import logging

import requests
from bs4 import BeautifulSoup

from common_spider import CommonSpider


class HuoshanSpider(CommonSpider):
    '''
    火山小视频爬虫，根据uid爬取
    https://reflow.huoshan.com/share/load_videos/?offset=0&count=21&user_id=68532174477&max_time=
    '''

    def __init__(self):
        super(HuoshanSpider,self).__init__()
        self.spider_name = 'huoshan'

    def search_user_video(self,user_id):
        max_time = ''
        while True:
            logging.info("-"*50)
            base_url = "https://reflow.huoshan.com/share/load_videos/?count=21&user_id=%s&max_time=%s" % ( user_id, max_time)
            logging.info(base_url)
            resp = requests.request("GET",base_url,headers=self.headers,cookies=self.cookies)
            json_data = json.loads(resp.text)
            items = json_data.get('data',{}).get('items',[])
            if json_data.get('extra',{}).get('has_more',False) == False:
                break
            max_time = json_data.get('extra',{}).get('max_time','')
            for item in items:
                self.sleep_random()
                url_list = item.get('video',{}).get('url_list',[])
                for video_url in url_list:
                    logging.info(video_url)
                    self.save_video(video_url)
                    break

def main():
    huoshan = HuoshanSpider()
    huoshan.search_user_video("89833721835")

if __name__ == '__main__':
    main()