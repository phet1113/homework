# -*-  coding = utf-8 -*-
# @Time : 2021/3/30 8:39 上午
# @author : Wang Zhixian
# @File : main.py
# @Software: PyCharm

from flask import Flask, render_template
import requests
# define the class
class api(object):
    cities = {}
    cate = []
    def getdata(self, request_url):
        # ask the api to get data
        datalist =[]
        response = requests.get(request_url)
        data = response.json()
        datalist.append(data["results"][0]["location"]["name"])
        datalist.append(data["results"][0]["now"]["text"])
        # change the code into the picture address
        datalist.append("https://s1.sencdn.com/web/icons/black/"+data["results"][0]["now"]["code"]+"@1x.png")
        datalist.append(data["results"][0]["now"]["temperature"])
        datalist.append(data["results"][0]["now"]["feels_like"])
        datalist.append(data["results"][0]["now"]["pressure"])
        datalist.append(data["results"][0]["now"]["humidity"])
        datalist.append(data["results"][0]["now"]["visibility"])
        datalist.append(data["results"][0]["now"]["wind_direction"])
        datalist.append(data["results"][0]["now"]["wind_speed"])
        datalist.append(data["results"][0]["now"]["wind_scale"])
        datalist.append(data["results"][0]["last_update"])
        return datalist

    def createnet(self):
        app = Flask(__name__)

        # create the first page
        @app.route('/')
        def index():
            return render_template("index.html")

        @app.route('/index')
        def home():
            return render_template("index.html")

        # make Pagination
        @app.route('/zhixia')
        def zhixia():
            datalist = []
            for item in self.cities[self.cate[0]]:
                data = self.getdata(request_url="https://api.seniverse.com/v3/weather/now.json?key=SWGh1J31G2h8U4gfO&location="+item+"&language=zh-Hans&unit=c")
                datalist.append(data)
            return render_template("zhixia.html", data=datalist)

        @app.route('/guangdong')
        def guangdong():
            datalist = []
            for item in self.cities[self.cate[1]]:
                data = self.getdata(request_url="https://api.seniverse.com/v3/weather/now.json?key=SWGh1J31G2h8U4gfO&location=" + item + "&language=zh-Hans&unit=c")
                datalist.append(data)
            return render_template("guangdong.html", data=datalist)

        @app.route('/jiangsu')
        def jiangsu():
            datalist = []
            for item in self.cities[self.cate[2]]:
                data = self.getdata(request_url="https://api.seniverse.com/v3/weather/now.json?key=SWGh1J31G2h8U4gfO&location=" + item + "&language=zh-Hans&unit=c")
                datalist.append(data)
            return render_template("jiangsu.html", data=datalist)

        @app.route('/zhejiang')
        def zhejiang():
            datalist = []
            for item in self.cities[self.cate[3]]:
                data = self.getdata(request_url="https://api.seniverse.com/v3/weather/now.json?key=SWGh1J31G2h8U4gfO&location=" + item + "&language=zh-Hans&unit=c")
                datalist.append(data)
            return render_template("zhejiang.html", data=datalist)

        return app

if __name__ == '__main__':
    p = api()
    p.cities = {"zhixia": ["beijing", "shanghai", "chongqing", "tianjin", "hong Kong"],
              "guangdong": ["guangzhou", "shenzhen", "shaoguan", "zhuhai", "foshan", "shantou", "jiangmen", "zhanjiang"],
              "jiangsu": ["nanjing", "xuzhou", "changzhou", "suzhou", "nantong", "huaian"],
              "zhejiang": ["hangzhou", "ningbo", "wenzhou", "jiaxing", "shaoxing", "jinhua"]
              }
    p.cate = list(p.cities.keys())
    print(type(p.cate[1]))
    p.createnet().run(debug=True)