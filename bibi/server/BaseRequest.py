# coding:utf-8
"""
提供基础模块。
"""
import tornado.web
import tornado.httpserver
import os, sys, json, hashlib, logging, importlib, random, pyDes
from DataConnection import DataConnection
from datetime import datetime, date

def format_date(obj):
    if isinstance(obj, datetime):
        return int(obj.strftime('%s'))
    if isinstance(obj, date):
        return obj.strftime('%Y-%m-%d')


def format_date2(obj):
    if isinstance(obj, datetime):
        return int(obj.strftime('%s')) * 1000
    if isinstance(obj, date):
        return obj.strftime('%Y-%m-%d')

class BaseRequestHandler(tornado.web.RequestHandler):
    """
    覆写tornado的RequestHandler
    使其可以配置url_pattern就可以被加载
    """
    config = None
    config_path = None
    url_pattern = None

    def __init__(self, *argc, **argkw):
        super(BaseRequestHandler, self).__init__(*argc, **argkw)
        self.wangcai_browser = self.request.headers.get("User-Agent", "").find("Wangcai Browser") > 0
        self.dbc = self.application.dbc

    def get_argument(self, name, default=tornado.web.RequestHandler._ARG_DEFAULT, strip=True):
        """增加从body里获取json格式参数的逻辑，以兼容客户端不同的传参方式"""
        if self.request.method == "POST" and self.request.body:
            # POST方法，请求中body是有值的，尝试对body进行json转换并获取参数
            try:
                _arg = json.loads(self.request.body).get(name)
                if _arg:
                    return _arg
            except:
                pass
        return self._get_argument(name, default, self.request.arguments, strip)


    def ret_plain_data2(self, data=None):
        """规划坑爹了，用此函数做临时补救方案，等客户端能支持了再统一。此接口返回的datetime统一为默认毫秒 """
        if type(data) == dict:
            data = json.dumps(data, sort_keys=True, default=format_date2)
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        return self.write(data)

    def ret_plain_data(self, data=None):
        return self.ret_data(data, crypt=False)

    def ret_data(self, data=None, crypt=True):
        # 格式统一为字符串
        if type(data) == dict:
            data = json.dumps(data, sort_keys=True, default=format_date)
        if self.current_user or self.wangcai_browser or not crypt:
            self.set_header("Content-Type", "application/json; charset=UTF-8")
            return self.write(data)
        else:
            return self.write(self.__encrypt(data))

    def ret_plain_error(self, ERROR_INFO, MSG=10001):
        return self.ret_error(ERROR_INFO, MSG, False)

    def ret_error(self, ERROR_INFO, MSG=10001, crypt=True):
        data = {"status": 10001, "msg": MSG}
        if self.current_user or self.wangcai_browser or not crypt:
            self.set_header("Content-Type", "application/json; charset=UTF-8")
            return self.write(json.dumps(data))
        else:
            return self.write(self.__encrypt(data))

