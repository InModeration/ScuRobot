from flask import Blueprint, render_template,request,jsonify
from questionsObject import Questions
import wechat_dir.searchAnswer


question = Blueprint('question', __name__)

@question.route("/search_question", methods=['GET','POST'])
def search_question():
    if request.method == 'GET':
        return "not this method!"
    elif request.method == "POST":
        q_name = request.form.get("q_name")
        query = wechat_dir.searchAnswer.SearchAnswer(q_name)
        query = query.char_cut()
        data = Questions.query_some_question(q_name=query)
        for iter in data:
            iter["_id"] = str(iter["_id"])
        return jsonify(data), 200, {'Locateion':'www.scuker.xyz'}
    else:
        return "405 禁用请求中指定的方法。"

@question.route('/question', methods=['GET','POST'])
def question1():
    if request.method == 'GET':  # TODO GET 方法获取一定 num 数量的问题
        questions_json = {}
        return questions_json #jsonify(result)
    elif request.method == "POST":  # TODO POST 增加一个问题
        q_name = request.form.get("q_name")
        q_decribe = request.form.get("q_decribe")
        q_tag_data = request.form.get("q_tag")  # 以逗号为分割符
        print(q_tag_data)
        q_tag = q_tag_data.split(",")
        create_user = request.form.get("create_user")
        Q = Questions(q_name=q_name, q_describe=q_decribe, q_tag=q_tag, create_user=create_user)
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


@question.route('/answers', methods=['GET', 'POST'])
def answers():
    if request.method == 'GET': # TODO GET 方法获取一定 num 数量的问题
        questions_json = {}
        return "0" #jsonify(result)
    elif request.method == "POST": # TODO POST 增加一个问题
        return "0"
    elif request.method == "DELETE": # TODO DELETE 删除一个问题
        return "0"
    elif request.method == "PUT": # TODO PUT 修改一个问题
        return "0"
    else:
        return "405 禁用请求中指定的方法。"


@question.route("/q_and_a", methods=["GET", "POST"])
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
@question.route("/tag")
def get_tag():
    num = int(request.args.get("num"))  # 问题的数量
    import some_def
    data = some_def.Tag.query_fre_tag(num=num)
    return jsonify(data), 200, {'Locateion':'www.baidu.com'}