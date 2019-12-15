import os
import pandas as pd
from questionsObject import Questions, Answer
from scu_log import AppLog

# 数据文件路径
PATH = "../data_to_db"
mylog = AppLog(name="Data_migration")

def read_excel(path):
    pd_data = pd.read_excel(path)
    return pd_data

def read_a_line(pd_data):
    data_list = []
    return data_list

def add_all_data():
    files_name = os.listdir(PATH)
    for name in files_name:
        filepath = PATH + '/' + name
        data = read_excel(filepath)  # 读入一个excel 的文具
        mylog.info(str(name+"开始插入:"))
        try:
            for i in range(data.shape[0]):  # 遍历每一行
                dataline = data.iloc[i]
                q = Questions(q_name=dataline["问题名称"], q_tag=dataline["问题标签"].split('、'),
                              q_describe=dataline["问题描述"], create_user="zjianfa")
                q.crate_a_question()

                # 插入一个答案
                index = 0
                for i in range(3, 6):
                    if pd.isna(dataline[i]):
                        pass
                    else:
                        a = Answer(content=dataline[i], create_user="scubot")
                        a.id = index
                        a = a.__dict__
                        q.insert_a_answer(answer_obj=a)
                        index += 1
        except Exception as e:
            print(repr(e))
            mylog.error(str("插入问题失败：", repr(e)))
        else:
            Questions.setIndex() # 设置索引
            mylog.info(str("插入完成"))

def del_all_data():
    if Questions.del_all_questions():
        mylog.info("删除完成")


if __name__ == '__main__':
    # del_all_data()
    add_all_data()



