#!/usr/bin/env python3

import os, sys, signal, itertools

chungus = open("chungus.txt").read()
chars = ('chunga', 'chunky', 'karen', 'big', 'fudd', 'chungus', 'ricardo')

def replace(A, B, C):
    for x, y in zip(B, C):
        A = A.replace(x, y)
    return A

def signal_handler(signum, frame):
    raise Exception("timeout")

signal.signal(signal.SIGALRM, signal_handler)

for counter, p in enumerate(itertools.permutations(chars)):
    if not (counter + 1) % 100:
        print("\n", counter + 1)
    else:
        print(".", end="")
        sys.stdout.flush()
    bf = replace(chungus, p, "+-><.[]")
    output = ""
    pos = 0         # Instruction
    array = {0:0}   # Cells
    current = 0     # Current cell, incremented with '>' and decremented with '<'
    signal.alarm(2) # Timeout of 2 seconds
    try:
        while pos < len(bf):

                # Current instruction
                inst = bf[pos]

                # Increment pointer
                if inst == "+":
                        if current not in array:
                                array[current] = 1
                        else:
                                array[current] += 1
                        array[current] %= 256 # Wrap around the ASCII table

                # Decrement pointer
                elif inst == "-":
                        if current not in array:
                                array[current] = -1
                        else:
                                array[current] -= 1
                        array[current] %= 256 # Wrap around the ASCII table

                # Next cell
                elif inst == ">":
                        current += 1
                        if current not in array:
                                array[current] = 0

                # Previous cell
                elif inst == "<":
                        current -= 1
                        if current not in array:
                                array[current] = 0

                # Output ASCII character of cell value
                elif inst == ".":
                        #sys.stdout.write(chr(array[current]))
                        output += chr(array[current])

                # Start loop
                elif inst == "[":
                        if array[current] == 0:
                                loops = 1
                                while loops:
                                        pos += 1
                                        if bf[pos] == "[":
                                                loops += 1
                                        elif bf[pos] == "]":
                                                loops -= 1

                # End loop
                elif inst == "]":
                        loops = 1
                        while loops:
                                pos -= 1
                                if bf[pos] == "[":
                                        loops -= 1
                                elif bf[pos] == "]":
                                        loops += 1
                        pos -= 1

                pos += 1
        if "HackTrinity" in output:
            exit("\n" + output)
    except Exception:
        signal.alarm(0) # Reset timeout
    except NameError:
        pass
