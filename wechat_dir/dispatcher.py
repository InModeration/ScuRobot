# -*- coding:utf-8 -*-
import sys

import time
import json

from wechat_dir.robot import *
from wechat_dir.MsgParser import MsgParser  # 消息对象
from wechat_dir.MsgHandler import MsgHandler

class MsgDispatcher(object):
    """
    根据消息的类型，获取不同的处理返回值
    """

    def __init__(self, data):
        parser = MsgParser(data)
        self.msg = parser
        self.handler = MsgHandler(parser)

    def dispatch(self):
        self.result = ""  # 统一的公众号出口数据
        if self.msg.msgtype == "text":  # TODO 回复文字
            self.result = self.handler.textHandle(user=self.msg.user)
        elif self.msg.msgtype == "voice":
            self.result = self.handler.voiceHandle()
        elif self.msg.msgtype == 'image':
            self.result = self.handler.imageHandle()
        elif self.msg.msgtype == 'video':
            self.result = self.handler.videoHandle()
        elif self.msg.msgtype == 'shortvideo':
            self.result = self.handler.shortVideoHandle()
        elif self.msg.msgtype == 'location':
            self.result = self.handler.locationHandle()
        elif self.msg.msgtype == 'link':
            self.result = self.handler.linkHandle()
        elif self.msg.msgtype == 'event':
            self.result = self.handler.eventHandle()
        return self.result

