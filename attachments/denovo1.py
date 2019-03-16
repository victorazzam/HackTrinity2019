#!/usr/bin/env python3

shifted_serial = '''
0000000000400d00         db  0x96 ; '.'
0000000000400d01         db  0x9e ; '.'
0000000000400d02         db  0x86 ; '.'
0000000000400d03         db  0xb0 ; '.'
0000000000400d04         db  0xb4 ; '.'
0000000000400d05         db  0x8c ; '.'
0000000000400d06         db  0x5a ; 'Z'
0000000000400d07         db  0xac ; '.'
0000000000400d08         db  0x88 ; '.'
0000000000400d09         db  0x96 ; '.'
0000000000400d0a         db  0xaa ; '.'
0000000000400d0b         db  0x94 ; '.'
0000000000400d0c         db  0xae ; '.'
0000000000400d0d         db  0x5a ; 'Z'
0000000000400d0e         db  0x88 ; '.'
0000000000400d0f         db  0x9c ; '.'
0000000000400d10         db  0xa4 ; '.'
0000000000400d11         db  0x86 ; '.'
0000000000400d12         db  0xac ; '.'
0000000000400d13         db  0x8a ; '.'
0000000000400d14         db  0x5a ; 'Z'
0000000000400d15         db  0x8c ; '.'
0000000000400d16         db  0x9c ; '.'
0000000000400d17         db  0x8e ; '.'
0000000000400d18         db  0x9c ; '.'
0000000000400d19         db  0xa8 ; '.'
0000000000400d1a         db  0xb4 ; '.'
0000000000400d1b         db  0x5a ; 'Z'
0000000000400d1c         db  0xb0 ; '.'
0000000000400d1d         db  0xb4 ; '.'
0000000000400d1e         db  0x86 ; '.'
0000000000400d1f         db  0x8e ; '.'
0000000000400d20         db  0xac ; '.'
0000000000400d21         db  0xb0 ; '.'
'''

shifted_flag = '''
0000000000400dc0         db  0xdc ; '.'
0000000000400dc1         db  0x60 ; '`'
0000000000400dc2         db  0xbe ; '.'
0000000000400dc3         db  0xc8 ; '.'
0000000000400dc4         db  0xe4 ; '.'
0000000000400dc5         db  0xda ; '.'
0000000000400dc6         db  0xbe ; '.'
0000000000400dc7         db  0x62 ; 'b'
0000000000400dc8         db  0xe6 ; '.'
0000000000400dc9         db  0xbe ; '.'
0000000000400dca         db  0xea ; '.'
0000000000400dcb         db  0x9c ; '.'
0000000000400dcc         db  0x84 ; '.'
0000000000400dcd         db  0xe4 ; '.'
0000000000400dce         db  0xca ; '.'
0000000000400dcf         db  0x82 ; '.'
0000000000400dd0         db  0xd6 ; '.'
0000000000400dd1         db  0xc2 ; '.'
0000000000400dd2         db  0xc4 ; '.'
0000000000400dd3         db  0xd8 ; '.'
0000000000400dd4         db  0xca ; '.'
'''

# Extract the hex part from the dissassembled strings
shifted_serial = "".join(x[31:33] for x in shifted_serial.split("\n"))
shifted_flag = "".join(x[31:33] for x in shifted_flag.split("\n"))

# Bitwise right-shift once and convert to string
serial = bytes.fromhex(hex(int(shifted_serial, 16) >> 1)[2:]).decode()
flag = bytes.fromhex(hex(int(shifted_flag, 16) >> 1)[2:]).decode()

# Print the results
print(f"Shifted serial: {shifted_serial}\nShifted flag: {shifted_flag}")
print(f"Serial: {serial}\nFlag: {flag}")
