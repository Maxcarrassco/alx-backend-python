#!/usr/bin/env python3
"""ASYNC Comprehension Module."""
import asyncio
import random
from typing import AsyncIterator


async def async_generator() -> AsyncIterator[float]:
    """Return a generator that yield a random value between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
