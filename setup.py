#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name

"""The setup script."""

import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, "atlas_ci", "__version__.py"), "r") as f:
    exec(f.read(), about)  # pylint: disable=exec-used

with open("README.rst", "r") as f:
    readme = f.read()
with open("HISTORY.rst", "r") as f:
    history = f.read()

requirements = []
setup_requirements = ["pytest-runner"]
test_requirements = ["pytest"]

setup(
    author=about["__author__"],
    author_email=about["__author_email__"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
    ],
    description=about["__description__"],
    entry_points={"console_scripts": ["atlas_ci = atlas_ci.__main__:main"]},
    install_requires=requirements,
    license="LGPLv3+",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords="atlas_ci",
    name=about["__title__"],
    packages=find_packages(include=["atlas_ci"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url=about["__url__"],
    version=about["__version__"],
    zip_safe=False,
)
