#!/usr/bin/env python3

from Crypto.Cipher import ARC4

of = (8432,) + (8326,) * 13 + (8354,)
sz = (4510072, 4493688, 4477304, 4460920, 4444536, 4428152, 4411768, 4395384, 4379000, 4362616, 4346232, 4329848, 4313464, 4296984, 4282216)
chars, key, data = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "", open("denovo_v3", "rb").read()

for layer in range(15):
    offset, size = of[layer], sz[layer]
    data = data[offset:offset+size]
    for guess in (x + y for x in chars for y in chars):
        serial = (key + guess).ljust(30, "0")
        enc = ARC4.new("-".join(serial[x:x+6] for x in (0,6,12,18,24)).encode())
        if enc.decrypt(data[:4]) == b"\x7fELF":
            data = b"\x7fELF" + enc.decrypt(data[4:])
            key += guess
            break

with open("denovo_v3_cracked", "wb") as f:
    f.write(data)
    print(f'Cracked into \033[1;7;91m denovo_v3_cracked \033[m using key \033[1;7;91m {"-".join(key[x:x+6] for x in (0,6,12,19,24))} \033[m')
