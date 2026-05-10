import argparse
from functools import lru_cache


def parse_args(argv):
    p = argparse.ArgumentParser(prog="fib-tools")
    p.add_argument("n", type=int)
    p.add_argument("--seq", action="store_true")
    return p.parse_args(argv)


@lru_cache(maxsize=None)
def _fib(n: int) -> int:
    if n < 2:
        return n
    return _fib(n - 1) + _fib(n - 2)


def run_command(args):
    if args.seq:
        return [_fib(i) for i in range(args.n)]
    return _fib(args.n)
