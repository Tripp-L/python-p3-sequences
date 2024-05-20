#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    
    fibonocci_sequence = [0, 1]
    while len(fibonocci_sequence) < length:
        fibonocci_sequence.append(fibonocci_sequence[-1] + fibonocci_sequence[-2])
        
    print(fibonocci_sequence)