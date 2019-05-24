""" mysql-connector connector"""

import mysql.connector
from mysql.connector import (connection)
from sqlalchemy.dialects.mysql import mysqlconnector
from sqlalchemy_sphinxql_connector.dialect import SphinxDialect

__all__ = ("Dialect",)


class DBAPIShim(object):

    def connect(self, *args, **kwargs):
        return connection.MySQLConnection(*args, **kwargs)

    def __getattr__(self, name):
        return getattr(mysql.connector, name)


class Dialect(SphinxDialect, mysqlconnector.MySQLDialect_mysqlconnector):

    @classmethod
    def dbapi(cls):
        return DBAPIShim()
