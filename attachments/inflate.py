#!/usr/bin/env python3

import sys, zlib

try:
    with open(sys.argv[1], "rb") as f:
        data = f.read()
    start = int(sys.argv[2], 16)
    end = int(sys.argv[3], 16)
    payload = data[start:end]
    print(zlib.decompress(payload, -15).decode().strip())
    # Thanks to https://stackoverflow.com/q/1089963
except (IndexError, ValueError):
    exit(f"Usage: {sys.argv[0]} file start end\nNote: start and end must be in 0x HEX format.")
