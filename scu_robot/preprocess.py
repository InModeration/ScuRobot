# import jieba
#
# def stop():
#     stopfile = open("stopDic.txt", "r+", encoding="utf-8")
#     stopword = stopfile.read().split("\n")
#
#     return stopword
#
# def sim():
#     combine_dict = {}
#     for line in open("simDic.txt", "r+",encoding="utf-8"):
#         seperate_word = line.strip().split("\t")
#         num = len(seperate_word)
#         for i in range(1, num):
#             combine_dict[seperate_word[i]] = seperate_word[0]
#     return combine_dict
#
# def supCut(text):
#     raw_word_list = []
#     for word in jieba.cut(text):
#         if not (word in stopword):
#             if word in simword:
#                 word = simword[word]
#             raw_word_list.append(word)
#     return raw_word_list
#
# stopword = stop()
# simword = sim()
#
