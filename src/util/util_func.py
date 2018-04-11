# -*- coding: utf-8 -*-
import builtwith
import urllib2
import requests
import lxml.html
from bs4 import BeautifulSoup

# 获取url的 服务器 信息
def get_url_bulitwith_info(url):
    return builtwith.parse(url)

def get_url_data_by_urllib2(url):
    return urllib2.urlopen(url).read()

def main():
    url = 'http://couplee.wang/'
    print get_url_bulitwith_info(url)
    # print get_url_data_by_urllib2(url)
    # print requests.get(url,verify=True).json()

if __name__ == '__main__':
    main()