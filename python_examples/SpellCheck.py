#!/usr/bin/python3

def stripWords():
    with open("/usr/share/dict/words", "r") as words:
        wordList = words.read().splitlines()
    words.close()
    return wordList

def spellCheck(test, dictionary):
    return True if test in dictionary else False

def test():
    words = stripWords()
    print("Checking apple: " + str(spellCheck("apple", words)))
    print("Checking kite: " + str(spellCheck("kite", words)))
    print("Checking zebra: " + str(spellCheck("zebra", words)))
    print("Checking abra: " + str(spellCheck("abra", words)))

test()
