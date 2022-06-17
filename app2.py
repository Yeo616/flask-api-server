from flask import Flask, jsonify
from http import HTTPStatus

app = Flask(__name__)

@app.route('/hithere', methods = ['GET'] )
def hi_there():
    return 'Hithere~~~'

@app.route('/add',methods = ['GET'])
def add():
    data = 283+111
    return str(data)

@app.route('/', methods = ['GET'])
def root():
    return '안녕하세요'

@app.route('/act/data', methods = ['GET'])
def act():
    ret = {'count': 2, 'students': [ {'name':'홍길동', 'age': 30}, 
                                     {'name': '김나나', 'age':25}]}
    return jsonify(ret)
    # 우리가 만든 파이썬 딕셔너리를, 파이썬으로 만들어주는 기능

if __name__ == '__main__':
    app.run()