#This program uses frequency analysis of english characters, along with key-length, to break the vigrenete cipher. or get as close to plain english as possible
#The idea is you compare the two frequency distributions, and shift/guess the letter to the corresponding peak, E of 12.7 here, most common letter, will have the 
#highest peak in the new distribution
from collections import Counter
engFreq = {
     'A': 8.2,'B': 1.5,  'C' : 2.8,  'D' : 4.3 , 'E' : 12.7, 'F' : 2.2, 'G' : 2.0, 'H' : 6.1,
     'I' : 7.0, 'J' : 0.15, 'K' : 0.77,  'L' : 4.0, 'M' : 2.4, 'N' : 6.7, 'O' : 7.5, 'P' : 1.9,
     'Q' : 0.095, 'R' : 6.0 , 'S' : 6.3, 'T' : 9.1, 'U' : 2.8, 'V' : 0.98, 'W' : 2.4, 'X' : 0.15,
     'Y' : 2.0, 'Z' : 0.074 
}
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# on stack exchange their is a FILTHY way to shorten this normalized 0 letter dictonary, Didnt know you can use for loops nested in array defs
def getLetterCount(cipherText):
    letterCount = {ch: 0 for ch in LETTERS} #Blank table of Str A-Z set to 0
    letterTotal = 0 #Normalizes the per block freq to 0
    for character in cipherText: 
        if character in LETTERS: 
            letterCount[character]+=1 
            letterTotal += 1
    freq = {} #blank dictonary, copying the chr and a modified frequency total by lettertotal
    for letter in LETTERS:
        if letterTotal > 0:
            freq[letter] = round((letterCount[letter] / letterTotal) * 100,3)
        else:
            freq[letter] = 0
    return freq, letterCount, letterTotal
def chiVal(freq):
    return 

def main():
    cipherText = input("Enter ciphertext for the vigrenre cipher: ").upper()
    cipherText = ''.join(filter(str.isalpha, cipherText)) #filtering punctuation, removing spaces, and changing all the characters to Upper case
    keyLength = int(input("Enter key length: "))


    columns = [''] * keyLength # this creates an empty string array, to store the new groups 
    for i, char in enumerate(cipherText): # the enumerate function adds a number to the object being stored, making it a tuple, because we need to preform freq analsys on certain elements in this array
        columns[i % keyLength] += char
    freq, count, total = getLetterCount(cipherText)
    print(freq, count, total)



 

if __name__ == "__main__":
    main()