# Usage: python3 .\decryption\dAtbash.py "CIPHERTEXT"

import sys
import string


def atbash(ciphertext):
    a = string.ascii_uppercase
    r = a[::-1]
    mapping = {a[i]: r[i] for i in range(26)}

    plaintext = ""
    for ch in ciphertext.upper():
        if ch.isalpha():
            plaintext += mapping[ch]
        else:
            plaintext += ch
    return plaintext


def main(argv=None, output_file="decodings.txt"):
    if argv is None:
        argv = sys.argv
    if len(argv) < 2:
        print('Usage: python3 .\decryption\dAtbash.py "CIPHERTEXT"')
        sys.exit(1)

    ciphertext = argv[1]
    decoded_text = atbash(ciphertext)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Decoded: {decoded_text}\n")

    print(f"Results saved to {output_file}")


if __name__ == '__main__':
    main()
