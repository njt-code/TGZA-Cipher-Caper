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
#
def getLetterCount(cipherText):
    letterCount = {ch: 0 for ch in LETTERS} #Blank table of Str A-Z set to 0, didnt know but on stack exchange for dictonaries like this, you can actuall run for loops
    letterTotal = 0 # used in calculating the frequency
    for character in cipherText: # Char is temp variable, this loop default loops every character in a string until the string ends, and returns the chr value individually each loop to the new var
        if character in LETTERS: #the value of chr is assigned each loop, but before it overwrites, we check if its within the LETTERS string, if so, +1 to that location
            letterCount[character]+=1 
            letterTotal += 1
    freq = {} #blank dictonary, copying the chr and a modified frequency total by lettertotal
    for letter in LETTERS:
        if letterTotal > 0:
            freq[letter] = round((letterCount[letter] / letterTotal) * 100,3)
        else:
            freq[letter] = 0
    return freq, letterCount, letterTotal # returns 3 values, for manual testing, but it doesnt need to return all that besides freq


def main():
    cipherText = input("Enter ciphertext for the vigrenre cipher: ").upper()
    cipherText = ''.join(filter(str.isalpha, cipherText)) #filtering punctuation, removing spaces, and changing all the characters to Upper case
    keyLength = int(input("Enter key length: "))
 

    columns = [''] * keyLength # this creates an empty string array, to store the new groups 
    for i, char in enumerate(cipherText): # the enumerate function adds a number to the object being stored
        columns[i % keyLength] += char
    freq, count, total = getLetterCount(cipherText)
    print(freq, count, total) # Test case to show that its displaying frequencys



if __name__ == "__main__": #This is to stop the code from running when its imported into a program, and only will invoke the script when called upon manually
    main()