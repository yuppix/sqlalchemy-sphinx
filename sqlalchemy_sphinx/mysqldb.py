""" MySQLdb connector"""

from __future__ import absolute_import

import MySQLdb
from sqlalchemy.dialects.mysql import mysqldb as mysqldb_dialect
from sqlalchemy_sphinx.dialect import SphinxDialect

__all__ = ("Dialect",)


class DBAPIShim(object):

    def connect(self, *args, **kwargs):
        return MySQLdb.Connection(*args, **kwargs)

    def __getattr__(self, name):
        return getattr(MySQLdb, name)


class Dialect(SphinxDialect, mysqldb_dialect.MySQLDialect_mysqldb):

    @classmethod
    def dbapi(cls):
        return DBAPIShim()
