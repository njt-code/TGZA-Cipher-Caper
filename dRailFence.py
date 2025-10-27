
# Usage: python3 railfence_decoder.py "CIPHERTEXT" 3

import sys

def railfence(ciphertext, rails):
    
    n = len(ciphertext)
    rail_pattern = [[None] * n for _ in range(rails)]

    
    row, step = 0, 1
    for i in range(n):
        rail_pattern[row][i] = '*'
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        row += step


    index = 0
    for r in range(rails):
        for c in range(n):
            if rail_pattern[r][c] == '*' and index < n:
                rail_pattern[r][c] = ciphertext[index]
                index += 1

    # Read zigzag to get plaintext
    result = []
    row, step = 0, 1
    for i in range(n):
        result.append(rail_pattern[row][i])
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        row += step

    return ''.join(result)

# --- MAIN PROGRAM ---

if len(sys.argv) < 3:
    print("Usage: python3 railfence_decoder.py \"CIPHERTEXT\" <RAILS>")
    sys.exit(1)

ciphertext = sys.argv[1]
rails = int(sys.argv[2])
output_file = "decodings.txt"

decoded_text =railfence(ciphertext, rails)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(f"Rails: {rails}\n")
    f.write(f"Decoded: {decoded_text}\n")

print(f"Results saved to {output_file}")
