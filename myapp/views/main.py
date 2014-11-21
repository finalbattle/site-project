# -*- coding: utf-8 -*-

import myapp
from torweb.urls import url
from torweb.handlers import BaseHandler
from torweb.tmpl import get_environment

env = get_environment(myapp.__name__)

@url("/main")
class MainHandler(BaseHandler):
    def get(self):
        tmpl = env.get_template("main.html")
        data = {"name": "torweb"}
        return self.write(tmpl.render(**data))
