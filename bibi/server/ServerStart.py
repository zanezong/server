#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../")

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options
from server.route_mapping import handlers_mapping
import os
from server.DataConnection import DataConnection
import importlib
define("port", default=8889, help="服务器端口", type=int)

if __name__ == "__main__":
    define("config", default="../config/api3_settings.py", help="server config file", type=str)
    tornado.options.parse_command_line()
    # 读取config文件，并设置其中配置的python path
    config_path = os.path.abspath(os.path.dirname(options.config))
    sys.path.append(config_path)
    print "config_path是什么？", config_path
    settings = __import__(os.path.basename(options.config)[:-3])
    app = tornado.web.Application(handlers=handlers_mapping, **settings.tornado)
    app.dbc = DataConnection(settings.db_settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()