print("Hello world")

from random import randint
import array as arr
# First, generate random alphabets
## step 1. Make two arrays of alphabets, one is for consonants, the other is for vowels
vowels=arr.array('u', ['a' ,'e' ,'i' ,'o' ,'u' ,'y'])
consonants=arr.array('u',['b','c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'])

''' to check result of step 1.
for index in range(len(vowels)):
    print(vowels[index])

for index in range(len(consonants)):
    print(consonants[index])
'''

#Second, Input your word , if user inputs "quit!", then end this program

#Third, Figure out wheter your input word is existed in Dictionary or not