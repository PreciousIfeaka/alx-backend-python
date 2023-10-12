#!/usr/bin/env python3
"""This module creates a coroutine with an argument that determines the
    maximum delay of the coroutine
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
