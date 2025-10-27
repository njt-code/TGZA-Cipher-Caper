
# Usage: python3 dBase.py "QmFzZTY0IGlzIGNvb2wh"

import sys
import base64

def base64(text):
    try:
        decodedbytes = base64.b64decode(text)
        return decodedbytes.decode('utf-8', errors='ignore')
    except Exception:
        return "Invalid Base64 input."


if len(sys.argv) < 2:
    print("Usage: python3 dBase.py \"CIPHERTEXT\"")
    sys.exit(1)

ciphertext = sys.argv[1]
outputfile = "decodings.txt"

decodedtext = base64(ciphertext)

with open(outputfile, "w", encoding="utf-8") as f:
    f.write(f"Decoded: {decodedtext}\n")

print(f"Results saved to {outputfile}")
