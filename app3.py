# from flask import Flask, jsonify,request
# # 클라이언트로부터 뭔가를 받는 건 request 라이브러리에 기능이 다 있다.
# from http import HTTPStatus

# # POST 보내는 법

# app = Flask(__name__)

# @app.route('/add_two_nums',methods = ['POST'])
# def add():
#     # 클라이언트로부터 두 수를 받는다.
#     data = request.get_json()
#     ret = data["x"] + data["y"]
#     result = {"result": ret}

#     return jsonify(result)
#     # json으로 리턴해야한다.

# if __name__ == '__main__':
#     app.run(port =5001)

from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)

@app.route('/add_two_nums', methods = ['POST'])
def add():
    # 클라이언트로부터 두 수를 받는다.
    data = request.get_json()
    ret = data['x'] + data['y']
    result = {"result" : ret}

    return jsonify(result)

if __name__ == '__main__' :
    app.run(port=5001)
