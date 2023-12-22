#!/usr/bin/python3
import sys

def factorize(number):
    """Generate 2 factors for a given number."""
    factor1 = 2
    while number % factor1:
        if factor1 <= number:
            factor1 += 1

    factor2 = number // factor1
    return factor2, factor1

if len(sys.argv) != 2:
    sys.exit(f"Wrong usage: {sys.argv[0]} <file_path>")

filename = sys.argv[1]

try:
    with open(filename, 'r') as input_file:
        for line in input_file:
            number = int(line.rstrip())
            factor2, factor1 = factorize(number)
            print(f"{number} = {factor2} * {factor1}")
except FileNotFoundError:
    sys.exit(f"Error: File not found - {filename}")
except Exception as e:
    sys.exit(f"An error occurred: {e}")
