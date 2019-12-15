import xml.etree.ElementTree as ET


# 解析消息xml参数
class MsgParser(object):
    """
    用于解析从微信公众平台传递过来的参数，并进行解析
    """
    def __init__(self, data):
        self.data = data
        self.et = ET.fromstring(self.data)

        self.user = self.et.find("FromUserName").text
        self.master = self.et.find("ToUserName").text
        self.msgtype = self.et.find("MsgType").text

        # 纯文字信息字段
        self.content = self.et.find("Content").text if self.et.find("Content") is not None else ""

        # 语音信息字段
        self.recognition = self.et.find("Recognition").text if self.et.find("Recognition") is not None else ""
        self.format = self.et.find("Format").text if self.et.find("Format") is not None else ""
        self.msgid = self.et.find("MsgId").text if self.et.find("MsgId") is not None else ""

        # 图片
        self.picurl = self.et.find("PicUrl").text if self.et.find("PicUrl") is not None else ""
        self.mediaid = self.et.find("MediaId").text if self.et.find("MediaId") is not None else ""

        # 事件
        self.event = self.et.find("Event").text if self.et.find("Event") is not None else ""

    # def parse(self):



        # return self
