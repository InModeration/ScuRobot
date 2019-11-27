from con_db import con_db
from questionsObject import Questions
import time

class Answer(object):
    _dbobj = con_db(collection='answers')
    _answer_colletion = _dbobj.demo_collection

    def __init__(self, q_id, a_content, create_user=""):
        self.q_id = q_id
        self.a_content = a_content
        self.create_user = create_user
        self.create_time = None
        self.update_time = None
        self.like = 0

    def crate_a_answer(self, answer_colletion=_answer_colletion):
        self.create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            answer_colletion.insert_one(self.__dict__)
        except Exception as e:
            print(e, "\n插入失败: ", self.__dict__)
            return False
        else:
            return True

    def detele_a_answer(self):
        pass

    def update_a_answer(self):
        self.update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        pass

    @staticmethod
    def query_a_question_all_answer(q_id, answer_colletion=_answer_colletion, **kwargs):
        """
        查询一个问题的所有答案
        :param q_id: 问题id
        :param kwargs: 需返回的字段
        :return:
        """
        query = {"q_id": q_id}
        answer_colletion.find(query)
        try:
            if kwargs == {}:
                a_cursor = answer_colletion.find(query)
            else:
                a_cursor = answer_colletion.find(query,kwargs)
        except Exception as e:
            print(e)
            return []
        else:
            return con_db.cursor_to_list(a_cursor)
        pass

    def like_add(self):

        # TODO 点赞加一
        pass

    @staticmethod
    def setIndex(answer_colletion=_answer_colletion):
        """设置questionsObject 对象数据库中的索引，只需运行一次，不要执行这个了"""
        try:
            answer_colletion.ensure_index([("a_content", 1)], unique=True)
        except Exception as e:
            print(e)
            return False
        else:
            return True

if __name__ == '__main__':
    a = Answer(q_id="5ddd2d870b7797308b018a42", a_content="川大食堂在4楼", create_user="zjianfa")
    a.crate_a_answer()
    a = Answer.query_a_question_all_answer(q_id="5ddd2d870b7797308b018a42")
    print(a)