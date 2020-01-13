# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import hashlib
import json
import base64

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/nlp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# ro2 = Role(name='user')
# User.query.all()
# bk = Book.query.filter_by(id=id).first()
# db.session.add(ro2)
# db.session.delete(user)
# db.session.commit()

class User(db.Model):
    # 定义表名
    __tablename__ = 'user'
    # 定义列对象
    num = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), unique=True)
    passwd = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    email = db.Column(db.String(255))
    # def __repr__(self):
    #     return 'Role:'.format(self.name)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/main')
def mainPage():
    perIntro = "Donec ullamcorper nulla non metus auctor fringilla. Vestibulum id ligula porta felis euismod semper. Praesent commodo cursus magna, vel scelerisque nisl consectetur. Fusce dapibus, tellus ac cursus commodo."
    return render_template("main.html", perIntro=perIntro)


@app.route('/resume', methods=['GET', 'POST'])
def resume():
    if request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))

        num = json_data["num"]
        user = User.query.filter_by(num=num).first()

        name = user.name
        phone = user.phone
        email = user.email

        # 构造json数据返回前端
        json_temp = {"num": num, "name": name, "phone": phone, "email": email}
        json_response = json.dumps(json_temp)
        return json_response
    else:
        return render_template("resume.html")


@app.route('/personal')
def personal():
    return render_template("personal.html")


@app.route('/perReport', methods=['GET', 'POST'])
def perReport():
    if request.method == 'POST':
        # 构造前端传来的json数据
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))

        num = json_data["num"]
        print("num:" + num)

        wCloudVal = [['foo', 12], ['bar', 6], ['你好', 59], ['谁在说话', 90]]
        emoVal = [{'name': '快乐', 'y': 61.41},
                  {'name': '焦虑', 'y': 11.84},
                  {'name': '痛苦', 'y': 10.85},
                  {'name': '愤恨', 'y': 4.67}]
        mapRatioVal = [{'name': '湖北', 'y': 61.41},
                       {'name': '吉林', 'y': 36.84},
                       {'name': '甘肃', 'y': 41.47}]
        emoTiVal = [{
            'name': '快乐',
            'data': [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175]},
            {
                'name': '焦虑',
                'data': [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434]},
            {
                'name': '痛苦',
                'data': [11744, 17722, 16005, 19771, 20185, 24377, 32147, 39387]},
            {
                'name': '愤恨',
                'data': [105, 2695, 7988, 12169, 15112, 22452, 34400, 34227]
            }]

        perlist = {'wCloud': wCloudVal, 'emoDistr': emoVal, "mapRatio": mapRatioVal,
                   "emoTiRatio": emoTiVal}

        # 构造json数据返回前端
        json_response = json.dumps(perlist)
        return json_response

    else:
        wCloudVal = []
        emoVal = []
        mapRatioVal = []
        emoTiVal = []

        perlist = {'wCloud': wCloudVal, 'emoDistr': emoVal, "mapRatio": mapRatioVal,
                   "emoTiRatio": emoTiVal}
        return render_template("perReport.html", perlist=perlist)


@app.route('/topic')
def topic():
    return render_template("topic.html")


