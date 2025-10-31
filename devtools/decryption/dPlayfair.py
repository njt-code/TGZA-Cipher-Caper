import itertools

def build_all_tables(limit=None):
   
    letters = [ch for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ"]
    all_perms = itertools.permutations(letters)

    count = 0
    for perm in all_perms:
        table = [perm[i:i+5] for i in range(0, 25, 5)]
        yield table
        count += 1
        if limit and count >= limit:
            break

def find_pos(table, letter):
    for r in range(5):
        for c in range(5):
            if table[r][c] == letter:
                return r, c
    return None, None

def playfair_decrypt(cipher, table):
    cipher = cipher.upper().replace('J', 'I')
    cipher = ''.join(ch for ch in cipher if ch.isalpha())

    if len(cipher) % 2 != 0:
        cipher += 'X'

    plaintext = ""
    for i in range(0, len(cipher), 2):
        a, b = cipher[i], cipher[i+1]
        ra, ca = find_pos(table, a)
        rb, cb = find_pos(table, b)

        if ra == rb:
            plaintext += table[ra][(ca - 1) % 5]
            plaintext += table[rb][(cb - 1) % 5]
        elif ca == cb:
            plaintext += table[(ra - 1) % 5][ca]
            plaintext += table[(rb - 1) % 5][cb]
        else:
            plaintext += table[ra][cb]
            plaintext += table[rb][ca]

    return plaintext

def main():
    print("Playfair Cipher Decryptor (Brute Force Mode)")
    ciphertext = input("Enter ciphertext: ").strip()
    try:
        limit = int(input("Enter how many table combinations to try (limit): ").strip())
    except ValueError:
        print("Invalid input for limit. Using 5 by default.")
        limit = 5

    output_file = "decodings.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        for i, table in enumerate(build_all_tables(limit=limit), start=1):
            decoded_text = playfair_decrypt(ciphertext, table)
            f.write(f"Decoded: {decoded_text}\n\n")

    print(f"\nResults saved to '{output_file}' (tested {limit} table permutations).")

if __name__ == '__main__':
    main()
