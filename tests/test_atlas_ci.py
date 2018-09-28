#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=no-self-use, line-too-long

"""Tests for `atlas_ci` package."""

import unittest
from typing import List

import atlas_ci


class TestAtlasCi(unittest.TestCase):
    """Tests for `atlas_ci` package."""

    data_path: str = "./tests/data"

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_get_hcl_files(self):
        """Test atlas_ci.get_hcl_files()."""

        assert (
            len(atlas_ci.ci.get_hcl_files(".")) == 0  # pylint: disable=len-as-condition
        )

    def test_001_get_hcl_files(self):
        """Test atlas_ci.get_hcl_files."""

        hcl_files: List[str] = [
            "/home/digitalr00ts/Documents/git/cookie.experiments/atlas-ci/tests/data/0-system.hcl",
            "/home/digitalr00ts/Documents/git/cookie.experiments/atlas-ci/tests/data/01-shared-buckets.hcl",
            "/home/digitalr00ts/Documents/git/cookie.experiments/atlas-ci/tests/data/1-shared-stack.hcl",
            "/home/digitalr00ts/Documents/git/cookie.experiments/atlas-ci/tests/data/1.1.1-shared-stack-extra.hcl",
            "/home/digitalr00ts/Documents/git/cookie.experiments/atlas-ci/tests/data/2-test-stack.hcl",
            "/home/digitalr00ts/Documents/git/cookie.experiments/atlas-ci/tests/data/2.2.1-test-stack-component2.hcl",
            "/home/digitalr00ts/Documents/git/cookie.experiments/atlas-ci/tests/data/2.2.2-test-stack-component2.hcl",
        ]

        assert atlas_ci.ci.get_hcl_files(self.data_path) == hcl_files

    def test_002_get_hcl_files(self):
        """Test atlas_ci.get_hcl_files w/ last_hcl."""

        hcl_files: List[str] = [
            "/home/digitalr00ts/Documents/git/cookie.experiments/atlas-ci/tests/data/0-system.hcl",
            "/home/digitalr00ts/Documents/git/cookie.experiments/atlas-ci/tests/data/01-shared-buckets.hcl",
            "/home/digitalr00ts/Documents/git/cookie.experiments/atlas-ci/tests/data/1-shared-stack.hcl",
            "/home/digitalr00ts/Documents/git/cookie.experiments/atlas-ci/tests/data/1.1.1-shared-stack-extra.hcl",
            "/home/digitalr00ts/Documents/git/cookie.experiments/atlas-ci/tests/data/2-test-stack.hcl",
            "/home/digitalr00ts/Documents/git/cookie.experiments/atlas-ci/tests/data/2.2.1-test-stack-component2.hcl",
        ]

        assert atlas_ci.ci.get_hcl_files(self.data_path, "2.2.1") == hcl_files
