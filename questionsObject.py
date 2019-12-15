import time
from con_db import client, con_db
from bson.objectid import ObjectId

class Answer(object):
    def __init__(self, content, create_user):
        self.content = content
        self.create_user = create_user
        self.create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.update_time = None
        self.like = 0
        self.id = None
    def get_attr(self):
        return self.__dict__

class Questions(object):
    client.get_collection(collection="questions")
    _question_colletion = client.demo_collection

    def __init__(self, q_name, q_describe='', q_tag=[], create_user=''):
        """
        :param q_name:问题名
        :param q_describe: 问题描述
        :param q_tag: 问题标签,类型为列表
        :param create_user: 创建者
        :param answers: 答案字典
        """
        self.q_name = q_name
        self.q_decribe = q_describe
        self.q_tag = q_tag
        self.create_user = create_user
        self.create_time = None
        self.update_time = None
        self.like = 0
        self.answers = []

    def crate_a_question(self, question_colletion=_question_colletion):
        """
        创建一个新的问题
        :return:
        """
        self.create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            question_colletion.insert_one(self.__dict__)
        except Exception as e:
            print(e, "\n插入失败: ", self.__dict__)
            return False
        else:
            return True

    def insert_a_answer(self, question_colletion=_question_colletion,answer_obj=None):
        """
        :type answer_obj: Answer
        """
        myquery = {"q_name": self.q_name}
        answer = answer_obj
        newvalues = {"$push": {"answers": answer}}
        question_colletion.update_one(myquery, newvalues, upsert=False)
        return True

    def detele_a_question(self, question_colletion=_question_colletion):
        query = {"q_name": self.q_name, "create_user": self.create_user}
        print(query)
        try:
            # a = question_colletion.find(query)
            # print(Questions.cursor_to_list(a))
            question_colletion.delete_one(query)
        except Exception as e:
            print(e)
            return False
        else:
            # TODO 还应该在Answer Class 中删除对于的answer
            return True

    @staticmethod
    def like_add_to_answer(q_id, answer_id, question_colletion=_question_colletion):


        # TODO 点赞加一
        query = {
                "_id": ObjectId(q_id),
                'answers.id': answer_id
                }
        print(query)
        # a = question_colletion.find_one(query,{"_id":0,"answers":1})
        # print(a)
        newvalues = {"$set": {"answers.$.like": 2}}
        try:
            pass
            question_colletion.update_one(query, newvalues)
        except Exception as e:
            print(e)
        return 0

    def update_a_question(self):
        self.update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        pass
        # TODO 更新一个问题，只有该问题没有被人回答才可能被更新

    @staticmethod
    def query_a_question(q_id, question_colletion = _question_colletion):
        query = {"_id": ObjectId(q_id)}
        q_cursor = question_colletion.find(query)
        return con_db.cursor_to_list(q_cursor)

    @staticmethod
    def query_all_question(question_colletion=_question_colletion, limit=0, **kwargs):
        """
        查询所有问题
        :param kwargs:  {"_id":0, "q_name":1,"q_decribe":1} 需要那个一个参数，就设置为1
        :return list
        """

        try:
            if kwargs == {}:
                q_cursor = question_colletion.find({}, limit=limit)
            else:
                q_cursor = question_colletion.find({}, kwargs, limit=limit)
        except Exception as e:
            print(e)
            return []
        else:
            return con_db.cursor_to_list(q_cursor)

    @staticmethod
    def query_some_question(q_tag=[], q_name=[], question_colletion=_question_colletion, **kwargs):
        """
        查询部分问题，模糊匹配
        :param q_tag:标签
        :param kwargs: 指定返回属性
        :return: list
        """
        if len(q_tag) == 0 and len(q_name) == 0:
            print("缺少查询信息")
            return []

        string_name, string_tag = '', ''
        for i in q_tag:
            if len(i) < 2:
                i = i + " "
            string_tag += i + '|'
        string_tag = string_tag[0:-1]

        for i in q_name:
            if len(i) < 2:
                i = i + " "
            string_name += i + '|'
        string_name = string_name[0:-1]

        try:
            if kwargs == {}:
                if len(q_tag) == 0:
                    q_json = question_colletion.find({"q_name": {"$regex": string_name}})
                elif len(q_name) == 0:
                    q_json = question_colletion.find({"q_tag": {"$regex": string_tag}})
                else:
                    q_json = question_colletion.find(
                        {"q_tag": {"$regex": string_tag}, "q_name": {"$regex": string_name}})
            else:
                if len(q_tag) == 0:
                    q_json = question_colletion.find({"q_name": {"$regex": string_name}}, kwargs)
                elif len(q_name) == 0:
                    q_json = question_colletion.find({"q_tag": {"$regex": string_tag}}, kwargs)
                else:
                    q_json = question_colletion.find(
                        {"q_tag": {"$regex": string_tag}, "q_name": {"$regex": string_name}}, kwargs)
        except Exception as e:
            print(e)
            return []
        else:
            return con_db.cursor_to_list(q_json)

    @staticmethod
    def del_all_questions(question_colletion=_question_colletion):
        try:
            question_colletion.remove({})
        except Exception as e:
            print(repr(e))
        else:
            return True

    @staticmethod
    def setIndex(question_colletion=_question_colletion):
        """设置questionsObject 对象数据库中的索引，只需运行一次"""
        try:
            question_colletion.ensure_index([("q_name", 1)], unique=True)
        except Exception as e:
            print(e)
            return False
        else:
            return True



if __name__ == '__main__':
    # a = Questions.query_all_question(limit=1)
    # print(a)
    # a = Questions.query_a_question(q_id="5df075fe6509ae4878f38279")
    # print(a)
    #
    Questions.like_add_to_answer(q_id="5df075fe6509ae4878f3827a",answer_id="0")

    a = Questions.query_a_question(q_id="5df075fe6509ae4878f3827a")
    print(a)
    # q_demo = Questions(q_name="江安宿舍情况怎么样呢", create_user="zjianfa", q_tag=["江安","宿舍","住宿"], q_describe="新生宿舍怎么样")

    # a = Questions.query_all_question()
    # print(a[0:10])
    # print("插入问题demo, q_name 为主键")
    # #
    # q_demo = Questions(q_name="你是一只特立独行的猪3", q_tag=["123", "石凳子", "我 "], q_describe="因为今天中午我找了很久都没找到",
    #                    create_user="zjianfa")
    # q_demo.insert_a_answer()
    # q_demo.crate_a_question()
    #
    # # pass
    #
    # print("查询所有问题-- 返回全部属性")
    # a_list = q_demo.query_all_question()
    # print(a_list)
    #
    # print("查询所有问题-- 返回部分属性")
    # a_list = q_demo.query_all_question(_id=0, q_name=1, q_tag=1)
    # print(a_list)
    #
    # print("模糊查询问题和tag")
    # b_list = q_demo.query_some_question(q_name=["川大", "食堂"], q_tag=["美食"])
    # print(b_list)
#
#     print("删除一个问题")
#     q_demo = Questions(q_name="你是一只特立独行的猪2", create_user="zjianfa")
#     q_demo.detele_a_question()
