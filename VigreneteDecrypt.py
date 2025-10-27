#This program uses frequency analysis of english characters, along with key-length, to break the vigrenete cipher. or get as close to plain english as possible
#The idea is you compare the two frequency distributions, and shift/guess the letter to the corresponding peak, E of 12.7 here, most common letter, will have the 
#highest peak in the new distribution
from collections import Counter
from errno import ENFILE
engFreq = {
     'A': 8.2,'B': 1.5,  'C' : 2.8,  'D' : 4.3 , 'E' : 12.7, 'F' : 2.2, 'G' : 2.0, 'H' : 6.1,
     'I' : 7.0, 'J' : 0.15, 'K' : 0.77,  'L' : 4.0, 'M' : 2.4, 'N' : 6.7, 'O' : 7.5, 'P' : 1.9,
     'Q' : 0.095, 'R' : 6.0 , 'S' : 6.3, 'T' : 9.1, 'U' : 2.8, 'V' : 0.98, 'W' : 2.4, 'X' : 0.15,
     'Y' : 2.0, 'Z' : 0.074 
}
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
engWords = { 'the','be','to','of','and','a','in','that','have','I',
    'it','for','not','on','with','he','as','you','do','at',
    'this','but','his','by','from','they','we','say','her','she',
    'or','an','will','my','one','all','would','there','their','what',
    'so','up','out','if','about','who','get','which','go','me',
    'when','make','can','like','time','no','just','him','know','take',
    'people','into','year','your','good','some','could','them','see','other',
    'than','then','now','look','only','come','its','over','think','also',
    'back','after','use','two','how','our','work','first','well','way',
    'even','new','want','because','any','these','give','day','most','us','once'
    }
BIGRAMS = {
    'th': 3.56, 'he': 3.07, 'in': 2.43, 'er': 2.05, 'an': 1.99,
    're': 1.85, 'on': 1.76, 'at': 1.49, 'en': 1.45, 'nd': 1.35,
    'ti': 1.34, 'es': 1.34, 'or': 1.28, 'te': 1.20, 'of': 1.17,
    'ed': 1.17, 'is': 1.13, 'it': 1.12, 'al': 1.09, 'ar': 1.07,
    'st': 1.05, 'to': 1.05, 'nt': 1.04, 'ng': 0.95, 'se': 0.93,
    'ha': 0.93, 'as': 0.87, 'ou': 0.87, 'io': 0.83, 'le': 0.83,
    've': 0.83, 'co': 0.79, 'me': 0.79, 'de': 0.76, 'hi': 0.76,
    'ri': 0.73, 'ro': 0.73, 'ic': 0.70, 'ne': 0.69, 'ea': 0.69,
    'ra': 0.69, 'ce': 0.65
    }
TRIGRAMS = {
    'THE': 1.81, 'AND': 0.73, 'ING': 0.72, 'ENT': 0.42, 'ION': 0.42,
    'HER': 0.36, 'FOR': 0.34, 'THA': 0.33, 'NTH': 0.33, 'INT': 0.32,
    'ERE': 0.31, 'TIO': 0.31, 'TER': 0.30, 'EST': 0.28, 'ERS': 0.28,
    'ATI': 0.26, 'HAT': 0.26, 'ATE': 0.25, 'ALL': 0.25, 'ETH': 0.24,
    'HES': 0.24, 'VER': 0.24, 'HIS': 0.24, 'OFT': 0.22, 'ITH': 0.21,
    'FTH': 0.21, 'STH': 0.21, 'OTH': 0.21, 'RES': 0.21, 'ONT': 0.20
    }
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

def getChiValue(columnFreq, columnLength):
    BShift = 0
    BChi = float('inf') #I am not good at implementing statistical math analysis, This function is basically a black box to me, I dont understand statistics yet, all I know is 
    #that this will return a chi-value or closeness to two different frequencies, and the more its off, the less likely it will be, and the loop at the bottom is calculating the chi value of each column 26 times, and whichever chivalue is lower, is the new best chi value, 
    #and whichever letter being shifted by ie Shift, whichever shift produced the lowest chi value is returned as the likely key shift int
    
    for shift in range(26):
        chi = 0
        for letter_column in range(26):
            shiftLetter = LETTERS[letter_column]

            preShiftLetterColumn = (letter_column - shift) % 26
            originLetter = LETTERS[preShiftLetterColumn]

            expectedEngFreq = (engFreq[originLetter] / 100) * columnLength

            observedEngFreq = (columnFreq[shiftLetter] / 100) * columnLength
            if expectedEngFreq > 0:
                chi += ((observedEngFreq - expectedEngFreq) ** 2) / expectedEngFreq
        if chi < BChi:
            BChi = chi
            BShift = shift
    return BShift
def Decrypt(cipherText, finalKey):
    #Shifts the ciphertext by the Final Key value, the First guess chi key, its slightly off 
    plainText = []
    keyL = len(finalKey) 
    for i, char in enumerate(cipherText): #Traveres the entire length of the ciphertext string
        if char in LETTERS: # checks if the chr is within the letters string
            keyChar = finalKey[i % keyL] #These blocks right here, cause the aches to implement, the goal is taking the new final key, and applying the shift to the ciphertext, to get plaintext
            shift = LETTERS.index(keyChar) # index takes the number from that position
            tempInd = (LETTERS.index(char) - shift) % 26
            plainText.append(LETTERS[tempInd])
        else:
            plainText.append(char)
    return ''.join(plainText)

