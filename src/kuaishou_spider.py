#-*- coding:utf-8 -*-
import json
import time
import os
import random
import threading

import requests
from bs4 import BeautifulSoup

from util.daemon import run_daemon

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)

def sleep_random():
    time.sleep(random.randint(7,11))

class KuaishouSpider(object):
    """docstring for kuaishouSpider"""
    def __init__(self):
        super(KuaishouSpider, self).__init__()
        self.headers = {
            "pragma": "no-cache",
            "cache-control": "no-cache",
            "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"
        }
        self.cookies = {
        }

    def search_user_video(self,user_id):
        user_id = str(user_id)
        one_url = "http://zhangye.s.gifshow.com/user/%s?fid=915959481&timestamp=%s" % (user_id,str(int(time.time()*1000)))
        # print one_url
        resp = requests.request("GET",one_url,headers=self.headers,cookies=self.cookies)
        # print resp.text
        soup = BeautifulSoup(resp.text,"lxml")
        base_url2 = "http://www.kuaishou.com"
        sleep_random()
        for row in soup.find_all("a",logj=True):
            # print type(row),row['href']
            next_page = row['href']
            next_url = base_url2+next_page
            # print next_url
            r = requests.request("GET",next_url,headers=self.headers,cookies=self.cookies)
            r_soup = BeautifulSoup(r.text,"lxml")
            video_dom = r_soup.find_all("video")
            # print video_dom
            if len(video_dom) == 0:
                print r_soup.text
            for r_row in video_dom:
                video_url = r_row["src"]
                sleep_random()
                self.save_video(user_id,video_url)
            sleep_random()

    def save_video(self,user_id,url):
        file_name = url.split("/")[-1]
        file_dir = "videos/"
        mkdir(file_dir+str(user_id))
        save_path = file_dir + str(user_id) + "/" +file_name
        rep = requests.request("GET",url,headers=self.headers,cookies=self.cookies)
        with open(save_path,"wb") as fw:
            fw.write(rep.content)


if __name__ == '__main__':
    #run_daemon()
    print "--------"
    spider = KuaishouSpider()
    origin_user = 300000101
    old_data = "already_check_user_kuaishou"
    with open(old_data,"r") as fr:
        rows = fr.readlines()
        if len(rows):
            origin_user = int(rows[-1].replace("\n",""))
            print "get origin_user:",str(origin_user)

    fw = open(old_data,"a+")
    for i in xrange(70000):
        sleep_random()
        start_user = str(origin_user + i)
        print "check:",start_user
        fw.write("%s\n" % start_user)
	try:
            spider.search_user_video(start_user)
	except:
	    print "is error"


