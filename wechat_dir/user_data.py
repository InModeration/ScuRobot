import datetime

"""
基本逻辑是 当调用该机器人时
先判断 we_chat_user 有无该用户，若没有：
    则这是一个新用户，新建一个A_chat对象,添加到 user_robot_data，然后把wechat_name 添加到we_chat_user 里面
若存在该用户
    则直接使用该用户信息
"""


# 存储用户对话会话数据,对象
user_robot_data ={}


