#!/usr/bin/env python
#coding=utf-8

'''
钉钉人工智障
https://oapi.dingtalk.com/robot/send?access_token=09473b6a3223256d0bd790a6d6838bd58cfe81e82d230e05a82e6743622740ae

'''
import urllib
import json
import urllib.request
import ssl

class DingTalkClient(object):
    def __init__(self, webhook):
        super(DingTalkClient,self).__init__()
        self.__webhook = webhook
    
    def sendText(self, msg, isAtAll=False, atMobiles=[]):
        sendData = {
            "msgtype": "text", 
            "text": {
                "content": msg
            }, 
            "at": {
                "atMobiles": atMobiles, 
                "isAtAll": isAtAll
            }
        }
        return self.__post(sendData)
    
    def sendMarkDown(self, title, content, isAtAll = False, atMobiles = []):  
        sendData = {
            "msgtype": "markdown",
            "markdown": {
                "title":title,
                "text": content
            },
            "at": {
                "atMobiles": atMobiles, 
                "isAtAll": isAtAll
            }
        }
        return self.__post(sendData);

    def __post(self, data):
        print(data)
        send_data = json.JSONEncoder().encode(data)
        ssl._create_default_https_context = ssl._create_unverified_context
        req = urllib.request.Request(self.__webhook, str.encode(send_data))
        req.add_header("Content-Type", "application/json")
        content = urllib.request.urlopen(req).read()
        # print(content)
        return content;


webhook = 'https://oapi.dingtalk.com/robot/send?access_token=09473b6a3223256d0bd790a6d6838bd58cfe81e82d230e05a82e6743622740ae'
client = DingTalkClient(webhook)
client.sendText("我的主人说我是小智障，我很不开心")
client.sendMarkDown("明天天气是", "#### 东风转南风\n" +
                                                                "> 南风转西风\n" +
                                                                "> \n" +
                                                                "> 西风转北风\n" +
                                                                "> \n" +
                                                                "> 北风转旋风")
