# SQLAlchemy Sphinx

SQLAlchemy Sphinx is a dialect for SQLalchemy which converts SQLAlchemy model into compatible sql for sphinx.

This dialect works for both python 2 and 3. Currently you need to import sqlalchemy_sphinx to properly register for python 3.

## Installation

SQLAlchemy Sphinx is available on pypi under the package name `sqlalchemy-sphinx`, you can get it by running:

```sh
pip install sqlalchemy-sphinx
```

## Usage

Defining a Sphinx SQLAlchemy is exactly the same way you would create a sqlalchemy model.

```python

from sqlalchemy import create_engine, Column, Integer, String, BigInteger, Unicode, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import deferred, sessionmaker

sphinx_engine = create_engine('sphinx://your.sphinx.host:9008')
SphinxBase = declarative_base(bind=sphinx_engine)
SphinxSession = sessionmaker(bind=sphinx_engine)
sphinx_session = SphinxSession()


class MockSphinxModel(Base):
    __tablename__ = "mock_table"
    name = Column(String)
    id = Column(Integer, primary_key=True)
    country = Column(String)
    ranker = deferred(Column(String))
    group_by_dummy = deferred(Column(String))
    max_matches = deferred(Column(String))
    field_weights = deferred(Column(String))
```


After the model is created we can run queries against the model:


```python
query = session.query(MockSphinxModel).limit(100)
sql_text = query.statement.compile(sphinx_engine).string
# 'SELECT name, id, country \nFROM mock_table\n LIMIT 0, 100'
```


We can also do matching

```python
query = session.query(MockSphinxModel.id)
query = query.filter(MockSphinxModel.name.match("adriel"), MockSphinxModel.country.match("US"))
sql_text = query.statement.compile(sphinx_engine).string
assert sql_text == "SELECT id \nFROM mock_table \nWHERE MATCH('(@name adriel) (@country US)')"
```

Options:

```python
query = session.query(MockSphinxModel.id)
query = query.filter(func.options(MockSphinxModel.field_weights == ["title=10", "body=3"]))
sql_text = query.statement.compile(sphinx_engine).string
assert sql_text == 'SELECT id \nFROM mock_table OPTION field_weights=(title=10, body=3)'

query = session.query(MockSphinxModel.id)
query = query.filter(MockSphinxModel.country.match("US"), func.options(MockSphinxModel.max_matches == 1))
sql_text = query.statement.compile(sphinx_engine).string
assert sql_text == "SELECT id \nFROM mock_table \nWHERE MATCH('(@country US)') OPTION max_matches=1"
```