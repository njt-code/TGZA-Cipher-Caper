#this module attacks the key, checking if its an english word as a key
import itertools, re
import detectEnglish, VigreneteDecrypt, FrequencyOfMsg, detectEnglish
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
maxKeyLength = 16
NUM_MOST_FREQ_LETTERS = 10
silent = False
NONLETTERS_PATTERN = re.compile('[^A-Z]')


def main():
    ciphertext = input('Input Ciphertext: ')
    hackedMessage = VIGHACK(ciphertext)
    if hackedMessage != None:
        print("Hacked Message: ", hackedMessage)
    else:
        print("Failed to hack: ")


def hackVigenereDictionary(ciphertext):
    #This is a dictonary attack for the KEY only, 
    fo = open('dictonary.txt')
    words = fo.readlines()
    fo.close()
    for word in words:
        word = word.strip()
        decryptedMessage = VigreneteDecrypt.Decrypt(word,ciphertext)
        if detectEnglish.isEnglish(decryptedMessage, wordPercentage=40):
            print('\nPossible Encryption Break:')
            print('Key ' + str(word) + ': ' + decryptedMessage[:200])
            print('\nEnter D for done, or just Enter to continue breaking:')
            response = input('> ')
            if response.upper().startswith('D'):
                return decryptedMessage


def findRepeatSequenceSpacings(message):
    message = NONLETTERS_PATTERN.sub('',message.upper())

    seqSpacings = {}
    for seqLen in range(3,6):
        for seqStart in range(len(message) - seqLen):
            seq = message[seqStart:seqStart + seqLen]
            for i in range(seqStart + seqLen, len(message) - seqLen):
                if message[i:i + seqLen] == seq:
                    if seq not in seqSpacings:
                        seqSpacings[seq] = []
                    seqSpacings[seq].append(i - seqStart)
    return seqSpacings


def getUsefulFactors(num):
    if num < 2:
        return []
    factors = []
    for i in range(2, maxKeyLength + 1):
        if num % i == 0:
            factors.append(i)
            otherFactor = int(num / i)
            if otherFactor < maxKeyLength + 1 and otherFactor != 1:
                factors.append(otherFactor)
    return list(set(factors))


def getMostCommonFactors(seqFactors):
    factorCounts = {}
    for seq in seqFactors:
        factorList = seqFactors[seq]
        for factor in factorList:
            if factor not in factorCounts:
                factorCounts[factor] = 0
            factorCounts[factor] += 1
    factorsByCount = []
    for factor in factorCounts:
        if factor <= maxKeyLength:
            factorsByCount.append((factor, factorCounts[factor]))
    factorsByCount.sort(key=getItemAtIndexOne, reverse=True)
    return factorsByCount


def getItemAtIndexOne(items):
    return items[1]


def kasikiExamination(ciphertext):
    ciphertext = ''.join(filter(str.isalpha,ciphertext.upper()))
    repeatedSeqSpacings = findRepeatSequenceSpacings(ciphertext)
    seqFactors = {}
    for seq in repeatedSeqSpacings:
        seqFactors[seq] = []
        for spacing in repeatedSeqSpacings[seq]:
            seqFactors[seq].extend(getUsefulFactors(spacing))
    factorsByCount = getMostCommonFactors(seqFactors)
    allLikelyKeyLengths = []
    for twoIntTuple in factorsByCount:
        allLikelyKeyLengths.append(twoIntTuple[0])
    return allLikelyKeyLengths


def getNthSubkey(nth, keyLength, message):
    message = NONLETTERS_PATTERN.sub('',message)
    i = nth - 1
    letters = []
    while i < len(message):
        letters.append(message[i])
        i += keyLength
    return ''.join(letters)


def attemptHackWithKeyLength(ciphertext, mostLikelyKeyLenth,maxAttempt= None,printEvery=2000):
    
    
    ciphertextUp = ciphertext.upper()
    allFreqScores = []
    


    for nth in range(1, mostLikelyKeyLenth + 1):
        nthLetters = getNthSubkey(nth, mostLikelyKeyLenth, ciphertextUp)
        freqScores = []
        for possibleKey in LETTERS:
            decryptedText = VigreneteDecrypt.Decrypt(possibleKey, nthLetters)
            keyAndFreqMatchTuple = (possibleKey, FrequencyOfMsg.frequencyCorrelation(decryptedText))
            freqScores.append(keyAndFreqMatchTuple)
        freqScores.sort(key=getItemAtIndexOne, reverse = True)
        allFreqScores.append(freqScores[:NUM_MOST_FREQ_LETTERS])


  
    attemptCount = 0


    if not silent:
        for i in range(len(allFreqScores)):
            print('Possible letters frequency matches for letter %s of key: ' % (i + 1), end='')
            for freqScore in allFreqScores[i]:
                print('%s ' % freqScore[0], end='')
                print()


    for indexes in itertools.product(range(NUM_MOST_FREQ_LETTERS), repeat=mostLikelyKeyLenth):
        possibleKey = ''
        for i in range(mostLikelyKeyLenth):
            possibleKey += allFreqScores[i][indexes[i]][0]
        attemptCount += 1
        if not silent and attemptCount % printEvery == 0:
            print('Attempt %s, out of %s' % (attemptCount, (NUM_MOST_FREQ_LETTERS ** mostLikelyKeyLenth)))

        decryptedText = VigreneteDecrypt.Decrypt(ciphertextUp, possibleKey)

        if detectEnglish.isEnglish(decryptedText):
            originalTest = []
            for i in range(len(ciphertext)):
                if ciphertext[i].isupper():
                    originalTest.append(decryptedText[i].upper())
                else:
                    originalTest.append(decryptedText[i].lower())
            decryptedText = ''.join(originalTest)
            
            print('Possible key %s: ' % (possibleKey))
            print(decryptedText[:200])
            print('Enter D if done, anything else continue: ')
            response = input('> ')
            if response.strip().upper().startswith('D'):
                return decryptedText
        if maxAttempt is not None and attemptCount >= maxAttempt:
            if not silent:
                print('Reached max guesses',maxAttempt)
                break
    return None


def VIGHACK(ciphertext):
    allLikelyKeyLengths = kasikiExamination(ciphertext)
    print('Kasiki detected KeyLenghts: ',allLikelyKeyLengths)
    if not silent:
        keyLengthStr = ''
        for keyLength in allLikelyKeyLengths:
            keyLengthStr += '%s ' % (keyLength)
        print('kasiki Exam estimates: ' + keyLengthStr)
    hackedMsg = None
    for keyLength in allLikelyKeyLengths:
        if not silent:
            print('attempting with keylength %s (%s possible keys)...' % (keyLength, NUM_MOST_FREQ_LETTERS ** keyLength))
            hackedMsg = attemptHackWithKeyLength(ciphertext, keyLength)
        if hackedMsg != None:
            break
    if hackedMsg == None:
        if not silent:
            print('Unable to find keylength, brute forcing time it is...')
        for keyLength in range(1, maxKeyLength + 1):
            if keyLength not in allLikelyKeyLengths:
                if not silent:
                    print('attempting guess with key length %s (%s possible keys)...' % (keyLength, NUM_MOST_FREQ_LETTERS ** keyLength))
                hackedMsg = attemptHackWithKeyLength(ciphertext, keyLength)
                if hackedMsg != None:
                    break
    return hackedMsg
if __name__ == '__main__':
    main()