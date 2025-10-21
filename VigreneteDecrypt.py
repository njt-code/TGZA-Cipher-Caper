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
def getLetterCount(cipherText):
    letterCount = {ch: 0 for ch in LETTERS} #Blank table of Str A-Z set to 0
    letterTotal = 0 #Normalizes the per block freq to 0
    for character in cipherText: # Char is temp variable, this loop default loops every character in a string value length, and returns the chr value individually each loop to the new var
        if character in LETTERS: #the value of chr is assigned each loop, but before it overwrites, we check if its within the LETTERS string, if so, +1 to that location
            letterCount[character]+=1 
            letterTotal += 1
    freq = {} #blank dictonary, copying the chr and a modified frequency total by lettertotal
    for letter in LETTERS:
        if letterTotal > 0:
            freq[letter] = round((letterCount[letter] / letterTotal) * 100,3)
        else:
            freq[letter] = 0
    return freq, letterCount, letterTotal
  ##this def does a few things, here my logic, We need to count the total number of occurences of that the chr in the ciphertext, and store them in an array, incrementing its
  #value, as it loops through each character of the ciphertext, the for __ in __: junction takes apart the string value of cipherText, and outputs it one by one into this new variable every instance until the end of str length
  #the if operator STORES the new value into another array, otherwise character gets overwritten each time, but still outputs the value of the str for the length of the word as its loop counter
  #the if statement uses another IN to check if that newly assigned char from the string ciphertext exists within this other string, checking its membership, if it does, + 1,
  #the next statement calculates this new frequency of characters in a blank array, letter is just a temp iterator, in again specifies the 26 loop length of LETTERS, it calculates each freqency
  #by denoting the first starting character, like letter starts 0, freq[letter] = 'A': 0, and we set it equal to, the letterCount[letter] arrays position of 'A': 5, or whatever count it is
  #but then before it stores the value, divides it by the total letter total, and multiplies it by 100, and rounds by 3 decimal places, giving a new frequency for the freq{} dictonary

def main():
    cipherText = input("Enter ciphertext for the vigrenre cipher: ").upper()
    cipherText = ''.join(filter(str.isalpha, cipherText)) #filtering punctuation, removing spaces, and changing all the characters to Upper case
    keyLength = int(input("Enter key length: "))
 # its non intuitive, that given IE pos 0 and you want to get the position N characters further in the string repeating to create groups, an obvious method exists
 # if you take the entire ciphertext length. and use the keylength with the modulous operator. it creates a very nice repeating loop, appending the corresponding characters to the correct group
 # using mod, with ie keyL 10, 1 mod 10 = 1, 2 mod 10 = 2... and repeats, 11 mod 10 = 1 again, 12 mod 10 = 2, very cleaver

    columns = [''] * keyLength # this creates an empty string array, to store the new groups 
    for i, char in enumerate(cipherText): # the enumerate function adds a number to the object being stored, making it a tuple, because we need to preform freq analsys on certain elements in this array
        columns[i % keyLength] += char
    freq, count, total = getLetterCount(cipherText)
    print(freq, count, total)



 

if __name__ == "__main__":
    main()