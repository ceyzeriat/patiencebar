#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv, exit
import re, os

if "upl" in argv[1:]:
    import os
    os.system("python setup.py register -r pypi")
    os.system("python setup.py sdist upload -r pypi")
    exit()

try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup
    setup

def rd(filename):
    f = open(filename)
    r = f.read()
    f.close()
    return r

version = re.findall(r"__version__ = \"(.*?)\"", open("patiencebar.py").read())[0]


setup(
    name="patiencebar",
    version=version,
    author="Guillaume Schworer",
    author_email="guillaume.schworer@obspm.fr",
    py_modules=["patiencebar"],
    url="https://github.com/ceyzeriat/patiencebar/",
    license="GNU",
    description="Terminal progress bar compatible with multi-threading",
    long_description=open("README.rst").read() + "\n\n"
                    + "Changelog\n"
                    + "---------\n\n"
                    + open("HISTORY.rst").read(),
    package_data={"": ["LICENSE", "AUTHORS.rst"]},
    include_package_data=True,
    install_requires=[],
    keywords = ['progress', 'bar', 'multi', 'threading', 'processing', 'multiprocessing', 'multithreading', 'terminal', 'command', 'line'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
    ],
)


# http://peterdowns.com/posts/first-time-with-pypi.html
