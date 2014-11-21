#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created: zhangpeng <zhangpeng1@infohold.com.cn>

import myapp

from torweb.urls import url
from torweb.tmpl import get_environment

env = get_environment(myapp.__name__)
