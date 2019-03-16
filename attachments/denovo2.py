#!/usr/bin/env python3

encrypted_flag = '''
0000000000400d40         db  0x1b ; '.'                                     
0000000000400d41         db  0x32 ; '2'
0000000000400d42         db  0x30 ; '0'
0000000000400d43         db  0x38 ; '8'
0000000000400d44         db  0x07 ; '.'
0000000000400d45         db  0x21 ; '!'
0000000000400d46         db  0x3a ; ':'
0000000000400d47         db  0x3d ; '='
0000000000400d48         db  0x3a ; ':'
0000000000400d49         db  0x27 ; '\''
0000000000400d4a         db  0x2a ; '*'
0000000000400d4b         db  0x28 ; '('
0000000000400d4c         db  0x3b ; ';'
0000000000400d4d         db  0x63 ; 'c'
0000000000400d4e         db  0x24 ; '$'
0000000000400d4f         db  0x0c ; '.'
0000000000400d50         db  0x37 ; '7'
0000000000400d51         db  0x3c ; '<'
0000000000400d52         db  0x0c ; '.'
0000000000400d53         db  0x62 ; 'b'
0000000000400d54         db  0x0c ; '.'
0000000000400d55         db  0x38 ; '8'
0000000000400d56         db  0x3d ; '='
0000000000400d57         db  0x1c ; '.'
0000000000400d58         db  0x24 ; '$'
0000000000400d59         db  0x0c ; '.'
0000000000400d5a         db  0x27 ; '\''
0000000000400d5b         db  0x3b ; ';'
0000000000400d5c         db  0x60 ; '`'
0000000000400d5d         db  0x0c ; '.'
0000000000400d5e         db  0x35 ; '5'
0000000000400d5f         db  0x3f ; '?'
0000000000400d60         db  0x13 ; '.'
0000000000400d61         db  0x34 ; '4'
0000000000400d62         db  0x0c ; '.'
0000000000400d63         db  0x62 ; 'b'
0000000000400d64         db  0x20 ; ' '
0000000000400d65         db  0x0c ; '.'
0000000000400d66         db  0x21 ; '!'
0000000000400d67         db  0x62 ; 'b'
0000000000400d68         db  0x14 ; '.'
0000000000400d69         db  0x3b ; ';'
0000000000400d6a         db  0x27 ; '\''
0000000000400d6b         db  0x2e ; '.'
'''

# Extract the hex part from the dissassembled string
encrypted_flag = "".join(x[31:33] for x in encrypted_flag.split("\n"))

# Bitwise XOR each byte with 83 and convert to string
flag = "".join(chr(x ^ 83) for x in bytes.fromhex(encrypted_flag))

# Print the results
print(f"Encrypted flag: {encrypted_flag}\nFlag: {flag}")
