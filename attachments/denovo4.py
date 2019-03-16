#!/usr/bin/env python3

import sys
from time import sleep
from struct import pack, unpack

def xor(what, key, amount=None):
	amount = amount if amount else len(what)
	return b"".join(bytes([what[i] ^ key]) for i in range(amount))

def parse(eso):
	num = unpack(">H", eso[9:11])[0]
	ptr = eso.find(b".data")
	sections = []
	for n in range(num):
		name = eso[ptr:ptr + eso[ptr:].find(b"\x00") + 1]
		ptr += len(name)
		zero = unpack("?", eso[ptr:ptr+1])[0]
		ptr += 1
		size = unpack(">I", eso[ptr:ptr+4])[0] * (not zero)
		ptr += 4
		sections.append((name[:-1], size))
	for s in sections:
		if s[0] == b".layer":
			layer = eso[ptr:ptr+s[1]]
		elif s[0] == b".s_offset":
			offset = unpack(">I", eso[ptr:ptr+s[1]])[0]
		ptr += s[1]
	return layer, offset

print("\033[?25l", end="") # Hide cursor

try:
	with open("denovo_v4", "rb") as f:
		layer = f.read()[0x4080:0x7b40]
	serial = bytearray(b"-".join([b"0" * 6] * 5))
	while b"0" in serial:
		count = abs(serial.count(b"0") - 30)
		layer, offset = parse(layer)
		found = 0
		for c in b"QWERTYUIOPASDFGHJKLZXCVBNM":
			serial[offset] = c
			tmp = serial.decode()
			print(f"Serial key: {tmp[:offset]}\033[1;92m{tmp[offset]}\033[m{tmp[offset+1:]}", end="\r")
			sys.stdout.flush()
			sleep(0.03)
			if xor(layer, c, 3) == b"ESO":
				layer = xor(layer, c)
				found = 1
				break
		else:
			exit("That didn't work :/")
	with open(f"denovo_v4.eso", "wb") as f:
		f.write(layer)
	print(f"Serial key: {tmp}")
except (KeyboardInterrupt, EOFError):
	print()

print("\033[?25h", end="") # Show cursor