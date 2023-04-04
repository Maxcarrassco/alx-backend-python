#!/usr/bin/env python3
"""ASYNC IO Module."""
import asyncio
import random
import time

async def wait_random(max_delay: int = 10) -> float:
    """Wait for a randow second and return the value."""
    wait_time = random.uniform(0, max_delay)
    time.sleep(wait_time)
    return wait_time
