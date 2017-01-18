#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exception Class
class ErrException(Exception):
    def __init__(self, err_code, err_msg):
        self.err_code = err_code
        self.err_msg = err_msg

class BaseException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)