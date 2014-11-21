#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created: zhangpeng <zhangpeng1@infohold.com.cn>

import myapp
from torweb.urls import url
from torweb.handlers import BaseHandler

@url("/add")
class Add(BaseHandler):
    text = """
    <form action="/add" method="POST">
    <input type="text" name="a" value="%(a)s"/> +
    <input type="text" name="b" value="%(b)s"/> 
    <input type="submit" value="="/> 
    <input type="text" name="c" value="%(c)s"/> 
    </form>
    """
    def get(self):
        a = b = 0
        return self.write(self.text % {"a":a, "b":b, "c":a+b})
    def post(self):
        a = int(self.args.get("a", 0))
        b = int(self.args.get("b", 0))
        return self.write(self.text % {"a":a, "b":b, "c":a+b})
