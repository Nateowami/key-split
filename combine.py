#!/usr/bin/env python3
import sys

a = bytes.fromhex(sys.argv[1])
b = bytes.fromhex(sys.argv[2])

print(bytes(x ^ y for x, y in zip(a, b)).decode())
