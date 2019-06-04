# -*- coding: utf-8 -*-

sentence=input("Write a sentence, please: ")
wordlist=sentence.split()
wordlist.sort()
for x in wordlist:
    print(x)
