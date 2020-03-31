# import jieba
# import pymongo
# from questionsObject import Questions
# from scu_robot.preprocess import supCut
# from gensim import corpora,models,similarities
#
# def searchByText(text):
#     #分词，去除停用词，替换近义词
#     raw_word_list = supCut(text)
#
#     #创建词袋
#     dictionary = corpora.Dictionary([raw_word_list])
#
#     #制作语料库,测试文本向量
#     doc_test_vec = dictionary.doc2bow(raw_word_list)
#
#     pre_check_word_list = []
#     pre_check_result = Questions.query_some_question(q_name=raw_word_list)
#     for i in pre_check_result:
#         pre_check_word = supCut(i["q_name"])
#         pre_check_word_list.append(pre_check_word)
#
#     corpus = [dictionary.doc2bow(doc) for doc in pre_check_word_list]
#
#     # 语料库建模
#     tfidf = models.TfidfModel(corpus)
#
#     #分析相似度
#     index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
#     sim = index[tfidf[doc_test_vec]]
#
#     #相似度排序
#     sorted_result = sorted(enumerate(sim), key=lambda item: -item[1])
#
#     #获取最佳问题
#     result_ques = pre_check_result[sorted_result[0][0]]
#
#     pre_check_answer = result_ques["answers"]
#
#     #找出最佳答案
#     result_answer = {}
#     max_like = -1
#     for i in pre_check_answer:
#         if i["like"] > max_like:
#             max_like = i["like"]
#             result_answer = i
#
#     return [result_ques["q_name"], result_answer["content"]]
#
#
# if __name__ == '__main__':
#     res = searchByText("四川大学西园食堂")
#     print(res)
