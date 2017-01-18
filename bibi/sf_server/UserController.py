#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


class ToLoginRegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login_register.html')


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.render('index.html')
