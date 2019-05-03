# pytest-focus

![pytest-focus](static/focus-logo.png "pytest-focus logo")

[![Build Status](https://api.travis-ci.com/inTestiGator/pytest-focus.svg?branch=master)](https://travis-ci.com/inTestiGator/pytest-focus)
[![codecov.io](http://codecov.io/github/inTestiGator/pytest-focus/coverage.svg?branch=master)](http://codecov.io/github/inTestiGator/pytest-focus?branch=master)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-orange.svg)](https://www.python.org/)
[![code-style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
![license-mit](https://img.shields.io/github/license/inTestiGator/pytest-focus.svg)

Welcome to pytest-focus, a pytest plugin designed to make you focus as you write
test cases until they pass. This tool aims to help you stay on top of making all
the test cases in your test suite pass by relaying which ones fail to pass as
they are run and tested. Notifications will be sent detailing which test case
failed when it happens. Currently supports Linux, MacOS, and Windows 10
operating systems.

## Checks

The following checks are made on the project via these commands:

`pipenv run pytest tests --cov-config pytest.cov --cov`

* The command above checks that the pytest test suite works and that the code
    coverage is not lowered when new additions are added

`pipenv run black **/*.py --check`

* The command above checks that all `.py` python code adheres to the black
  code style

`pipenv run flake8 **/*.py`

* The command above checks that all `.py` python code adheres to the standards
    of `flake8`

`pipenv run pylint **/*.py`

* The command above checks that all `.py` python code adheres to the standards
    of `pylint` and gets rated "10/10"

`mdl README.md`

* The command above checks that the `README.md` adheres to the markdown
    language and its syntax

Failure for these commands to pass will result in the build failing to pass
`Travis CI`. Any build that does not pass this system will not be merged into
the `master` branch.
