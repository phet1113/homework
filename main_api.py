# -*-  coding = utf-8 -*-
# @Time : 2021/3/30 7:32 下午
# @author : Wang Zhixian
# @File : app.py
# @Software: PyCharm

from flask import Flask, render_template
import requests
from api import api

# application
if __name__ == '__main__':
    p = api()
    p.cities = {"municipality": ["beijing", "shanghai", "chongqing", "tianjin", "hong Kong"],
                "guangdong": ["guangzhou", "shenzhen", "shaoguan", "zhuhai", "foshan", "shantou", "jiangmen",
                              "zhanjiang"],
                "jiangsu": ["nanjing", "xuzhou", "changzhou", "suzhou", "nantong", "huaian"],
                "zhejiang": ["hangzhou", "ningbo", "wenzhou", "jiaxing", "shaoxing", "jinhua"]
                }
    p.cate = list(p.cities.keys())
    p.dic = {"guangdong": "广东省", "jiangsu": "江苏省", "zhejiang": "浙江省", "municipality": "直辖市（含香港特别行政区)", "henan": "河南省"}
    p.createnet().run(debug=True)
