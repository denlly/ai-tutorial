# 小试牛刀

## 钉钉机器人

任务描述

1.  使用 Python 作为客户端，调用钉钉 WebHook 的接口
2.  面向对象的思想设计客户端
3.  完成任务

技术点

1. http 组件 urllib
2. OO 的设计
3. 封装自定义的 Python 库

物料

1. [python3.7.x](https://www.python.org/ftp/python/3.7.3/python-3.7.3-macosx10.9.pkg)
2. [钉钉开发文档](https://open-doc.dingtalk.com/microapp/serverapi2/qf2nxq)

## get started

1. 设计一个类包含以下成员

-   私有属性 webhook
-   私有方法\_\_post
-   共有方法 sendText 和 sendMarkdown

2.  完成 post 方法

    -   请求是 Https 的协议，增加 ssl.\_create_default_https_context = ssl.\_create_unverified_context

    -   请求过程增加 “Content-Type” 的设置 req.add_header("Content-Type", "application/json")

3.  调用完成其他方法调用

### 参考文档

        - https://www.programcreek.com/python/example/83039/ssl._create_unverified_context
