# -*- coding: utf-8 -*-

"""Main module."""
from typing import List, Optional, Any, Union
import logging
import glob
import os
import sys

_LOGGER = logging.getLogger(__package__)


def _config_logging(
    console_loglevel: Optional[str] = None,
    file_loglevel: Optional[str] = None,
    log_file: Optional[str] = None,
) -> None:
    """
    Configure logging

    Parameters
    ----------
    console_loglevel: str, optional
        Set console log level (Default: warning)
    file__loglevel: str, optional
        Set file log level (Default: debug)
    log_file: str, optional
        Name of log file. By default there is not fileHandler for logging
    """

    if console_loglevel is None:
        console_loglevel = logging.WARNING
    log_format: str = "%(levelname)s: %(message)s"

    logging.basicConfig(stream=sys.stderr, level=console_loglevel, format=log_format)

    if log_file:
        log_formatter: logging.Formatter = logging.Formatter(
            "[%(asctime)s:%(levelname)-7s:%(name)s.%(module)s:%(lineno)d] %(message)s"
        )
        filehandler: logging.FileHandler = logging.FileHandler(log_file)
        if not file_loglevel:
            filehandler.setLevel(logging.DEBUG)
        else:
            filehandler.setLevel(file_loglevel)
        filehandler.setFormatter(log_formatter)
        _LOGGER.addHandler(filehandler)


def get_hcl_files(
    path: Optional[str] = None, last_hcl: Optional[str] = None
) -> List[Union[Union[bytes, str], Any]]:
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

    _LOGGER.debug("Looking for HCL files in %s", os.path.abspath(path))
    hcl_files: List[Union[Union[bytes, str], Any]] = glob.glob(
        os.path.join(path, "*.hcl")
    )

    hcl_files.sort()

    if last_hcl:
        hcl_files_tmp: List = list()
        for hcl_file in hcl_files:
            hcl_files_tmp.append(hcl_file)
            if last_hcl in hcl_file:
                _LOGGER.debug(
                    "Not including hcl files after and including %s", last_hcl
                )
                break

    return sorted(hcl_files)


def main():
    """Main entry point"""
    _config_logging(log_file=".".join([__package__, "log"]))


if __name__ == "__main__":
    main()
