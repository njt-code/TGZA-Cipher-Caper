# how to use: .\decryption\dpython3 dCeasar.py "Encoded message"

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


def main(argv=None, outfile="decodings.txt"):
    
    if argv is None:
        argv = sys.argv
    text = argv[1] if len(argv) > 1 else ""

    with open(outfile, "w", encoding="utf-8") as f:
        for shift in range(26):
            decoded = caesar(text, shift)
            f.write(f"Shift {shift}: {decoded}\n")

    print(f"Results saved to {outfile}")


if __name__ == '__main__':
    main()
