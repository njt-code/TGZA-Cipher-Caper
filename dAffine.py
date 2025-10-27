
# Usage: python3 dAffine.py "CIPHERTEXT" a b

import sys
import string

def inverse(a, m):

    for i in range(m):
        if (a * i) % m == 1:
            return i
    return None  

def decrypt_affine(ciphertext, a, b):
    alphabet = string.ascii_uppercase
    m = 26
    ainv = inverse(a, m)
    if ainv is None:
        return "Invalid 'a' value."

    plaintext = ""
    for ch in ciphertext.upper():
        if ch.isalpha():

            cval = ord(ch) - ord('A')
            pval = (ainv * (cval - b)) % m
            plaintext += chr(pval + ord('A'))
        else:
            plaintext += ch
    return plaintext

if len(sys.argv) < 4:
    print("Usage: python3 dAffine.py \"CIPHERTEXT\" a b")
    sys.exit(1)


ciphertext = sys.argv[1]
a = int(sys.argv[2])
b = int(sys.argv[3])

outputfile = "decodings.txt"


with open(outputfile, "w", encoding="utf-8") as f:
    f.write(f"a: {a}, b: {b}\n")
    f.write(f"Decoded: {decrypt_affine(ciphertext, a, b)}\n")

print(f"Results saved to {outputfile}")
