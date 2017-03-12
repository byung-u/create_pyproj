create_pyproj
-------------

- create python project template like this.

- Reference
  - [Stackoverflow](http://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application)
  - [mypy](https://github.com/python/mypy)

```
Project/
|-- LICENSE
|-- README.md
|-- TODO.md
|-- docs
|   |-- conf.py
|   |-- generated
|   |-- index.rst
|   |-- installation.rst
|   |-- modules.rst
|   |-- quickstart.rst
|   |-- project.rst
|-- project/
|   |-- test/
|   |   |-- __init__.py
|   |   |-- test_main.py
|   |
|   |-- __init__.py
|   |-- exception.py
|   |-- main.py
|   |-- model.py
|-- requirements.txt
|-- scripts/
|   |-- project
|-- setup.py
```

Release
-------------
- 0.1.0 (current)
  - Create project directory
  - Create related files
