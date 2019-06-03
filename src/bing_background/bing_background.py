#!/usr/bin/env python
# coding=utf-8

import urllib
# import urllib
import urllib.request
from urllib.parse import urljoin
import time
import ssl
import json
import os.path
import os


class BingbgDownloader:
    __bing_domain = 'https://cn.bing.com'
    __request_url = '/HPImageArchive.aspx?format=js&idx=0&n=%s&nc=1530545682185&pid=hp'
    _count = 0
    __image_dir = '.img'

    def __init__(self):
        super(BingbgDownloader, self).__init__()
        ssl._create_default_https_context = ssl._create_unverified_context

    # 获取请求信息
    def _get_request_info(self, count):
        fullpath = urljoin(
            self.__bing_domain, self.__request_url, True)
        stream = urllib.request.urlopen(fullpath % (count))
        data = stream.read()
        jsonObject = json.loads(bytes.decode(data))
        self._get_img_in_response(jsonObject)

    # 解释出图片信息内容
    def _get_img_in_response(self, data):
        # fileArray = []
        # print(data["images"])
        imageFolder = os.path.join('./', self.__image_dir)
        if os.path.exists(imageFolder) == False:
            os.mkdir(os.path.join('./', self.__image_dir))

        print(data["images"])
        for img in data["images"]:
            self._download_img(img["url"], './%s/%s.jpg' % (self.__image_dir,img["hsh"]))
            # print(fileobject)

    # 下载壁纸
    def _download_img(self, img_url, fullname):
        try
            img_data = urllib.request.urlopen(
                urljoin(self.__bing_domain, img_url)).read()
            with open(fullname, 'wb') as file:
                file.write(img_data)
        except Exception as e: 
            print('下载失败：%s' %(img_url))

        

    def downImg(self, count):
        if count < 1:
            count = 1
        self._get_request_info(count)


if __name__ == "__main__":
    dl = BingbgDownloader()
    dl.downImg(4)
