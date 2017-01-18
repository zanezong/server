#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
import torndb
class DataConnection(object):
    """
    数据连接模块，提供持久化存储以及缓存服务的数据连接。目前情况是mysql+redis
    本对象由web服务入口初始化
    """
    def __init__(self, db_settings):
        """
        db_settings 和 cache_settings 是key-value形式的配置集合dict。key固定为read和write，用于做读写分离，value为配置参数dict对象。value示例如下：
        db连接参数示例：
        {
            "host": "localhost",
            "port": 3306,
            "user": "root",
            "password": "xxxxx",
            "database": "test",
        }
        cache连接参数示例：
        {
            "host": "localhost",
            "port": 6379,
            "password": "xxxxx",
            "db": 0,
        }
        """
        self.__dbs = {}
        self.__caches = {}
        self.__db_connection = None
        self.__cache_connection = None
        if not "read" in db_settings or not "write" in db_settings:
            raise BaseException("db配置文件有误，无法找到读或写配置")
        # 如果有需求，可以在这里做mysql的连接池
        for _k, _v in db_settings.items():
            _v.update(dict(time_zone='+8:00'))
            _port = _v.pop("port")
            if _port:
                _v["host"] += ":%s"%_port
            self.__dbs[_k] = torndb.Connection(**_v)
        self.__db_connection = db_connection(self.__dbs['read'], self.__dbs['write'])

    @property
    def db(self):
        return self.__db_connection

    @property
    def db_read(self):
        return self.__dbs['read']

    @property
    def db_write(self):
        return self.__dbs['write']

    @property
    def cache(self):
        return self.__cache_connection

    @property
    def cache_read(self):
        return self.__caches['read']

    @property
    def cache_write(self):
        return self.__caches['write']

class db_connection(object):
    """区分读写的数据库连接对象，在类里进行读写连接的管理。后期可在此处做连接池的功能"""
    def __init__(self, read_conn, write_conn):
        self.read = read_conn
        self.write = write_conn

    def close(self):
        self.read.close()
        self.write.close()

    def reconnect(self):
        self.close()
        self._db = MySQLdb.connect(**self._db_args)
        self._db.autocommit(True)

    def __getattr__(self, attr):
        if attr in ['query', 'get', 'iter']:
            # 读操作
            return getattr(self.read, attr)
        elif attr in ['execute', 'execute_lastrowid', 'execute_rowcount', 'executemany', 'executemany_lastrowid', 'executemany_rowcount', 'insert', 'update']:
            # 写操作
            return getattr(self.write, attr)
        else:
            # 其他操作默认使用写链接
            return getattr(self.write, attr)


if __name__ == "__main__":
    mysql_settings = {
            "read" : {
                "host": "118.89.215.71",
                "port": 3306,
                "user": "root",
                "password": "sigewudi",
                "database": "bibisha",
                },
            "write" : {
                "host": "118.89.215.71",
                "port": 3306,
                "user": "root",
                "password": "sigewudi",
                "database": "bibisha",
                }
            }
    dbc = DataConnection(mysql_settings)


