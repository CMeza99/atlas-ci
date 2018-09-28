# -*- coding: utf-8 -*-

"""CI module."""
from logging import Logger, getLogger
from typing import List, Optional, Any, Union
import glob
import os


_logger: Logger = getLogger(__name__)


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
    hcl_files: List[Union[Union[bytes, str], Any]] = list()

    if not path:
        path = os.getcwd()
    else:
        path = os.path.abspath(path)

    _logger.debug("Looking for HCL files in %s", path)

    if os.path.isdir(path):
        hcl_files = glob.glob(os.path.join(path, "*.hcl"))
        if not hcl_files:
            _logger.warning("No HCL files found at %s", path)
    else:
        _logger.error("This is not a valid/accessible path, %s", path)

    hcl_files.sort()

    if last_hcl:
        _logger.info("Not including hcl files after and including %s", last_hcl)
        hcl_files_tmp: List = list()
        for hcl_file in hcl_files:
            hcl_files_tmp.append(hcl_file)
            if last_hcl in hcl_file:
                break
        hcl_files = hcl_files_tmp

    return hcl_files
