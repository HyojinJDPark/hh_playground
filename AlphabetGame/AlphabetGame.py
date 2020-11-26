print("Hello world")

from random import randint
import array as arr
# First, generate random alphabets
## step 1. Make two arrays of alphabets, one is for consonants, the other is for vowels
## step 2. choose two words from vowels, choose five words from consonants and show them inorderly.
vowels=arr.array('u', ['a' ,'e' ,'i' ,'o' ,'u' ,'y'])
consonants=arr.array('u',['b','c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'])

''' to check result of step 1.
for index in range(len(vowels)):
    print(vowels[index])

for index in range(len(consonants)):
    print(consonants[index])
'''
random_vowels=arr.array('u',[])
for _ in range(2):
    index=randint(0,len(vowels)-1)
    random_vowels.append(vowels[index])

random_consonants=arr.array('u',[])
for _ in range(5):
    index=randint(0,len(consonants)-1)
    random_consonants.append(consonants[index])

''' to check result of step 2.
print(random_vowels)
print(random_consonants)
'''
for index in range(2):
    print(random_vowels[index] , end=" ")
for index in range(5):
    print(random_consonants[index],end=" ")
print() #to add new line

#Second, Input your word , if user inputs "quit!", then end this program
##step 1. Input any words, with keyboard.
##step 2. make a loop until user input "quit!"

your_word="" # initialize value

while True :
    your_word=input("input your word : ")
    if your_word == "quit!" :
        exit("Bye")
    break
    
print("This is your word :",your_word)

#Third, Figure out wheter your input word is existed in Dictionary or not
##step 1. find dictionary package "pip install PyDictionary" ref) https://pypi.org/project/PyDictionary/#description
##step 2. import PyDictionary library
from PyDictionary import PyDictionary