#!/usr/bin/env python3
import os, sys

s = sys.argv[1].encode()
r = os.urandom(len(s))
x = bytes(a ^ b for a, b in zip(s, r))

print(r.hex())
print(x.hex())
