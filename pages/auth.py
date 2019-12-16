from flask import Blueprint, render_template,request,jsonify
from userObject import User
from tokendef import tokendef
from session import Session
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
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
        print(isRight)
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
                'token': token,
                'username': username
            }
            return jsonify(result)
        else:
            result['info'] = "密码错误"
            return jsonify(result)
    else:
        return "405 禁用请求中指定的方法。"

@auth.route('/sign',methods=['POST','delete'])
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

@auth.route('/userinfo',methods=["GET"])
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