#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
import atlas_ci

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = []
setup_requirements = ["pytest-runner"]
test_requirements = ["pytest"]

setup(
    author=atlas_ci.__author__,
    author_email=atlas_ci.__email__,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
    ],
    description="Putting the Aye in Atlas",
    entry_points={
        "console_scripts": [
            "atlas_ci = atlas_ci.__main__:main"
        ]
    },
    install_requires=requirements,
    license="LGPLv3+",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="atlas_ci",
    name="atlas_ci",
    packages=find_packages(include=["atlas_ci"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/carlos.meza@everbridge.com/atlas_ci",
    version=atlas_ci.__version__,
    zip_safe=False,
)
