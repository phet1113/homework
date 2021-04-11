# -*-  coding = utf-8 -*-
# @Time : 2021/3/28 9:54 下午
# @author : Wang Zhixian
# @File : assemble.py
# @Software: PyCharm
from bs4 import BeautifulSoup
import re
import urllib
import urllib.request
import ssl
from flask import Flask, render_template
from pachong import *

if __name__ == '__main__':
    p = crawler().creatNet()
    p.run(debug=True)