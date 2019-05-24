from sqlalchemy.dialects import registry

__version__ = "0.1.1"

# https://bitbucket.org/zzzeek/sqlalchemy/issues/3536/engine-entrypoint-plugins
registry.register("sphinx", "sqlalchemy_sphinxql_connector.mysqldb", "Dialect")
registry.register("sphinx.cymsql", "sqlalchemy_sphinxql_connector.cymysql", "Dialect")
registry.register("sphinx.mysqldb", "sqlalchemy_sphinxql_connector.mysqldb", "Dialect")
