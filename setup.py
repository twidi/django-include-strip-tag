#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

from setuptools import setup, find_packages

import include_strip_tag

long_description = codecs.open('README.md', "r", "utf-8").read()

setup(
    name = "django-include-strip-tag",
    version = include_strip_tag.__version__,
    author = include_strip_tag.__author__,
    author_email = include_strip_tag.__contact__,
    description = include_strip_tag.__doc__,
    keywords = "django include templatetag template strip",
    url = include_strip_tag.__homepage__,
    download_url = "https://github.com/twidi/django-include-strip-tag/downloads",
    packages = find_packages(),
    include_package_data=True,
    license = "MIT",
    platforms=["any"],
    zip_safe=True,

    long_description = long_description,

    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
)
