#!/usr/bin/env python
# -*- coding: utf-8 -*-

from server.exception import BaseException

class BaseLogic(object):
    """logic层处理业务逻辑，以及面向接口的字段格式转换，例如某一结构数据是以json字符串格式储存，但是在输出时需要转成json对象等"""
    def __init__(self, dbc=None):
        # for unit test
        if not dbc:
            raise BaseException("Data connection error.")
        self.dbc = dbc
        self.cache = dbc.cache


