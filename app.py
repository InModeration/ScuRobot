from flask import Flask, json, jsonify, request
import flask_cors

# 蓝图管理
from pages.page_user import page_user
from pages.auth import auth
from pages.wechat import wechat
from pages.question import question

app = Flask(__name__)

app.register_blueprint(question)
app.register_blueprint(page_user, url_prefix='/user')
app.register_blueprint(wechat)#, url_prefix='/wechat')
app.register_blueprint(auth)


app.config['JSON_AS_ASCII'] = False  # 解决乱码问题
flask_cors.CORS(app, supports_credentials=True)  # 允许跨域

@app.route('/')
def index():
    return "welcome!"

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    # app.run(host='127.0.0.1', port=5000, debug=True)
    app.run(host='0.0.0.0', port=80, debug=True)