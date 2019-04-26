import asyncio
import time


def timed(fn, *args, **kwargs):
    name = fn.__name__
    count = 0
    before = time.time()
    duration = 0

    while duration < 1.0:
        count += 1
        if asyncio.iscoroutinefunction(fn):
            asyncio.run(fn(*args, **kwargs))
        else:
            fn(*args, **kwargs)
        duration = time.time() - before

    avg = duration / count
    if avg < 0.001:
        avg *= 1000000
        print(f"{count} runs of {name} in {duration:.1f}s: {avg:.2f} usec per run")
    elif avg < 0.1:
        avg *= 1000
        print(f"{count} runs of {name} in {duration:.1f}s: {avg:.2f} msec per run")
    else:
        print(f"{count} runs of {name} in {duration:.1f}s: {avg:.3f} sec per run")
    return count, duration

