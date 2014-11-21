# -*- coding: utf-8 -*-

import myapp
from torweb.application import make_application
from torweb.config import CONFIG
from torweb import run_torweb


settings_path = "/home/zhangpeng/workspace/site-project/myapp/settings.yaml"

CONF = CONFIG(settings_path)

app = make_application(myapp, debug=True, wsgi=True,
                       settings_path=settings_path,
                       url_root=CONF("URL_ROOT")
                      )
run_torweb.run(app, port=CONF("PORT"))
