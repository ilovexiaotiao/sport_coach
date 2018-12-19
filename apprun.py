# encoding=utf8

import os
from flask import Flask, request, redirect, url_for,send_from_directory,render_template,make_response,jsonify
from werkzeug import secure_filename
import urllib,urllib2
import json
import redis
import collections

app = Flask(__name__)
data = {
    "0": {
        "name": "瑜伽",
        "desc": "45分钟|舞蹈|免费",
        "arrange": {
            "20181214": [{
                "start": "16:00",
                "end": "17:00",
                "teacher": "高中华1",
                "type": "瑜伽老师",
                "url": "",
                    },
                    {
                "start": "16:00",
                "end": "17:00",
                "teacher": "高中华1",
                "type": "瑜伽老师",
                "url": "",
                    },
                ],

            "20181215": [{
                "date": "12月14日",
                "start": "16:00",
                "end": "17:00",
                "teacher": "刘中华1",
                "type": "瑜伽老师",
                "url": ""
            },
                {
                    "date": "12月14日",
                    "start": "16:00",
                    "end": "17:00",
                    "teacher": "王中华1",
                    "type": "瑜伽老师",
                    "url": ""
                }
            ],
        },
    },

    "1": {
        "name": "交谊舞",
        "desc": "45分钟|舞蹈|免费",
        "arrange": {
            "20181214": [{
                "date": "12月14日",
                "start": "16:00",
                "end": "17:00",
                "teacher": "高中华",
                "type": "舞蹈老师",
                "url": ""
            },
                {
                    "date": "12月14日",
                    "start": "16:00",
                    "end": "17:00",
                    "teacher": "高中华",
                    "type": "舞蹈老师",
                    "url": ""
                }
            ],
            "20181215": [{
                "date": "12月14日",
                "start": "16:00",
                "end": "17:00",
                "teacher": "刘中华",
                "type": "舞蹈老师",
                "url": ""
            },
                {
                    "date": "12月14日",
                    "start": "16:00",
                    "end": "17:00",
                    "teacher": "王中华",
                    "type": "舞蹈老师",
                    "url": ""
                }
            ]

        }
    }
}

class Alist(object):
    def __init__(self,index,datas):
        result_sorted=collections.OrderedDict()
        self.index = index
        self.indexname = datas[index]["name"]
        self.indexdesc = datas[index]["desc"]
        print self.indexname
        result = datas.get(index)["arrange"]
        key_list = result.keys()
        key_list.sort()
        #print key_list
        result_sort = result_sorted.fromkeys(key_list)
        print result_sort
            # 循环赋值
        for i in range(0,len(key_list)):
            # if key_list[i] == result[i][0]:
            result_sort[key_list[i]] = result.get(key_list[i])
        self.result_sorted = result_sort


@app.route('/lesson_list',methods = ['POST', 'GET'])
def get_list():
    if request.method == 'POST':
        strings = request.get_json()
        indexname=strings['index']
        list = Alist(indexname, data)
        resp=make_response()
        resp.status_code = 200
        resp.headers["content-type"] = "text/html"
        resp.response = render_template('lesson_list_content.html',result= list.result_sorted,indexname=list.indexname,desc=list.indexdesc)
        #return jsonify(list.result)
        return resp
    else:
        sorted_result = sorted(data.items(), key=lambda x: x[1], reverse=False)
        sorted_result = sorted_result[0][1]["arrange"]
    return render_template('lesson_list.html',result= sorted_result )


if __name__ == "__main__":
    app.run(debug=True)
    #app.run(debug=True)
