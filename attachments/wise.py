import sys, socket

a = ("No?", "He could actually save people from death?", "What happened to him?", "Is it possible to learn this power?", "Senator, what's this I've found?")

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((sys.argv[1], 66))
    print("\nPalpatine: " + s.recv(1000).decode())
    for i in a:
        print("\nAnakin: " + i)
        s.send(i.encode())
        print("\nPalpatine: " + s.recv(1000).decode())
    s.close()
except IndexError:
    exit("Usage: python wise.py server_ip")
except (KeyboardInterrupt, EOFError):
    pass

print()
