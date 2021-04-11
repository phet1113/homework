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

class crawler(object):
    ssl._create_default_https_context = ssl._create_unverified_context

    baseurl = "http://www.zongheng.com/rank/details.html?rt=3&d=1&p="

    def askurl(self, url):
        head = {
            # change the User-Agent
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
            'Cookie': 'BAIDUID=ED02DEFE60A617EF43B8F0F72EDE4DE6:FG=1; BIDUPSID=ED02DEFE60A617EF43B8F0F72EDE4DE6; PSTM=1508720102;TIEBA_USERTYPE=e916512815a19960b624ed59; bdshare_firstime=1508724078966; FP_LASTTIME=1510621935104; TIEBAUID=151fb0a2f5bc99698d3e338b;rpln_guide=1; BDUSS=pBOFZsUG5PdFAxMnFtQU5DWEIxMDVOTWYyZWxyczB- fm10cjVPaElCQ0d2anRhQVFBQUFBJCQAAAAAAAAAAAEAAABPX00WwO7A1gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAIYxFFqGMRRaZk; STOKEN=180a7f530458725c97dfccdcbe99215e0ad64c49b8bc8e47d74a59bbbb9c0874; fixed_bar=1; wise_device=0;LONGID=374169423; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1512029668,1512050336,1512050702,1512089508;Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1512092098 ; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=2;H_PS_PSSID=1466_21092_18559_25178_22075; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598'

        }

        request = urllib.request.Request(url, headers=head)
        html = ""
        try:
            response = urllib.request.urlopen(request)
            html = response.read().decode("utf-8")
        # If there is an error, print it in html
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)

        return html

    def getdata(self):
        # defining regular expressions
        findLink = re.compile(r'href="(.*?)" target="_blank">')
        findtitle = re.compile(r'title="(.*?)">')
        findinfo = re.compile(r'<div class="rank_d_b_info">(.*?)</div>', re.S)
        findimg = re.compile(r'src="(.*?)"/>')
        findlast = re.compile(r'<div class="rank_d_b_last" title="(.*?)">')
        findtype = re.compile(r'<a target="_blank">(.*?)</a>')
        findinfo = re.compile(r'<div class="rank_d_b_info">(.*?)</div>', re.S)
        findlastlink = re.compile(r' href="(.*?)" target="_blank"><span class="rank_d_lastchapter">最新章节')
        datalist = []
        j = 1
        for i in range(1, 4):
            url = self.baseurl + str(i)
            html = self.askurl(url)
            soup = BeautifulSoup(html, "html.parser")
            for item in soup.find_all('div', class_="rank_d_list borderB_c_dsh clearfix"):
                rank = j
                j = j + 1
                data = []
                item = str(item)
                # get data according to the regular expressions
                link = re.findall(findLink, item)[0]
                authorlink = re.findall(findLink, item)[2]
                title = re.findall(findtitle, item)[0]
                author = re.findall(findtitle, item)[2]
                info = re.findall(findinfo, item)[0]
                img = re.findall(findimg, item)[0]
                last = re.findall(findlast, item)[0]
                typee = re.findall(findtype, item)[0]
                lastlink = re.findall(findlastlink, item)[0]
                data.append(rank)
                data.append(link)
                data.append(authorlink)
                data.append(title)
                data.append(author)
                data.append(info)
                data.append(img)
                data.append(last)
                data.append(typee)
                data.append(lastlink)
                datalist.append(data)
        return (datalist)
    # # create the first page
    def creatNet(self):
        app = Flask(__name__)
        @app.route('/')
        def index():
            datalist = []
            data = self.getdata()
            for item in data:
                datalist.append(item)
            return render_template("index2.html", rank=datalist)

        @app.route('/index')
        def home():
            datalist = []
            data = self.getdata()
            for item in data:
                datalist.append(item)
            return render_template("index2.html", rank=datalist)

        # make Pagination
        @app.route('/1')
        def rank1():
            datalist = []
            data = self.getdata()
            for i in range(0, 15):
                datalist.append(data[i])
            return render_template("1.html", rank1s=datalist)

        @app.route('/16')
        def rank16():
            datalist = []
            data = self.getdata()
            for i in range(15, 30):
                datalist.append(data[i])
            return render_template("16.html", rank2s=datalist)

        @app.route('/31')
        def rank31():
            datalist = []
            data = self.getdata()
            for i in range(30, 45):
                datalist.append(data[i])
            return render_template("31.html", rank3s=datalist)

        @app.route('/46')
        def rank46():
            datalist = []
            data = self.getdata()
            for i in range(45, 60):
                datalist.append(data[i])
            return render_template("46.html", rank4s=datalist)
        return app

if __name__ == '__main__':
    p = crawler().creatNet()
    p.run(debug=True)
