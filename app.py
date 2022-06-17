from flask import Flask

app=Flask(__name__)

# API가 있어야 한다. 아래 코드가 API
@app.route('/', methods = ['GET'])
def hello_world():
    return 'Hello World hihi'

# '/': 최상위 경로라는 뜻,
# 이 경로로 요청이 오면, 서버(나)는 Hello World라고 응답할거다.
# 실행을 하면 우리 로컬에서 실행되는 것

if __name__ == '__main__':
    app.run()
