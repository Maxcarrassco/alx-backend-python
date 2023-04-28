#!/usr/bin/env python3
"""Client Unittest Module."""
from parameterized import parameterized
from client import GithubOrgClient
import unittest
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """Implement all test cases for org function from the client script."""

    @parameterized.expand([
        'google',
        'abc'
        ])
    @patch('client.get_json')
    def test_org(self, org: str, mock_get_json):
        """Test if org method from GithubOrgClient return the right output."""
        expect = {
                "repo_url": f"https://api.github.com/orgs/{org}"
                }
        mock_get_json.return_value = expect
        git_org = GithubOrgClient(org)
        self.assertAlmostEqual(git_org.org, expect)
