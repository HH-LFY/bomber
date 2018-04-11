#-*- coding:utf-8 -*-
import json
import time
import os

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)