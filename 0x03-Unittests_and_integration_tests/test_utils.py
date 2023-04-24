#!/usr/bin/env python3
"""Utils Unittest Module."""
import unittest
from parameterized import parameterized
from typing import Sequence, Mapping
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Implement all unittest cases for utils."""

    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
            ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected):
        """Test if access nested map return the rightful output."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a", )),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map: Mapping, path: Sequence):
        """Check if exception is being raise if wrong argument are pass."""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