def englishComparison(plainText): #scores it, Higher values means closer to english, highest score
    score = 0
    text = plainText.upper()

    words = text.split()
    for word in words:
        clean = ''.join(filter(str.isalpha,word))
        if clean in engWords:
            score += len(clean) * 10
    for i in range(len(text) - 1):
        bigram = text[i:i+2]
        if bigram in BIGRAMS:
            score += BIGRAMS[bigram] * 5
    for i in range(len(text) - 2):
        trigram = text[i:i+3]
        if trigram in TRIGRAMS:
            score += TRIGRAMS[trigram] * 10
    freq,_,total = getLetterCount(text)
    if total > 0:
        for letter in LETTERS:
            exp = engFreq[letter]
            act = freq[letter]
            diff = abs(exp - act)
            score +=(10 - diff) * 0.5
    return score #Highest score is most likely, and is chosen for the closensss to bi, tri, and 100 common english words, the chi value is ALWAYS GOING TO BE THE HIGHEST SCORE INITIALLY, this just ranks the output plaintext for its englishness
        

def keyVariationToEng(finalKey, cipherText): #final key is the CHI guessed key, with CHI being closeness to original frequency, cipherText 
    #is the original input, this is using the base decrypt function, which shifts it based on the chi key, and instead tests a bunch of variations in the key by shifting -3 to 3, just arbitrary
    # shifting them all again to something more would be not using the chi, and instead brute forcing the entire ciphertext, this does far fewer tests, hard capped 50
    #it by english
    #and

    bestKey = finalKey
    bestScore = englishComparison(Decrypt(cipherText, finalKey))

    print('-'*5 + "KEY VARIATION CHECK" + '-'*5)
    print('\nInitial Chi Key:', finalKey, '\nInitial Score: ',bestScore)
    if bestScore < 100:
        print("\nScores of > 150, mean that the outputted plaintext is less close to english ")
    else: 
        print("\nHigher scores of > 150, Usually mean its close to english")
    for i in range(len(finalKey)):
        OGChar = finalKey[i]
        OGIndex = LETTERS.index(OGChar)
        for diff in range(-3,4):
         
            testIndex = (OGIndex + diff) % 26
            testChar = LETTERS[testIndex]
            testKey = finalKey[:i] + testChar + finalKey[i+1:]

            testDecrypt = Decrypt(cipherText, testKey)
            score = englishComparison(testDecrypt)
            if score > bestScore:
                bestScore = score
                bestKey = testKey
    return bestKey, bestScore

def getBestKeyDecrypt(finalKey,cipherText):
    bestKey, bestScore = keyVariationToEng(finalKey, cipherText)
    bestDecrypt = Decrypt(cipherText, bestKey)
    print('Best Key: ', bestKey, 'Best Score: ',bestScore)
    print('Best Decryption: ', bestDecrypt)
    return bestKey, bestDecrypt



def main():
    #Main input
    cipherText = input("Enter ciphertext for the vigrenre cipher: ").upper()
    cipherText = ''.join(filter(str.isalpha, cipherText)) #filtering punctuation, removing spaces, and changing all the characters to Upper case
    keyLength = int(input("Enter key length: "))
 
    #Seperating ciphertext by keylength columns, IE OMICRON PERCY I EIGHT, with keylength 4 -> IIORET, ECPYG, OREIH, MNCI. for the entire length of the ciphertext, IN THEORY, these blocks while short
    #in this example, display english like character frequencies, and you then just shift PER block/column until the frequency is akin to english, and that appended in a loop produces the plainText
    columns = [''] * keyLength 
    for i, char in enumerate(cipherText): #separates the ciphertext into keylength spaced columns
        columns[i % keyLength] += char

    finalKey = ''
    for i, column in enumerate(columns):
        columnFreq, columnCount, columnTotal = getLetterCount(column)#calls the frequency function, getting a frequency per column, then putting each freq, the CHI value function per amount of blocks
        columnLength = len(column)

        bestShift = getChiValue(columnFreq, columnLength)#calls the chi value function, which generates a predicted Shift value IE +7, +10 etc, based on the lowest chi value
        keyLetter = LETTERS[bestShift] # the best shift character is added from the chr location on the LETTERS string, when accessed like a dictonary, it already segments each of the values into a array location
        finalKey += keyLetter           # IE if the chi value is low for a block shift of A -> D, like the Best key shift of that is 4, appends location 4 in the letters array, to the final key.
        print("Column: " + str(i+1) + ', length = ' + str(columnLength) + ', Guessed KeyLetter = ' + str(keyLetter))

    plainText = Decrypt(cipherText, finalKey) #calls the decrypt function which shifts the ciphertext by the shift

    print('\nGuessed Plain: ' + plainText + '\nGuessed Chi Key: ' + finalKey) #is the chi guess, with smaller samples, can be wrong, made a veriance checker which is called next

    bestKey, bestDecrypt = getBestKeyDecrypt(finalKey, cipherText) # 

    print('\nScored Guess Key:', bestKey, '\nBest PlainText: ', bestDecrypt)

    



if __name__ == "__main__": #This is to stop the code from running when its imported into a program, and only will invoke the script when called upon manually
    main()