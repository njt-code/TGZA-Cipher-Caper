# Usage: python3 .\decryption\dSimple.py "CIPHERTEXT" "KEY"

import sys
import string


def substitution(ciphertext, key):
    key = key.upper()
    alphabet = string.ascii_uppercase
    mapping = {key[i]: alphabet[i] for i in range(26)}

    plaintext = ""
    for ch in ciphertext.upper():
        if ch.isalpha():
            plaintext += mapping.get(ch, ch)
        else:
            plaintext += ch
    return plaintext


def main(argv=None, output_file="decodings.txt"):
    if argv is None:
        argv = sys.argv
    if len(argv) < 3:
        print('Usage: python3 .\decryption\dSimple.py "CIPHERTEXT" "KEY"')
        sys.exit(1)

    ciphertext = argv[1]
    key = argv[2]

    decoded_text = substitution(ciphertext, key)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Key: {key}\n")
        f.write(f"Decoded: {decoded_text}\n")

    print(f"Results saved to {output_file}")


if __name__ == '__main__':
    main()
