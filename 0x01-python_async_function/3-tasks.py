#!/usr/bin/env python3
"""ASYNC IO Module."""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """Create and return a task using wait_random."""
    return asyncio.create_task(wait_random(max_delay))
