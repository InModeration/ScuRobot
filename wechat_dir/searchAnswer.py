import questionsObject
import jieba
from gensim import corpora, models, similarities
from zhon.hanzi import punctuation as ch_punctuation
import numpy as np

q_data = questionsObject.Questions(q_name="get_all_question")\
    .query_all_question(limit=888, _id=1, q_name=1, q_tag=1)

# 问题列表
q_text = []
for iter in q_data:
    q_text.append(iter["q_name"])

# 问题对应的id列表
q_id = []
for iter in q_data:
    q_id.append(str(iter["_id"]))



class SearchAnswer(object):
    def __init__(self, q_string):
        # self.data = q_data
        self.q_string = q_string
        self.jieba_string = 0
        self.remove_punctuation()

    def char_cut(self):
        # 精准模式
        text_cut = jieba.cut(self.q_string)
        text = []
        for i in text_cut:
            text.append(i)
        return text

    def remove_punctuation(self):
        translator = str.maketrans(dict.fromkeys(ch_punctuation))
        self.q_string = self.q_string.translate(translator)



# 字符串切割列表
q_text_cut = []
for iter in q_text:
    if iter is not None:
        a = SearchAnswer(iter)
        text = a.char_cut()
        q_text_cut.append(text)

# # print(q_text_cut)
# for i in q_data["q_tag"][0]:
#     print(i)
# print(q_data[0]["q_tag"])

# 2.生成词典
dictionary = corpora.Dictionary(q_text_cut)

# 3.通过doc2bow稀疏向量生成语料库
corpus = [dictionary.doc2bow(item) for item in q_text_cut]

# 4.通过TF模型算法，计算出tf值
tf = models.TfidfModel(corpus)

# 5.通过token2id得到特征数（字典里面的键的个数）
num_features = len(dictionary.token2id.keys())

# 6.计算稀疏矩阵相似度，建立一个索引
index_2 = similarities.MatrixSimilarity(tf[corpus], num_features=num_features)




def get_id_index(q_string):
    a = SearchAnswer(q_string)
    test_words = a.char_cut()  #[word for word in jieba.cut(test_text)]
    # 8.新的稀疏向量
    new_vec = dictionary.doc2bow(test_words)

    # 9.算出相似度
    sims = index_2[tf[new_vec]]


    index_list = np.where(sims == np.max(sims))[0]  # 最匹配元素下标
    max = np.max(sims)
    print(max)
    if max < 0.3:
        return False
    # print(index_list)
    q_id_query =[]
    for index in index_list:
        q_id_query.append(q_id[index])
    return q_id_query

def get_q_and_a(q_ids):
    relute = ""
    for id in q_ids:
        b = questionsObject.Questions.query_a_question(q_id=id)[0]
        relute = relute + b["q_name"] + "\n"
        i = 1
        for iter in b["answers"]:
            relute = relute + "回答" + str(i) + "\n"
            relute = relute + iter["content"] + "\n"
            i += 1
    return relute

def get_all(q_name = ""):
    a = get_id_index(q_name)
    if a == False:
        return "问题库暂时没有收录该问题，要不试试我们的提问论坛？\n www.scuker.xyz:8080 \n"
    b = get_q_and_a(a)
    return b

# if __name__ == '__main__':
#     a = get_id_index("江安寝室")
#     print(a)
#     b = get_q_and_a(a)
#     print(b)
#
#     c = get_all("江安寝室")
#     print(c)