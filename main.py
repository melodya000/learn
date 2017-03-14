#coding=utf8


"""
     alice.respond('what is your name')
     alice.respond('how old are you')
     alice.respond('who is your father')
     alice.respond('who are you')
     py3 code
"""
import urllib
import urllib.request
import requests
import json
import itchat
from itchat.content import *

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    print(msg)
    text = urllib.parse.quote(msg['Text'])
    # key   tuling app key
    # info  对方输入的内容
    # userid  可以忽略   主要是为了区分该用户  方便进行上下文的语义的识别
    respond = urllib.request.urlopen("http://www.tuling123.com/openapi/api?key=*********&info=%s&userid=1"%text)
    try:
        print(respond.read())
        body = json.loads(respond.read())
        info = body["text"]
    except:
        info = "抱歉 太深奥了 理解不动"
    itchat.send(info)
    # itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg['Text'](msg['FileName'])
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])

# @itchat.msg_register(TEXT, isGroupChat=True)
# def text_reply(msg):
#     if msg['isAt']:
#         itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])


def main():
    itchat.auto_login(hotReload=True)
    itchat.run()

if __name__ == '__main__':
    main()
