#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created: zhangpeng <zhangpeng1@infohold.com.cn>

from torweb.handlers import BaseHandler
from myapp.shortcuts import env


class Handler(BaseHandler):
    def __str__(self):
        return self.__class__.__name__
    def render_to_string(self, template, **kwargs):
        tmpl = env.get_template(template)
        kwargs.update({
            "handler": self,
            "request": self.request,
            "reverse_url": self.application.reverse_url
        })
        template_string = tmpl.render(**kwargs)
        return template_string
    def render(self, template, **kwargs):
        template_string = self.render_to_string(template, **kwargs)
        self.write(template_string)

