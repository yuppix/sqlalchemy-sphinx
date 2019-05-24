from setuptools import setup

setup(
    name="sqlalchemy_sphinxql_connector",
    version="0.1.1",
    description="SQLAlchemy extension for dealing with SphinxQL",
    long_description=open("README.rst", "r").read(),
    packages=['sqlalchemy_sphinxql_connector'],
    zip_safe=False,
    install_requires=[
        "sqlalchemy > 0.9",
    ],
    entry_points={
     'sqlalchemy.dialects': [
          'sphinx = sqlalchemy_sphinxql_connector.mysql_connector:Dialect',
          'sphinx.cymysql = sqlalchemy_sphinxql_connector.cymysql:Dialect',
          'sphinx.mysqldb = sqlalchemy_sphinxql_connector.mysqldb:Dialect'
          ]
    }
)