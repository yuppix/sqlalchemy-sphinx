from setuptools import setup

setup(
    name="sqlalchemy-sphinxql-connector",
    version="0.1.0",
    description="SQLAlchemy extension for dealing with SphinxQL",
    long_description=open("README.rst", "r").read(),
    packages=['sqlalchemy-sphinxql-connector'],
    zip_safe=False,
    install_requires=[
        "sqlalchemy > 0.9",
    ],
    entry_points={
     'sqlalchemy.dialects': [
          'sphinx = sqlalchemy-sphinxql-connector.mysqldb:Dialect',
          'sphinx.cymysql = sqlalchemy-sphinxql-connector.cymysql:Dialect',
          'sphinx.mysqldb = sqlalchemy-sphinxql-connector.mysqldb:Dialect'
          ]
    }
)