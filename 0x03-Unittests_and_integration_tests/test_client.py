#!/usr/bin/env python3
"""Client Unittest Module."""
from parameterized import parameterized
from client import GithubOrgClient
import unittest
from unittest.mock import patch, Mock


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

    def test_public_repos_url(self):
        """Test if org method from GithubOrgClient return the right output."""
        with patch.object(GithubOrgClient,
                          '_public_repos_url') as mock_public_repos_url:
            expect = 'https://api.github.com/orgs/google/repos'
            git_org = GithubOrgClient('google')
            mock_public_repos_url.__get__ = Mock(return_value=expect)
            self.assertEqual(git_org._public_repos_url, expect)
