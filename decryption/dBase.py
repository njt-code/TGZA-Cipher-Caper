# Usage: python3 .\decryption\dBase.py "QmFzZTY0IGlzIGNvb2wh"

import sys
import base64


def decode_base64(text):
    try:
        decodedbytes = base64.b64decode(text)
        return decodedbytes.decode('utf-8', errors='ignore')
    except Exception:
        return "Invalid Base64 input."


def main(argv=None, outputfile="decodings.txt"):
    if argv is None:
        argv = sys.argv
    if len(argv) < 2:
        print('Usage: python3 .\decryption\dBase.py "CIPHERTEXT"')
        sys.exit(1)

    ciphertext = argv[1]
    decodedtext = decode_base64(ciphertext)

    with open(outputfile, "w", encoding="utf-8") as f:
        f.write(f"Decoded: {decodedtext}\n")

    print(f"Results saved to {outputfile}")


if __name__ == '__main__':
    main()
