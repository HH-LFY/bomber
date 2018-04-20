#-*- coding:utf-8 -*-
import json
import time
import os
import random
import threading
import logging
import logging.handlers

import hashlib
import requests
from bs4 import BeautifulSoup

from util import os_func
from util import util_func

class CommonBomber(object):
    """bomber基类"""
    def __init__(self):
        super(CommonBomber, self).__init__()
        self.name = self.__class__.__name__.replace('Bomber','')

    def send_sms_verify_code(self,phone):
        pass

if __name__ == '__main__':
    pass
