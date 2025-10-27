
# Usage: python3 dPlayfair.py "CIPHERTEXT" "KEYWORD"

import sys

def buildtable(key):
    key = key.upper().replace('J', 'I')
    table_letters = []
    
    
    for ch in key:
        if ch.isalpha() and ch not in table_letters:
            table_letters.append(ch)
    
   
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in table_letters:
            table_letters.append(ch)
    
    
    return [table_letters[i:i+5] for i in range(0, 25, 5)]

def findpos(table, letter):
    for r in range(5):
        for c in range(5):
            if table[r][c] == letter:
                return r, c
    return None, None

def playfair(cipher, key):
    table = buildtable(key)
    cipher = cipher.upper().replace('J', 'I')
    cipher = ''.join(ch for ch in cipher if ch.isalpha())
    
    # add filer if the text length is odd
    if len(cipher) % 2 != 0:
        cipher += 'X'
    
    plaintext = ""
    for i in range(0, len(cipher), 2):
        a, b = cipher[i], cipher[i+1]
        ra, ca = findpos(table, a)
        rb, cb = findpos(table, b)
        
        if ra == rb:
            # Same row: move left
            plaintext += table[ra][(ca - 1) % 5]
            plaintext += table[rb][(cb - 1) % 5]
        elif ca == cb:
            # Same column: move up
            plaintext += table[(ra - 1) % 5][ca]
            plaintext += table[(rb - 1) % 5][cb]
        else:
            # Rectangle: swap columns
            plaintext += table[ra][cb]
            plaintext += table[rb][ca]
    
    return plaintext

if len(sys.argv) < 3:
    print("Usage: python3 dPlayfair.py \"CIPHERTEXT\" \"KEYWORD\"")
    sys.exit(1)

ciphertext = sys.argv[1]
key = sys.argv[2]
output_file = "decodings.txt"

decoded_text = playfair(ciphertext, key)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(f"Key: {key}\n")
    f.write(f"Decoded: {decoded_text}\n")

print(f"Results saved to {output_file}")
