from flask import request, make_response,Blueprint
import hashlib
from wechat_dir.dispatcher import *
from AppLog import AppLog
mylog = AppLog("test")

wechat = Blueprint('wechat', __name__)

@wechat.route('/wechat', methods=["GET", "POST","DETELE","PUT"])
def main():
    return "OK"


@wechat.route('/wechat_api', methods=["GET", "POST"])
def wechat_api():
    if request.method == 'GET':
        # 这里改写你在微信公众平台里输入的token
        print("--------------------")
        token = '123456789'
        # 获取输入参数
        data = request.args
        signature = data.get('signature', '')
        timestamp = data.get('timestamp', '')
        nonce = data.get('nonce', '')
        echostr = data.get('echostr', '')
        # 字典排序
        list = [token, timestamp, nonce]
        list.sort()
        s = list[0] + list[1] + list[2]
        # sha1加密算法
        hascode = hashlib.sha1(s.encode('utf-8')).hexdigest()
        # 如果是来自微信的请求，则回复echostr
        if hascode == signature:
            return echostr
    else:
        rec = request.stream.read()  # 接收消息
        # mylog.info(u'request data:', '\n', rec.decode())
        dispatcher = MsgDispatcher(rec)
        data = dispatcher.dispatch()
        response = make_response(data)
        response.content_type = 'application/xml'
        return response

