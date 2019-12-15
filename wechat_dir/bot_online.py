import requests, re
import json
import datetime

class A_chat(object):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ("
                             "KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}

    def __init__(self, wechat_name):
        self.wechat_name = wechat_name
        self.robotId = None
        self.userId = None
        self.sessionId = None
        self.id_info = None
        self.get_all_id()
        self.cookies = None
        self.creat_time = datetime.datetime.now()

    def time_difference(self):
        """
        判断该对象是否过期
        :return: 过期返回False
        """
        start = self.creat_time
        end=datetime.datetime.now()
        if (end - start).seconds > 30:  # 30 秒数
            return False
        else:
            return True


    @staticmethod
    def json_parsing(data):
        """
        将返回回来的字符串解析为json
        :param data:response
        :return:dirt
        """
        reg = re.findall(r'[{](.*)[}]', data)[0]
        data = "{" + reg + "}"
        return json.loads(data)

    @staticmethod
    def punctuate(data):
        """切分语句"""
        result = data.split("__webrobot_processMsg")
        return result[-1]

    def get_all_id(self):
        """获取 三个ID"""
        url = "http://i.xiaoi.com/robot/webrobot?&callback=__webrobot__processOpenResponse&" \
              "data=%7B%22type%22%3A%22open%22%7D&ts=1576170536940"
        response = requests.get(url, headers=self.headers).text
        try:
            datadir = self.json_parsing(response)
            self.id_info = datadir
        except Exception as e:
            print(e)
        # 赋值
        self.robotId = datadir["robotId"]
        self.userId = datadir["userId"]
        self.sessionId = datadir["sessionId"]

    def get_chat(self, data):
        """
        获取回答
        :param data:
        :return:
        """
        url_0 = "http://i.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data="
        dir = self.id_info
        body_dir = {"content": data}
        dir["body"] = body_dir
        dir["type"] = "txt"
        url = url_0 + str(dir) + "&ts=1576173243291"
        if self.cookies ==None:
            response = requests.get(url, headers=self.headers)
            self.cookies = response.cookies.get_dict()
            data_0 = self.punctuate(response.text)
            data = self.json_parsing(data_0)
            result0 = "Hi，我是川大旺仔机器人，我可以查天气，讲笑话，订机票哦~ 除此之外还有几十项实用好玩的功能哦~ 快来试试吧\r\n"
            result1 = data["body"]["content"]
            return result0+result1
        else:
            response = requests.get(url, headers=self.headers, cookies=self.cookies)
            data_0 = self.punctuate(response.text)
            data = self.json_parsing(data_0)
            result1 = data["body"]["content"]
            return result1.strip()

if __name__ == '__main__':
    new_chat = A_chat("zjianfa")
    # print(new_chat.__dict__)
    a = new_chat.get_chat(data="天气")
    b = new_chat.get_chat(data="成都")
    print(a, b)


