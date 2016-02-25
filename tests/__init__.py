from sqlalchemy.dialects import registry

registry.register("sphinx", "sqlalchemy_sphinx.mysqldb", "Dialect")
registry.register("sphinx.cymsql", "sqlalchemy_sphinx.cymysql", "Dialect")
registry.register("sphinx.mysqldb", "sqlalchemy_sphinx.mysqldb", "Dialect")
