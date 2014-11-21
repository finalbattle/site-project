#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created: zhangpeng <zhangpeng1@infohold.com.cn>

from myapp.shortcuts import *
from myapp.handlers import Handler
from code import interact

@url("/index")
class Index(Handler):
    def get(self):
        self.render("index.html")
