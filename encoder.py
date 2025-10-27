
# Usage: python3 encoder.py "PLAINTEXT" "KEY"

import sys
import math

def encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    num_cols = len(key)
    num_rows = math.ceil(len(plaintext) / num_cols)

    grid = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    index = 0
    for r in range(num_rows):
        for c in range(num_cols):
            if index < len(plaintext):
                grid[r][c] = plaintext[index]
                index += 1

    keyorder = sorted(list(key))

    ciphertext = ""
    for k in keyorder:
        col_index = key.index(k)
        for r in range(num_rows):
            if grid[r][col_index] != '':
                ciphertext += grid[r][col_index]

    return ciphertext

if len(sys.argv) < 3:
    print("Usage: python3 encoder.py \"PLAINTEXT\" \"KEY\"")
    sys.exit(1)

plaintext = sys.argv[1]
key = sys.argv[2]
output_file = "encodings.txt"

encodedtext = encrypt(plaintext, key)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(f"Key: {key}\n")
    f.write(f"Encoded: {encodedtext}\n")

print(f"Results saved to {output_file}")
