#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sf_server.UserController import IndexHandler, ToLoginRegisterHandler
handlers_mapping=[
    (r"/", IndexHandler),
    (r"/tologinregister", ToLoginRegisterHandler)
]