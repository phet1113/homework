# -*-  coding = utf-8 -*-
# @Time : 2021/3/30 7:32 下午
# @author : Wang Zhixian
# @File : app.py
# @Software: PyCharm

from flask import Flask, render_template
import requests
from main import api

# application
if __name__ == '__main__':
    p = api()
    p.createnet().run(debug=True)
    #response = requests.get("https://api.seniverse.com/v3/weather/now.json?key=SWGh1J31G2h8U4gfO&location=beijing&language=zh-Hans&unit=c")
    #data = response.json()
    #print(data)
    #print(p.getdata("https://api.seniverse.com/v3/weather/now.json?key=SWGh1J31G2h8U4gfO&location=beijing&language=zh-Hans&unit=c"))