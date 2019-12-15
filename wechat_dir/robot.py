#!/usr/bin python
#coding: utf8

import requests
import json
import wechat_dir.bot_online as bot_online
import scu_robot.searchQuestion

# 存储用户对话会话数据,对象
user_data = {}

# TODO 简单做下。后面慢慢来
# 关键词 获取回复
def get_response_by_keyword(keyword, FromUserName):
    """
    用户输入公众号的内容，返回需要回应的
    :param keyword: 用户输入的文字内容
    :return:
    """
    result = {"type": "text", "content": ""}
    if keyword[0:2] == "川大":
        # TODO 使用自己的接口函数
        keyword = keyword[2:]
        print("查询信息：", keyword)
        res = scu_robot.searchQuestion.searchByText(keyword)
        contens = res[0]["answers"]
        respose = ''
        for i in contens:
            respose = respose + i["content"]
        print(respose)
        result["content"] = respose
        return result
    elif(keyword[0:4] == "四川大学"):
        result["content"] = "四川大学（Sichuan University）简称“川大”，坐落于" \
                            "四川省会成都，是教育部直属、中央直管副部级的全国重点大学" \
                            "；位列国家“211工程”、“985工程”、“世界一流大学建设高校A类”" \
                            "，入选珠峰计划、2011计划、111计划、卓越工程师教育培养计划、" \
                            "卓越医生教育培养计划、卓越法律人才教育培养计划、国家建设高水平大学" \
                            "公派研究生项目、中国政府奖学金来华留学生接收院校、全国深化创新创业" \
                            "教育改革示范高校，为学位授权自主审核单位、中国研究生院院长联席会成" \
                            "员单位、医学“双一流”建设联盟成员、自主划线高校，是国家布局在中国" \
                            "部重点建设的高水平研究型综合大学。"
        return result
    elif(keyword[0:2] == "你是"):
        result["content"] = "Hi，我是川大旺仔机器人，我知道川大的一切，我可以查天气，讲笑话，订机票哦~ 除此之外还有几十项实用好玩的功能哦~ 快来试试吧"
        return result
    else:
        # 先查询用户数据字典里面有没有信息，若无信息则新建一个对象，并存储，
        # 若有信息则查看是否过期，若没有过期，则继续使用之前的对象，若过期新建，更新对象
        # user_data = wechat_dir.user_data.user_robot_data  # dict Object
        print(user_data.keys())
        if FromUserName in user_data.keys():
            user_chat_object = user_data[FromUserName]
            if user_chat_object.time_difference:
                content = user_chat_object.get_chat(data=keyword)
            else:  # 若过期了
                user_chat_object = bot_online.A_chat(FromUserName)  # 用户名
                user_data[FromUserName] = user_chat_object
                content = user_chat_object.get_chat(data=keyword)
        else:
            user_chat_object = bot_online.A_chat(FromUserName)  # 用户名
            user_data[FromUserName] = user_chat_object
            content = user_chat_object.get_chat(data=keyword)
        content = content.replace("小i", "旺仔", 3)
        result = {"type": "text", "content": content}
        return result

    #
    # if '团建' in keyword:
    #     result = {"type": "image", "content": "3s9Dh5rYdP9QruoJ_M6tIYDnxLLdsQNCMxkY0L2FMi6HhMlNPlkA1-50xaE_imL7"}
    # elif "学习" in keyword:
    #     result = {"type":"text", "content":"我也不知道学习是什么"}
    # elif 'music' in keyword or '音乐' in keyword:
    #     musicurl='http://204.11.1.34:9999/dl.stream.qqmusic.qq.com/C400001oO7TM2DE1OE.m4a?vkey=3DFC73D67AF14C36FD1128A7ABB7247D421A482EBEDA17DE43FF0F68420032B5A2D6818E364CB0BD4EAAD44E3E6DA00F5632859BEB687344&guid=5024663952&uin=1064319632&fromtag=66'
    #     result = {"type": "music", "content": {"title": "80000", "description":"有个男歌手姓巴，他的女朋友姓万，于是这首歌叫80000", "url": musicurl, "hqurl": musicurl}}
    # elif '关于' in keyword:
    #     items = [{"title": "关于我", "description":"喜欢瞎搞一些脚本", "picurl":"https://avatars1.githubusercontent.com/u/12973402?s=460&v=4", "url":"https://github.com/guoruibiao"},
    #              {"title": "我的博客", "description":"收集到的，瞎写的一些博客", "picurl":"http://avatar.csdn.net/0/8/F/1_marksinoberg.jpg", "url":"http://blog.csdn.net/marksinoberg"},
    #              {"title": "薛定谔的��", "description": "副标题有点奇怪，不知道要怎么设置比较好","picurl": "https://www.baidu.com/img/bd_logo1.png","url": "http://www.baidu.com"}
    #              ]
    #     result = {"type": "news", "content": items}
    # else:
    #     result = {"type": "text", "content": "可以自由进行拓展",'description':"asfdasfsdfsdfs"}
    # return result

# def get_turing_response(req=""):
#     url = "http://www.tuling123.com/openapi/api"
#     secretcode = "嘿嘿，这个就不说啦"
#     response = requests.post(url=url, json={"key": secretcode, "info": req, "userid": 12345678})
#     return json.loads(response.text)['text'] if response.status_code == 200 else ""
#
# def get_qingyunke_response(req=""):
#     url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg={}".format(req)
#     response = requests.get(url=url)
#     return json.loads(response.text)['content'] if response.status_code == 200 else ""