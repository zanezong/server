#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

"""
作为配置文件的示例，可根据具体部署服务器环境不同，使用不同的配置文件。也可以把所有配置文件都放在此文件夹内，分别命名。
"""
ROOT_PATH = os.path.dirname(os.getcwd())
print os.path.join(ROOT_PATH, "static")
# 数据连接相关
# mysql配置，可根据命名在DataConnection里做连接池以及读写分离
db_settings=dict(
        read={
            "host": "118.89.215.71",
            "port": 3306,
            "user": "root",
            "password": "sigewudi",
            "database": "bibisha",
            },
        write={
            "host": "118.89.215.71",
            "port": 3306,
            "user": "root",
            "password": "sigewudi",
            "database": "bibisha",
            },
        )

# PYTHON_PATH 基础要求需要logic、server、util等模块，默认这三个模块是在同一目录下，所以直接引入该目录即可
PYTHON_PATH = ["../",]

# tornado配置
tornado = {
        "static_path" : os.path.join(ROOT_PATH, "templates"),
        "template_path" : os.path.join(ROOT_PATH, "templates"),
        "gzip" : True,
        "compress_response": True,
        "debug": True,
        }

# 模块加载与否配置
LOAD_MODULE = []
REJECT_MODULE = []
