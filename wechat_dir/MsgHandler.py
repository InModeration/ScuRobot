import time
import json
from wechat_dir.robot import *

class MsgHandler(object):
    """
    针对type不同，转交给不同的处理函数。直接处理即可
    """

    def __init__(self, msg):
        self.msg = msg
        self.time = int(time.time())

    def textHandle(self, user='', master='', time='', content=''):
        template = """
        <xml>
             <ToUserName><![CDATA[{}]]></ToUserName>
             <FromUserName><![CDATA[{}]]></FromUserName>
             <CreateTime>{}</CreateTime>
             <MsgType><![CDATA[text]]></MsgType>
             <Content><![CDATA[{}]]></Content>
         </xml>
        """
        # 对用户发过来的数据进行解析，并执行不同的路径
        result = ""
        try:
            # print("用户名：", user)
            response = get_response_by_keyword(self.msg.content, FromUserName=user)  # 用户信息问题输入口

            if response['type'] == "image":
                result = self.imageHandle(self.msg.user, self.msg.master, self.time, response['content'])
            elif response['type'] == "music":
                data = response['content']
                result = self.musicHandle(data['title'], data['description'], data['url'], data['hqurl'])
            elif response['type'] == "news":
                items = response['content']
                result = self.newsHandle(items)
            # 这里还可以添加更多的拓展内容
            elif response['type'] == "text":
                data = response["content"]
                # response = "测试"
                # print(result)
                result = template.format(self.msg.user, self.msg.master, self.time, data)
                print("1", result)
            else:
                pass
                # response = get_turing_response(self.msg.content)
                # result = template.format(self.msg.user, self.msg.master, self.time, response)
            #with open("./debug.log", 'a') as f:
            #   f.write(response['content'] + '~~' + result)
            #    f.close()
        except Exception as e:
            # with open("./debug.log", 'a') as f:
               # f.write("text handler:"+str(e.message))
               # f.close()
            pass
        return result

    def musicHandle(self, title='', description='', url='', hqurl=''):
        template = """
        <xml>
             <ToUserName><![CDATA[{}]]></ToUserName>
             <FromUserName><![CDATA[{}]]></FromUserName>
             <CreateTime>{}</CreateTime>
             <MsgType><![CDATA[music]]></MsgType>
             <Music>
             <Title><![CDATA[{}]]></Title>
             <Description><![CDATA[{}]]></Description>
             <MusicUrl><![CDATA[{}]]></MusicUrl>
             <HQMusicUrl><![CDATA[{}]]></HQMusicUrl>
             </Music>
             <FuncFlag>0</FuncFlag>
        </xml>
        """
        response = template.format(self.msg.user, self.msg.master, self.time, title, description, url, hqurl)
        return response

    def voiceHandle(self, user=''):
        print(self.msg.recognition)
        template = """
                <xml>
                     <ToUserName><![CDATA[{}]]></ToUserName>
                     <FromUserName><![CDATA[{}]]></FromUserName>
                     <CreateTime>{}</CreateTime>
                     <MsgType><![CDATA[text]]></MsgType>
                     <Content><![CDATA[{}]]></Content>
                 </xml>
                """
        # 对用户发过来的数据进行解析，并执行不同的路径
        result = ""
        try:
            # print("用户名：", user)
            response = get_response_by_keyword(self.msg.recognition, FromUserName=user)  # 用户信息问题输入口
            if response['type'] == "image":
                result = self.imageHandle(self.msg.user, self.msg.master, self.time, response['content'])
            elif response['type'] == "music":
                data = response['content']
                result = self.musicHandle(data['title'], data['description'], data['url'], data['hqurl'])
            elif response['type'] == "news":
                items = response['content']
                result = self.newsHandle(items)
            # 这里还可以添加更多的拓展内容
            elif response['type'] == "text":
                data = response["content"]
                # response = "测试"
                # print(result)
                result = template.format(self.msg.user, self.msg.master, self.time, data)
                print("1", result)
            else:
                pass
                # response = get_turing_response(self.msg.content)
                # result = template.format(self.msg.user, self.msg.master, self.time, response)
            # with open("./debug.log", 'a') as f:
            #   f.write(response['content'] + '~~' + result)
            #    f.close()
        except Exception as e:
            # with open("./debug.log", 'a') as f:
            # f.write("text handler:"+str(e.message))
            # f.close()
            pass
        return result

    def imageHandle(self, user='', master='', time='', mediaid=''):
        template = """
        <xml>
             <ToUserName><![CDATA[{}]]></ToUserName>
             <FromUserName><![CDATA[{}]]></FromUserName>
             <CreateTime>{}</CreateTime>
             <MsgType><![CDATA[image]]></MsgType>
             <Image>
             <MediaId><![CDATA[{}]]></MediaId>
             </Image>
         </xml>
        """
        if mediaid == '':
            response = self.msg.mediaid
        else:
            response = mediaid
        result = template.format(self.msg.user, self.msg.master, self.time, response)
        return result

    def videoHandle(self):


        return 'video'

    def shortVideoHandle(self):
        return 'shortvideo'

    def locationHandle(self):
        return 'location'

    def linkHandle(self):
        return 'link'

    def eventHandle(self, user='', master='', time='', content=''):
        print("----------------------")
        template = """
                <xml>
                     <ToUserName><![CDATA[{}]]></ToUserName>
                     <FromUserName><![CDATA[{}]]></FromUserName>
                     <CreateTime>{}</CreateTime>
                     <MsgType><![CDATA[text]]></MsgType>
                     <Content><![CDATA[{}]]></Content>
                 </xml>
                """
        # 对用户发过来的数据进行解析，并执行不同的路径
        result = ""
        try:
            # print("用户名：", user)
            response = get_response_by_keyword(keyword="关于")  # 用户信息问题输入口
            if response['type'] == "image":
                result = self.imageHandle(self.msg.user, self.msg.master, self.time, response['content'])
            elif response['type'] == "music":
                data = response['content']
                result = self.musicHandle(data['title'], data['description'], data['url'], data['hqurl'])
            elif response['type'] == "news":
                items = response['content']
                result = self.newsHandle(items)
            # 这里还可以添加更多的拓展内容
            elif response['type'] == "text":
                data = response["content"]
                # response = "测试"
                # print(result)
                result = template.format(self.msg.user, self.msg.master, self.time, data)
                print("1", result)
            else:
                pass
                # response = get_turing_response(self.msg.content)
                # result = template.format(self.msg.user, self.msg.master, self.time, response)
            # with open("./debug.log", 'a') as f:
            #   f.write(response['content'] + '~~' + result)
            #    f.close()
        except Exception as e:
            # with open("./debug.log", 'a') as f:
            # f.write("text handler:"+str(e.message))
            # f.close()
            pass
        return result

    def newsHandle(self, items):
        # 图文消息这块真的好多坑，尤其是<![CDATA[]]>中间不可以有空格，可怕极了
        articlestr = """
        <item>
            <Title><![CDATA[{}]]></Title>
            <Description><![CDATA[{}]]></Description>
            <PicUrl><![CDATA[{}]]></PicUrl>
            <Url><![CDATA[{}]]></Url>
        </item>
        """
        itemstr = ""
        for item in items:
            itemstr += str(articlestr.format(item['title'], item['description'], item['picurl'], item['url']))

        template = """
        <xml>
            <ToUserName><![CDATA[{}]]></ToUserName>
            <FromUserName><![CDATA[{}]]></FromUserName>
            <CreateTime>{}</CreateTime>
            <MsgType><![CDATA[news]]></MsgType>
            <ArticleCount>{}</ArticleCount>
            <Articles>{}</Articles>
        </xml>
        """
        result = template.format(self.msg.user, self.msg.master, self.time, len(items), itemstr)
        return result