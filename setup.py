#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Setup for pytest-focus plugin. """


from setuptools import setup

setup(
    name="pytest-focus",
    version="0.1.1",
    description="A plugin that alerts users of failed test cases with notifications",
    url="https://github.com/inTestiGator/pytest-focus",
    author="Matthew Baldeosingh, et al.",
    author_email="baldeosinghm@allegheny.edu",
    license="MIT",
    # long_description=read("README.md"),
    py_modules=["pytest_focus"],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    # install_requires=["pytest>=3.5.0"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=['pytest'],
    entry_points={'pytest11': ['focus = pytest_focus', ], },
)
