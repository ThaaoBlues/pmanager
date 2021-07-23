## compilation :
- ``python setup.py sdist bdist_wheel``


## test package :

- publish on test.pypi.org to check if everything is right :
    - ``twine upload -r testpypi dist/*``

- install package from test.pypi :
    - ``python -m pip install -i https://test.pypi.org/simple/ projects_manager --upgrade``


- test the new features :

    - ``whatever it's new``

## publish on pypi.org


- publish on pypi.org :
    - ``twine upload dist/*``

- install package :
    - ``python -m pip install projects_manager``