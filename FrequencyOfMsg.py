ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#ported this from the old vigernere Cipher
def getLetterCount(cipherText):
    letterCount = {ch: 0 for ch in LETTERS} #Blank table of Str A-Z set to 0, didnt know but on stack exchange for dictonaries like this, you can actually run for loops inside defs

    for character in cipherText.upper(): 
        if character in LETTERS: 
            letterCount[character]+=1 

    return letterCount


def indexAtZero(item):
    return item[0]


def freqOrder(message):
    lettersToFreq = getLetterCount(message)
    freqToLetter = {}

    for letter in LETTERS:
        if lettersToFreq[letter] not in freqToLetter:
            freqToLetter[lettersToFreq[letter]] = [letter]
        else:
            freqToLetter[lettersToFreq[letter]].append(letter)

    for freq in freqToLetter:
        freqToLetter[freq].sort(key=ETAOIN.find, reverse = True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])
    freqPairs = list(freqToLetter.items())
    freqPairs.sort(key=indexAtZero, reverse = True)

    freqOrder = []
    for freqPair in freqPairs:
        freqOrder.append(freqPair[1])
    return ''.join(freqOrder)


def EngMatchScore(message):
    frequencyOrder = freqOrder(message)
    matchScore = 0

    for commonLetter in ETAOIN[:8]:
        if commonLetter in frequencyOrder[:8]:
            matchScore += 1

    for uncommonLetter in ETAOIN[-8:]:
        if uncommonLetter in frequencyOrder[-8:]:
            matchScore += 1

    return matchScore
def frequencyCorrelation(message):
    englishFreq = [
        0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
        0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
        0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
        0.00978, 0.02360, 0.00150, 0.01974, 0.00074
    ]
    message = message.upper()
    letterCount = getLetterCount(message)
    totalLetters = sum(letterCount.values())
    if totalLetters == 0:
        return 0

    correlation = 0

    for i, letter in enumerate(LETTERS):
        observedFreq = letterCount[letter] / totalLetters
        correlation += observedFreq * englishFreq[i]
    return correlation