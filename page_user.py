from flask import Blueprint, render_template,request,jsonify
from userObject import User


page_user = Blueprint('user', __name__)

@page_user.route('/all_user', methods=["GET", "POST","DETELE","PUT"])
def all_user():
    if request.method == 'GET':  # TODO GET 方法获取一定 num 数量的用户
        num = int(request.args.get("num"))  # 问题的用户
        data = User.query_all_user(limit=num)
        for iter in data:
            iter["_id"] = str(iter["_id"])
        return jsonify(data), 200, {'Locateion':'www.scuker.xyz'}
    return "请求方法错误"

@page_user.route("/a_user",methods=["GET", "POST","DELETE","PUT"])
def a_user():
    if request.method == "GET":
        username = request.args.get("username")  # 问题的数量
        user = User(username=username)
        data = user.query_a_user()
        data_id = str(data[0]["_id"])
        # print(data_id)
        data[0]["_id"] = data_id
        # print(data)
        return jsonify(data), 200, {'Locateion':'www.baidu.com'}

    elif request.method == "POST":  # 新添一个用户
        username = request.form.get("username")
        name = request.form.get("name")
        password = request.form.get("password")
        new_user = User(username=username,name=name)
        new_user.hash_password(password=password)
        data = new_user.setNewUser()
        if data:
            return jsonify(("True", "新建成功")), 200, {'Locateion': 'www.scuker.xyz'}
        else:
            return jsonify(("Flase", "用户名重复")), 400, {'Locateion': 'www.scuker.xyz'}

    elif request.method == "DELETE":
        username = request.form.get("username")
        password = request.form.get("password")
        new_user = User(username=username)
        new_user.hash_password(password=password)
        data = new_user.del_a_user()
        if data:
            return jsonify(("True", "删除成功")), 200, {'Locateion': 'www.scuker.xyz'}
        else:
            return jsonify(("Flase", "删除失败")), 400, {'Locateion': 'www.scuker.xyz'}

    elif request.method == "PUT":  # TODO PUT 修改一个用户 成共返回更新后的信息
        username = request.form.get("username")
        default_value = username + "0"
        new_username = request.form.get("new_username", default_value)
        new_name = request.form.get("new_name", default_value)
        new_password = request.form.get("new_password", default_value)

        new_user = User(username=username)
        new_user.hash_password(password=new_password)
        new_password_hash = new_user.password

        data = new_user.update_a_user(username=new_username, password=new_password_hash, name=new_name)
        print(data)
        if data:
            # user = User(username=new_username)
            # data = user.query_a_user()
            # print(data)
            return jsonify(("True", "更新成功")), 200, {'Locateion': 'www.scuker.xyz'}
        else:
            return jsonify(("Flase", "更新失败")), 400, {'Locateion': 'www.scuker.xyz'}
    else:
        return "405 禁用请求中指定的方法。"
