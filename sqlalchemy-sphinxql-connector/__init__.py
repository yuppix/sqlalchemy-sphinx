from sqlalchemy.dialects import registry

__version__ = "0.1"

# https://bitbucket.org/zzzeek/sqlalchemy/issues/3536/engine-entrypoint-plugins
registry.register("sphinx", "sqlalchemy-sphinxql-connector.mysqldb", "Dialect")
registry.register("sphinx.cymsql", "sqlalchemy-sphinxql-connector.cymysql", "Dialect")
registry.register("sphinx.mysqldb", "sqlalchemy-sphinxql-connector.mysqldb", "Dialect")
