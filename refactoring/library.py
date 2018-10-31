#!/usr/bin/env python3

import asyncio
import time


def anxiety(source: str, count: int = 3) -> None:
    while count > 0:
        print(f"thinking about {source}...")
        time.sleep(0.2)
        count -= 1


def despair() -> None:
    time.sleep(2)  # what can you do?
