# TGZA-Cipher-Caper

Dependancies 



INSTRUCTIONS:

1. Ensure python is installed if already installed, open cmd: python -v, run exit to return to cmd, if not installed navigate to https://www.python.org/downloads
2. Ensure pip is installed, comes native with python: pip --version, if does not return anything, or says not found, but you have python installed, try python -m pip --version, to run it as a python command, if again not found, refer to step 1

USAGE:

Enter the given cipherText, Enter the key-length, Gives Chi guessed key, and guessed initial plaintext, and then also checks variations of the key +-3, and scores the other variations. if no other variation has a higher score, the chi wins.


Uses frequency analysis to guess the correct shift based on lowest chi value from the frequency of the columns