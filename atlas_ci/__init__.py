# -*- coding: utf-8 -*-

"""Top-level package for Atlas CI."""

import logging

# import sys

from .__version__ import (
    __title__,
    __description__,
    __url__,
    __version__,
    __author__,
    __author_email__,
    __license__,
    __copyright__,
)

# from . import *  # pylint: disable=wildcard-import
from . import ci


logging.getLogger(__name__).addHandler(logging.NullHandler())
