# encoding=utf8

import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template, make_response, jsonify
# from werkzeug import secure_filename
import urllib, urllib2
import json, os, datetime
# import redis
import collections

app = Flask(__name__)
path = "E:\Nicholas Shan\sport_coach\static\json\lesson_list.json"
with open(path, "r") as f:
    # file = file.decode("utf-8-sig")
    data = json.load(f)