@app.route('/topicReport', methods=['GET', 'POST'])
def topicReport():
    if request.method == 'POST':
        # 构造前端传来的json数据
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))

        ttopic = json_data["ttopic"]
        print("ttopic:" + ttopic)

        wCloudVal = [['foo', 12], ['bar', 6], ['你好', 59], ['谁在说话', 90]]
        chnMapVal = [{"name": "北京", "value": 27}, {"name": "天津", "value": 77}, {"name": "河北", "value": 11},
                     {"name": "山西", "value": 83}, {"name": "内蒙古", "value": 49}, {"name": "辽宁", "value": 65},
                     {"name": "吉林", "value": 57}, {"name": "黑龙江", "value": 31}, {"name": "上海", "value": 50},
                     {"name": "江苏", "value": 21}, {"name": "浙江", "value": 31}, {"name": "安徽", "value": 85},
                     {"name": "福建", "value": 73}, {"name": "江西", "value": 47}, {"name": "山东", "value": 49},
                     {"name": "河南", "value": 72}, {"name": "湖北", "value": 66}, {"name": "湖南", "value": 47},
                     {"name": "广东", "value": 18}, {"name": "广西", "value": 57}, {"name": "海南", "value": 50},
                     {"name": "重庆", "value": 76}, {"name": "四川", "value": 55}, {"name": "贵州", "value": 16},
                     {"name": "云南", "value": 60}, {"name": "西藏", "value": 24}, {"name": "陕西", "value": 54},
                     {"name": "甘肃", "value": 21}, {"name": "青海", "value": 78}, {"name": "宁夏", "value": 16},
                     {"name": "新疆", "value": 57}, {"name": "台湾", "value": 91}, {"name": "香港", "value": 58},
                     {"name": "澳门", "value": 27}, {"name": "南海诸岛", "value": 58}, {"name": "南海诸岛", "value": 80}]
        emoVal = [{'name': '快乐比例', 'y': 61.41},
                  {'name': '焦虑比例', 'y': 11.84},
                  {'name': '痛苦比例', 'y': 10.85},
                  {'name': '愤恨比例', 'y': 4.67}]
        sexRatioVal = [{'name': '男生数', 'y': 61.41},
                       {'name': '女生数', 'y': 51.84}]
        emoTiVal = [{
            'name': '快乐',
            'data': [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175]},
            {
                'name': '焦虑',
                'data': [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434]},
            {
                'name': '痛苦',
                'data': [11744, 17722, 16005, 19771, 20185, 24377, 32147, 39387]},
            {
                'name': '愤恨',
                'data': [105, 2695, 7988, 12169, 15112, 22452, 34400, 34227]
            }]

        perlist = {'wCloud': wCloudVal, 'chnMap': chnMapVal, 'emoDistr': emoVal, "sexRatio": sexRatioVal,
                   "emoTiRatio": emoTiVal}

        # 构造json数据返回前端
        json_response = json.dumps(perlist)
        return json_response

    else:
        wCloudVal = []
        chnMapVal = []
        emoVal = []
        sexRatioVal = []
        emoTiVal = []

        perlist = {'wCloud': wCloudVal, 'chnMap': chnMapVal, 'emoDistr': emoVal, "sexRatio": sexRatioVal,
                   "emoTiRatio": emoTiVal}
        return render_template("topicReport.html", perlist=perlist)


@app.route('/login', methods=['GET', 'POST'])
def login():
    flag = False
    if request.method == 'POST':

        num = request.form.get("num")
        passwd = request.form.get("passwd")

        print(num, passwd)

        # 创建md5对象
        m = hashlib.md5()
        b = passwd.encode(encoding='utf-8')
        m.update(b)
        passwd_md5 = m.hexdigest()

        try:
            user = User.query.filter_by(num=num).first()
            dbpasswd = user.passwd

            if dbpasswd == passwd_md5:
                flag = True
                token = num
                return render_template("log.html", flag=flag, token=token)

        except Exception as r:
            print(r)

        return render_template("log.html", flag=flag)
    else:
        return render_template("log.html")


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        # 构造前端传来的json数据
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))

        num = json_data["num"]
        name = json_data["name"]
        passwd = json_data["passwd"]
        phone = json_data["phone"]
        email = json_data["email"]

        # 创建md5对象
        m = hashlib.md5()
        b = passwd.encode(encoding='utf-8')
        m.update(b)
        passwd_md5 = m.hexdigest()

        user = User(num=num, name=name, passwd=passwd_md5, phone=phone, email=email)

        flag = False
        try:
            db.session.add(user)
            db.session.commit()
            flag = True
        except Exception as r:
            print(r)

        # 构造json数据返回前端
        json_temp = {"flag": flag}
        json_response = json.dumps(json_temp)
        return json_response
    else:
        return render_template("reg.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
