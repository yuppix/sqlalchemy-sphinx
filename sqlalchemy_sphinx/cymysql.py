""" CyMySQL connector"""

from __future__ import absolute_import

import cymysql
from cymysql.connections import Connection
from sqlalchemy.dialects.mysql import cymysql as cymysql_dialect
from sqlalchemy_sphinx.dialect import SphinxDialect

__all__ = ("Dialect",)


class DBAPIShim(object):

    def connect(self, *args, **kwargs):
        return Connection(*args, **kwargs)

    def __getattr__(self, name):
        return getattr(cymysql, name)


class Dialect(SphinxDialect, cymysql_dialect.MySQLDialect_cymysql):

    @classmethod
    def dbapi(cls):
        return DBAPIShim()
