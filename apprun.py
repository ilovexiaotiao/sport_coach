# encoding=utf8

import os
from flask import Flask, request, redirect, url_for,send_from_directory,render_template,make_response,jsonify
from werkzeug import secure_filename
import urllib,urllib2
import json,os,datetime
import redis
import collections

app = Flask(__name__)
path = "E:\\sport_coach\\static\\json\\lesson_list1.json"
with open(path,"r") as f:
    # file = file.decode("utf-8-sig")
    data = json.load(f)


class Alist(object):
    def __init__(self,index,datas,datelist):
        result_sorted=collections.OrderedDict()
        self.index = index
        self.indexname = datas[index]["name"]
        self.indexdesc = datas[index]["desc"]
        #print self.indexname
        result = datas.get(index)["arrange"]
        key_list = result.keys()
        key_list.sort()
        #print key_list
        result_sort = result_sorted.fromkeys(key_list)
        #print result_sort
            # 循环赋值
        for i in range(0,len(key_list)):
            if key_list[i] in datelist:
                print key_list[i]
                result_sort[key_list[i]] = result.get(key_list[i])
            self.result_sorted = result_sort

class Adate(object):
    def __init__(self):
        self.date = datetime.date.today() + datetime.timedelta(days=1)


    def time_string(self,i):
        date1 = self.date + datetime.timedelta(days=i)
        return date1.strftime(
            '%a')

    def get_date_list(self):
        list = []
        for i in range(0,3):
            list.append(self.time_string(i))
        return list




@app.route('/lesson_list',methods = ['POST', 'GET'])
def get_list():
    if request.method == 'POST':
        strings = request.get_json()
        indexname=strings['index']
        dates = Adate()
        datelist = dates.get_date_list()
        list = Alist(indexname, data, datelist)
        print list.result_sorted
        resp=make_response()
        resp.status_code = 200
        resp.headers["content-type"] = "text/html"
        resp.response = render_template('lesson_list_content.html',result= list.result_sorted,indexname=list.indexname,desc=list.indexdesc,datelist = datelist)
        #return jsonify(list.result)
        return resp
    else:
        sorted_result = sorted(data.items(), key=lambda x: x[1], reverse=False)
        sorted_result = sorted_result[0][1]["arrange"]
    return render_template('lesson_list.html',result= sorted_result )


if __name__ == "__main__":
    app.run(debug=True)
    #app.run(debug=True)
