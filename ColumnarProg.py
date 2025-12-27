import base64
import math
def encodeBase64(plaintext):
    return base64.b64encode(plaintext.encode('utf-8')).decode('utf-8')

def decodeBase64(encodedMsg):
    return base64.b64decode(encodedMsg.encode('utf-8')).decode('utf-8')

def padText(plaintext,key,pad='X'):
    keyLength = len(key)
    remainder = len(plaintext) % keyLength
    if remainder != 0:
        plaintext += pad * (keyLength - remainder)
    return plaintext

def getOrd(key):
    return sorted(range(len(key)), key=lambda x: key[x])

def encryptColumnar(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    plaintext = padText(plaintext, key)
    numOfColumns = len(key)
    numOfRows = len(plaintext) // numOfColumns + (len(plaintext) % numOfColumns != 0)
    grid = [['' for _ in range(numOfColumns)] for _ in range(numOfRows)]
    index = 0


    for r in range(numOfRows):
        for c in range(numOfColumns):
            if index < len(plaintext):
                grid[r][c] = plaintext[index]
                index += 1
    cipherText = ""

    order = getOrd(key)
    for k in order:
        for r in range(numOfRows):
            if grid[r][k] != '':
                cipherText += grid[r][k]

    return encodeBase64(cipherText)

def decryptColumnar(cipherText, key):
    cipherText = decodeBase64(cipherText)
    cipherText = cipherText.upper()
    numOfColumns = len(key)
    numOfRows = (len(cipherText) + numOfColumns - 1) // numOfColumns
    order = getOrd(key)
    filledCells = len(cipherText) % numOfColumns

    columnLength = [
        numOfRows if i < filledCells else numOfRows - 1
        for i in range(numOfColumns)
        ] if filledCells != 0 else [numOfRows] * numOfColumns

    grid = [['' for _ in range(numOfColumns)] for _ in range(numOfRows)]

    index = 0
    for n, c in enumerate(order):
        for r in range(columnLength[n]):
            if index < len(cipherText):
                grid[r][c] = cipherText[index]
                index += 1
    plaintext = ''.join(''.join(row) for row in grid)
    return plaintext
   
def main():
    ch = input("1. Encrypt Or 2. Decrypt: ").strip().upper()
    key = input("Enter Key: ").strip().upper()
    if ch == '1':
        plaintext = input("\nEnter Plaintext: ")
        print("Cipher = ", encryptColumnar(plaintext,key))
    elif ch == "2":
        cipherText = input("\nEnter Ciphertext: ")
        print("Plaintext: ",decryptColumnar(cipherText, key))
 
if __name__ == "__main__":
    main()