# Usage: python3 .\decryption\dColumnar.py "CIPHERTEXT" "KEY"

import sys
import math

def decryptcolumnar(ciphertext, key):
    ciphertext = ciphertext.replace(" ", "").upper()
    num_cols = len(key)
    num_rows = math.ceil(len(ciphertext) / num_cols)
    key_order = sorted(list(key))

    
    cols = [''] * num_cols
    col_lengths = [num_rows] * num_cols
    extra = num_cols * num_rows - len(ciphertext)
    for i in range(extra):
        col_lengths[key_order.index(key[i])] -= 1

   
    index = 0
    for k in key_order:
        col_index = key.index(k)
        length = col_lengths[key_order.index(k)]
        cols[col_index] = list(ciphertext[index:index + length])
        index += length

    
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
        print('Usage: python3 .\decryption\dColumnar.py "CIPHERTEXT" "KEY"')
        sys.exit(1)

    ciphertext = argv[1]
    key = argv[2]

    decodedtext = decryptcolumnar(ciphertext, key)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Key: {key}\n")
        f.write(f"Decoded: {decodedtext}\n")

    print(f"Results saved to {output_file}")


if __name__ == '__main__':
    main()
