# Usage: python3 dColumnar.py "CIPHERTEXT" "KEY"

import sys
import math

def decryptcolumnar(ciphertext, key):
    ciphertext = ciphertext.replace(" ", "").upper()
    num_cols = len(key)
    num_rows = math.ceil(len(ciphertext) / num_cols)
    key_order = sorted(list(key))

    # Determine length of each column
    col_lengths = [num_rows] * num_cols
    total_cells = num_cols * num_rows
    extra = total_cells - len(ciphertext)
    # Reduce extra cells from the rightmost columns in sorted order
    if extra > 0:
        for i in range(extra):
            col_index = key.index(key_order[-(i+1)])
            col_lengths[col_index] -= 1

    # Fill columns
    cols = [''] * num_cols
    index = 0
    for k in key_order:
        col_index = key.index(k)
        length = col_lengths[col_index]
        cols[col_index] = list(ciphertext[index:index + length])
        index += length

    # Read rows to get plaintext
    plaintext = ""
    for r in range(num_rows):
        for c in range(num_cols):
            if r < len(cols[c]):
                plaintext += cols[c][r]

    return plaintext

def main(argv=None, output_file="decodings.txt"):
    if argv is None:
        argv = sys.argv
    if len(argv) < 3:
        print('Usage: python3 dColumnar.py "CIPHERTEXT" "KEY"')
        return None  # instead of sys.exit()

    ciphertext = argv[1]
    key = argv[2]

    decodedtext = decryptcolumnar(ciphertext, key)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Key: {key}\n")
        f.write(f"Decoded: {decodedtext}\n")

    print(f"Results saved to {output_file}")
    return decodedtext  # return the decoded text for programmatic use

if __name__ == '__main__':
    main()
