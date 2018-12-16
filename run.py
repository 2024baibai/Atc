#-*- coding=utf-8 -*-
from flask import Flask,render_template,request,jsonify,g
from wb_util import Weibo
from config import *
import datetime

app = Flask(__name__)
app.config.from_object('config')

#微博
t=Weibo(username=WEIBO_USERNAME,password=WEIBO_PASSWORD)

@app.route( '/' )
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    name=request.form.get('name')
    upload_file = request.files['file']
    filepath=u'./upload/{}'.format(name)
    upload_file.save(filepath)
    url=t.upload(filepath)
    return jsonify({'upload':True,'href':url})


if __name__ == "__main__":
    app.run()
