import questionsObject
import jieba
# import gensim

q_data = questionsObject.Questions(q_name="get_all_question")\
    .query_all_question(limit=888, _id=0, q_name=1)

class SearchAnswer(object):
    def __init__(self, q_string):
        self.data = q_data
        self.q_string = q_string
        self.jieba_string =0

    def char_cut(self):
        # 精准模式
        text_cut = jieba.cut(self.q_string)
        text = []
        for i in text_cut:
            text.append(i)
        return text





if __name__ == '__main__':
    a = SearchAnswer("宿舍")
    text = a.cut()
    from questionsObject import Questions
    value = Questions.query_some_question(q_name=text)
    print(value)
