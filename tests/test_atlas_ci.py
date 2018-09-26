#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `atlas_ci` package."""

import unittest
import atlas_ci.__main__


class TestAtlasCi(unittest.TestCase):
    """Tests for `atlas_ci` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_get_hcl_files(self):
        """Test atlas_ci.get_hcl_files()."""

        assert len(atlas_ci.__main__.get_hcl_files(".")) == 0

    def test_001_get_hcl_files(self):
        """Test atlas_ci.get_hcl_files('/InvalidPath')."""

        atlas_ci.__main__.get_hcl_files("/InvalidPath")
        # FileNotFoundError: [Errno 2] No such file or directory: '/InvalidPath'

    def test_002_get_hcl_files(self):
        """Test atlas_ci.get_hcl_files('./data')."""

        atlas_ci.__main__.get_hcl_files("./data")
