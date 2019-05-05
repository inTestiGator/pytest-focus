#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Setup for pytest-focus plugin. """

from setuptools import setup

setup(
    name="pytest-focus",
    version="0.1.1",
    description="A plugin alerting users of failed test cases with notifications",
    url="https://github.com/inTestiGator/pytest-focus",
    # pylint: disable=locally-disabled, multiple-statements, fixme, line-too-long
    author="Matthew Baldeosingh, Josh Yee, Alex Yarkosky, Zachary Shaffer, Mohammad Kahn",
    # pylint: disable=locally-disabled, multiple-statements, fixme, line-too-long
    author_email="baldeosinghm@allegheny.edu, yeej2@allegheny.edu, yarkoskya@allegheny.edu, shafferz@allegheny.edu, kahnm@allegheny.edu",
    license="MIT",
    py_modules=["pytest_focus"],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
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
    install_requires=["pytest"],
    entry_points={"pytest11": ["focus = pytest_focus"]},
)
