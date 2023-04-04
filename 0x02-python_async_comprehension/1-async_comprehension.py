#!/usr/bin/env python3
"""ASYNC Comprehension Module."""
from typing import Iterable
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Iterable[float]:
    """Return a list of values from async_genrator."""
    return [val async for val in async_generator()]
