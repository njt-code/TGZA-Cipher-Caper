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
# on stack exchange their is a FILTHY way to shorten this normalized 0 letter dictonary, I had it manually, just like the frequencies above. 
#journaling here basically, this below def is counting each item in the newly formed array, and setting up a frequency distribution, akin to the hard coded one above.
def getLetterCount(cipherText):
    letterCount = {ch: 0 for ch in LETTERS} #Blank table of Str A-Z set to 0
    letterTotal = 0 #Normalizes the per block freq to 0 each time
    for letter in cipherText:
        if letter in LETTERS: # loop counter, I know its inefficient, but freq analysis only loops 26 * keylength, so its quite efficient, and negligible
            letterCount[letter]+=1
            letterTotal += 1
    freq = {}
    for letter in LETTERS:
            freq[letter] = (letterCount[letter] / letterTotal) * 100 if letterTotal > 0 else 0 #this is the hard definition for transcribing the frequency, with 
  

def main():
    cipherText = input("Enter ciphertext for the vigrenre cipher: ").upper()
    cipherText = ''.join(filter(str.isalpha, cipherText)) #filtering punctuation, removing spaces, and changing all the characters to Upper case
    keyLength = int(input("Enter key length: "))


 # its non intuitive, that given IE pos 0 and you want to get the position N characters further in the string repeating to create groups, an obvious method exists
 # if you take the entire ciphertext length. and use the keylength as the modulous operator. it creates a very nice repeating loop, appending the corresponding characters to the correct group
 # using mod, with ie keyL 10, 1 mod 10 = 1, 2 mod 10 = 2... and repeats, 11 mod 10 = 1 again, 12 mod 10 = 2, very cleaver


    columns = [''] * keyLength # this creates empty string arrays, to store the new groups 
    for i, char in enumerate(cipherText): #char specifies just any character, the enumerate function
        columns[i % keyLength] += char
 
if __name__ == "__main__":
    main()