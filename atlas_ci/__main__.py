# -*- coding: utf-8 -*-

"""Main module."""

from typing import List, Optional, Any, Union
import logging
import glob
import os

_LOGGER = logging.getLogger(__name__)


def get_hcl_files(path: Optional[str] = None) -> List[Union[Union[bytes, str], Any]]:
    """
    Get sorted list of hcl files from a directory.

    Parameters
    ----------
    path : str, optional
        Path to look for hcl files. Will use current working directory if no value is supplied.

    Returns
    -------
    list
        Sorted list of hcl files.
    """

    if not path:
        path = os.getcwd()

    hcl_files: List[Union[Union[bytes, str], Any]] = glob.glob(
        os.path.join(path, "*.hcl")
    )

    return sorted(hcl_files)


def main():
    """Command line entry point"""
    pass


if __name__ == "__main__":
    main()
