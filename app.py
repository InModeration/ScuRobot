from flask import Flask, json, jsonify, request
from flask_cors import CORS
from userObject import User
from tokendef import tokendef
from session import Session
from questionsObject import Questions

from page_user import page_user
from wechat_dir.wechat import wechat

app = Flask(__name__)

app.register_blueprint(page_user, url_prefix='/user')
app.register_blueprint(wechat)#, url_prefix='/wechat')

app.config['JSON_AS_ASCII'] = False  # 解决乱码问题
CORS(app, supports_credentials=True)  # 允许跨域


@app.route('/login', methods=['GET','POST'])
def login():
    result = {
        'message': "fail",
        'action': "login",
        'info': "",
        'data':{}
    }
    # 登出
    if request.method =="GET":
        token = request.args.get("token")
        username = request.args.get("username")
        if tokendef.certify_token(key=username, token=token):
            # 注销seesion里面的信息
            new_session = Session(username)
            new_session.delete()
            result['message'] = 'successful'
            result['action'] = 'login_out'
            result['info'] = '注销成功'
            return jsonify(result)
        else:
            result['action'] = 'login_out'
            result['info'] = 'token 过期'
            return jsonify(result)

    # 登录
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get('password')

        user = User(username)
        isRight = user.verify_password(password)  # 在数据库里面核对密码，
        if isRight:  # if password is right
            new_session = Session(username=username)
            token = tokendef.generate_token(username)  # 生成token
            if new_session.query() == None:  # 如果session里面无记录
               new_session.token = token
               new_session.add()
               result['info'] = "新加用户token"
            else:
               # session 里面已经存在该用户了,则更新token就好
               new_session.token = token
               new_session.update()
               result['info'] = '更新用户token'
            result['message'] = 'successful'
            result['data'] = {
                'token':token,
                'username':username
            }
            return jsonify(result)
        else:
            result['info'] = "密码错误"
            return jsonify(result)
    else:
        return "405 禁用请求中指定的方法。"

@app.route('/sign',methods=['POST','delete'])
def sign():
    result = {
        'message': "fail",
        'action': "sign",
        'info':""
    }
    if request.method == 'POST':
        username = request.form.get("username")
        name = request.form.get('name')
        password = request.form.get('password')

        user = User(username)
        user.hash_password(password)  # 加密密码
        user.name = name
        sign_info = user.setNewUser()
        if sign_info:
            result['message'] = 'successful'
            result['info'] = "注册成功"
        else:
            result['info'] = '已存在该用户名'
        return jsonify(result)
    elif request.method == 'DELETE':
        result['info'] = "暂不开发删除用户功能"
        result['action'] ="delete"
        return jsonify(result)  # 删除用户
    else:
        return "405 禁用请求中指定的方法。"

@app.route('/userinfo',methods=["GET"])
def userinfo():
    if request.method =="GET":
        token = request.args.get("token")
        username = request.args.get("username")
        print(token,username)
        if tokendef.certify_token(username, token):
            session = Session(username)
            if session.query() != None:
                user = User(username)
                info = user.queryinfo()
        return jsonify(info)

@app.route('/')
def index():
    return "welcome!"

@app.route('/question',methods=['GET','POST'])
def question():
    if request.method == 'GET': # TODO GET 方法获取一定 num 数量的问题
        questions_json = {}
        return questions_json #jsonify(result)
    elif request.method == "POST":  # TODO POST 增加一个问题
        q_name = request.form.get("q_name")
        q_decribe = request.form.get("q_decribe")
        q_tag_data = request.form.get("q_tag")  # 以逗号为分割符
        q_tag = q_tag_data.split(",")
        create_user = request.form.get("create_user")
        Q = Questions(q_name=q_name,q_describe=q_decribe,q_tag=q_tag,create_user=create_user)
        try:
            a = Q.crate_a_question()
        except Exception:
            pass
        if a :
            return "200 OK"
        else:
            return "已存在该问题!"

    elif request.method == "DELETE": # TODO DELETE 删除一个问题
        return 0
    elif request.method == "PUT": # TODO PUT 修改一个问题
        return 0
    else:
        return "405 禁用请求中指定的方法。"


@app.route('/answers', methods=['GET','POST'])
def answers():
    if request.method == 'GET': # TODO GET 方法获取一定 num 数量的问题
        questions_json = {}
        return questions_json #jsonify(result)
    elif request.method == "POST": # TODO POST 增加一个问题
        pass
    elif request.method == "DELETE": # TODO DELETE 删除一个问题
        return 0
    elif request.method == "PUT": # TODO PUT 修改一个问题
        return 0
    else:
        return "405 禁用请求中指定的方法。"


@app.route("/q_and_a", methods=["GET", "POST"])
def q_and_a():
    if request.method == "GET":
        num = int(request.args.get("num"))  # 问题的数量
        data = Questions.query_all_question(limit=num, _id=1, q_name=1,
                                            q_decribe=1, answers=1,create_time=1,q_tag=1,create_user=1)
        for iter in data:
            iter["_id"] = str(iter["_id"])
        return jsonify(data), 200, {'Locateion':'www.baidu.com'}
    elif request.method == "POST":
        """获取一个问题和其答案"""
        q_id = request.form.get("_id")
        data = Questions.query_a_question(q_id=q_id)
        for iter in data:
            iter["_id"] = str(iter["_id"])
        return jsonify(data), 200, {'Locateion': 'www.baidu.com'}
    else:
        return "405 禁用请求中指定的方法。"


# TODO 查询频率最高的几个标签 num = 10
@app.route("/tag")
def get_tag():
    num = int(request.args.get("num"))  # 问题的数量
    import some_def
    data = some_def.Tag.query_fre_tag(num=num)
    return jsonify(data), 200, {'Locateion':'www.baidu.com'}



if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', port=80, debug=True)