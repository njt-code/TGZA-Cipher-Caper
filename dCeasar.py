#how to use:- python3 dCeasar.py "Encoded message"

import sys

def caesar(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base - shift) % 26 + base)
        else:
            result += ch
    return result

text = sys.argv[1] if len(sys.argv) > 1 else ""
outfile = "decodings.txt"

with open(outfile, "w", encoding="utf-8") as f:
    for shift in range(26):
        decoded = caesar(text, shift)
        f.write(f"Shift {shift}: {decoded}\n")

print(f"Results saved to {outfile}")
