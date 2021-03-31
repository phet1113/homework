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
    dic = {}
    def getname(self,cate,dic):
        name = []
        for item in cate:
            name.append(dic[item])
        return(name)

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
            number = []
            # count the number of cities
            for item in self.cate:
                number.append(len(self.cities[item]))
            # give the name of province
            name = self.getname(self.cate, self.dic)
            return render_template("index.html", name=name, number=number)

        @app.route('/index')
        def home():
            number = []
            # count the number of cities
            for item in self.cate:
                number.append(len(self.cities[item]))
            # give the name of province
            name = self.getname(self.cate, self.dic)
            return render_template("index.html", name=name, number=number)

        # make Pagination
        @app.route('/zhixia')
        def zhixia():
            datalist = []
            name = self.getname(self.cate, self.dic)
            # input data
            for item in self.cities[self.cate[0]]:
                data = self.getdata(request_url="https://api.seniverse.com/v3/weather/now.json?key=SWGh1J31G2h8U4gfO&location="+item+"&language=zh-Hans&unit=c")
                datalist.append(data)
            return render_template("zhixia.html", data=datalist, name=name)

        @app.route('/guangdong')
        def guangdong():
            datalist = []
            name = self.getname(self.cate, self.dic)
            for item in self.cities[self.cate[1]]:
                data = self.getdata(request_url="https://api.seniverse.com/v3/weather/now.json?key=SWGh1J31G2h8U4gfO&location=" + item + "&language=zh-Hans&unit=c")
                datalist.append(data)
            return render_template("guangdong.html", data=datalist, name=name)

        @app.route('/jiangsu')
        def jiangsu():
            datalist = []
            name = self.getname(self.cate, self.dic)
            for item in self.cities[self.cate[2]]:
                data = self.getdata(request_url="https://api.seniverse.com/v3/weather/now.json?key=SWGh1J31G2h8U4gfO&location=" + item + "&language=zh-Hans&unit=c")
                datalist.append(data)
            return render_template("jiangsu.html", data=datalist, name=name)

        @app.route('/zhejiang')
        def zhejiang():
            datalist = []
            name = self.getname(self.cate, self.dic)
            for item in self.cities[self.cate[3]]:
                data = self.getdata(request_url="https://api.seniverse.com/v3/weather/now.json?key=SWGh1J31G2h8U4gfO&location=" + item + "&language=zh-Hans&unit=c")
                datalist.append(data)
            return render_template("zhejiang.html", data=datalist, name=name)

        return app

if __name__ == '__main__':
    p = api()
    # input the cities that we want
    p.cities = {"zhixia": ["beijing", "shanghai", "chongqing", "tianjin", "hong Kong"],
              "guangdong": ["guangzhou", "shenzhen", "shaoguan", "zhuhai", "foshan", "shantou", "jiangmen", "zhanjiang"],
              "jiangsu": ["nanjing", "xuzhou", "changzhou", "suzhou", "nantong", "huaian"],
              "zhejiang": ["hangzhou", "ningbo", "wenzhou", "jiaxing", "shaoxing", "jinhua"]
              }
    # change the dict
    p.cate = list(p.cities.keys())
    p.dic = {"guangdong": "广东省", "jiangsu": "江苏省", "zhejiang": "浙江省", "zhixia": "直辖市（含香港特别行政区)", "henan": "河南省"}
    p.createnet().run(debug=True)
