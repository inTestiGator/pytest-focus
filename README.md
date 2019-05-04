# pytest-focus
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a5522e362cd8486d9df3819918285163)](https://app.codacy.com/app/Alex-Yarkosky/pytest-focus?utm_source=github.com&utm_medium=referral&utm_content=inTestiGator/pytest-focus&utm_campaign=Badge_Grade_Dashboard)
[![All Contributors](https://img.shields.io/badge/all_contributors-5-orange.svg?style=flat-square)](#contributors)

![pytest-focus](static/focus-logo.png "pytest-focus logo")

[![All Contributors](https://img.shields.io/badge/all_contributors-5-orange.svg?style=flat-square)](#contributors)
[![Build Status](https://api.travis-ci.com/inTestiGator/pytest-focus.svg?branch=master)](https://travis-ci.com/inTestiGator/pytest-focus)
[![PyPI](https://img.shields.io/pypi/v/pytest-focus.svg?style=plastic)](https://pypi.org/project/pytest-focus/)
[![codecov.io](http://codecov.io/github/inTestiGator/pytest-focus/coverage.svg?branch=master)](http://codecov.io/github/inTestiGator/pytest-focus?branch=master)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-orange.svg)](https://www.python.org/)
[![code-style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
![license-mit](https://img.shields.io/github/license/inTestiGator/pytest-focus.svg)

Welcome to pytest-focus, a pytest plugin designed to make you focus as you write
test cases until they pass. The way that it completes this task, is through the
use of push notifications and a creation of a ToDo-list. As test cases fail,
pytest-focus sends the user notifications in real time about tests that have failed.
After all the tests have been checked, it creates a ToDo-list for the user to view
in order to help people focus on immediate problems. This tool aims to help
you stay on top of making all the test cases in your test suite pass by relaying
which ones fail to pass as they are run and tested. Notifications will be sent detailing which test case failed when it happens. Currently supports Linux,
MacOS, and Windows 10 operating systems.

## Setup
You can install this plugin from PYPI  and download dependencies by following
the following commands:

```
pipenv install pytest-focus --dev
pipenv install --dev
```

## Running pytest-focus

In order to run pytest-focus, run the following command:

`pipenv run pytest --focus`

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

## Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
<table><tr><td align="center"><a href="https://github.com/baldeosinghm"><img src="https://avatars0.githubusercontent.com/u/42876742?v=4" width="100px;" alt="Matthew Baldeosingh"/><br /><sub><b>Matthew Baldeosingh</b></sub></a><br /><a href="https://github.com/inTestiGator/pytest-focus/commits?author=baldeosinghm" title="Code">💻</a> <a href="https://github.com/inTestiGator/pytest-focus/commits?author=baldeosinghm" title="Documentation">📖</a> <a href="#ideas-baldeosinghm" title="Ideas, Planning, & Feedback">🤔</a> <a href="#review-baldeosinghm" title="Reviewed Pull Requests">👀</a></td><td align="center"><a href="http://www.shafferz.com"><img src="https://avatars1.githubusercontent.com/u/26298864?v=4" width="100px;" alt="Zachary Shaffer"/><br /><sub><b>Zachary Shaffer</b></sub></a><br /><a href="https://github.com/inTestiGator/pytest-focus/commits?author=shafferz" title="Code">💻</a> <a href="#ideas-shafferz" title="Ideas, Planning, & Feedback">🤔</a> <a href="#review-shafferz" title="Reviewed Pull Requests">👀</a> <a href="#question-shafferz" title="Answering Questions">💬</a></td><td align="center"><a href="http://alexander.yarkosky.xyz"><img src="https://avatars1.githubusercontent.com/u/36210455?v=4" width="100px;" alt="Alexander Yarkosky"/><br /><sub><b>Alexander Yarkosky</b></sub></a><br /><a href="https://github.com/inTestiGator/pytest-focus/commits?author=Alex-Yarkosky" title="Code">💻</a> <a href="#content-Alex-Yarkosky" title="Content">🖋</a> <a href="https://github.com/inTestiGator/pytest-focus/commits?author=Alex-Yarkosky" title="Documentation">📖</a> <a href="#infra-Alex-Yarkosky" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#review-Alex-Yarkosky" title="Reviewed Pull Requests">👀</a> <a href="#design-Alex-Yarkosky" title="Design">🎨</a></td><td align="center"><a href="https://github.com/ilikerustoo"><img src="https://avatars3.githubusercontent.com/u/25516043?v=4" width="100px;" alt="Mohammad Khan"/><br /><sub><b>Mohammad Khan</b></sub></a><br /><a href="https://github.com/inTestiGator/pytest-focus/commits?author=ilikerustoo" title="Code">💻</a> <a href="https://github.com/inTestiGator/pytest-focus/commits?author=ilikerustoo" title="Documentation">📖</a> <a href="#ideas-ilikerustoo" title="Ideas, Planning, & Feedback">🤔</a> <a href="#review-ilikerustoo" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/inTestiGator/pytest-focus/commits?author=ilikerustoo" title="Tests">⚠️</a> <a href="#platform-ilikerustoo" title="Packaging/porting to new platform">📦</a></td><td align="center"><a href="https://github.com/yeej2"><img src="https://avatars1.githubusercontent.com/u/22895281?v=4" width="100px;" alt="Joshua Yee"/><br /><sub><b>Joshua Yee</b></sub></a><br /><a href="https://github.com/inTestiGator/pytest-focus/commits?author=yeej2" title="Code">💻</a> <a href="https://github.com/inTestiGator/pytest-focus/commits?author=yeej2" title="Documentation">📖</a> <a href="#ideas-yeej2" title="Ideas, Planning, & Feedback">🤔</a> <a href="#review-yeej2" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/inTestiGator/pytest-focus/commits?author=yeej2" title="Tests">⚠️</a> <a href="#platform-yeej2" title="Packaging/porting to new platform">📦</a> <a href="#infra-yeej2" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td></tr></table>

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
