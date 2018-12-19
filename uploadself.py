# encoding=utf8

import os
from flask import Flask, request, redirect, url_for,send_from_directory,render_template,make_response,jsonify
from werkzeug import secure_filename
import urllib,urllib2
import json
import redis

app = Flask(__name__)
data = {
    "20181214": {
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

    "20181215": {
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
    def __init__(self):
        self.index =""
        self.result = data
        # self.index = datas.keys()
        # result = sorted(datas.items(), key=lambda x: x[1], reverse=False)
        # self.response =

list=Alist()

@app.route('/lesson_list',methods = ['POST', 'GET'])
def get_list():
    if request.method == 'POST':
        strings = request.get_json()
        list.index = strings['index']
        list.result =data.get(list.index)["arrange"]
        #print list.index

        resp=make_response()
        resp.status_code = 200
        resp.headers["content-type"] = "text/html"
        resp.response = render_template('lesson_list_content.html',result= list.result)
        #return jsonify(list.result)
        return resp
    else:
        sorted_result = sorted(data.items(), key=lambda x: x[1], reverse=False)
        sorted_result = sorted_result[0][1]["arrange"]
    print list.index
    return render_template('lesson_list.html',result= sorted_result,index = list.index )





if __name__ == "__main__":
    app.run(debug=True)
    #app.run(debug=True)
