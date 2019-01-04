#!/usr/bin/env python
# encoding: utf-8

import itchat
import requests
import json
from app.handlers.base import HandlerBase
from itchat.core import Core


class LoginHandler(HandlerBase):
    def get(self):
        ins = Core()
        ins.auto_login(picDir="123.png")
        friends = itchat.get_friends(update=True)[0:]
        self.write("Hello World")


html_str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <img src="/static/123.png"  alt="二维码" />
</head>
<body>

</body>
</html>
"""


class QRHandler(HandlerBase):
    def get(self):
        self.write(html_str)
