import subprocess
import sys

def run_encoder():
    plaintext = input("\nEnter plaintext: ").strip()
    key = input("Enter key (≤7 unique letters): ").strip()
    # Call the encoder file using subprocess
    subprocess.run([sys.executable, ".\console\encoder.py", plaintext, key])

def run_decoder():
    ciphertext = input("\nEnter ciphertext: ").strip()
    key = input("Enter key (≤7 unique letters): ").strip()
    # Call the decoder file using subprocess
    subprocess.run([sys.executable, ".\console\decoder.py", ciphertext, key])

def main_menu():
    print("=== Columnar Transposition Cipher Launcher ===")
    while True:
        print("\n1) Encode text")
        print("2) Decode text")
        print("3) Exit")
        choice = input("Select option (1/2/3): ").strip()
        if choice == "1":
            run_encoder()
        elif choice == "2":
            run_decoder()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
