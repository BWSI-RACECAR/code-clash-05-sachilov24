
Code Clash #5
Ali Qattan
•
08:59
100 points
Due 23:59

Sign in to GitHub · GitHub
https://classroom.github.com/a/DyJvQ2o7

morse.py
Text
Class comments
Your work
Assigned
Private comments
Assignment details
"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #5 - Morse Code Encryption(morse.py)


Author: Andrew Scott White

Difficulty Level: 4/10

Prompt:Sam is trying to communicate with his friend Alfie using Morse Code, but he
is tired of manually encrypting the messages. He has asked you to create a Python 
script that converts messages to Morse code and vice versa. Sam’s Morse Code key is attached below. 

Note: There is one space between characters and two spaces between words in Morse Code
Hints: 	i) You can convert a message to uppercase using  message.upper()
	ii) You can remove leading/trailing whitespace from text using text.strip()
 
 
Morse Code Key:

'A':'.-', 
'B':'-...',            
'C':'-.-.', 
'D':'-..', 
'E':'.',                    
'F':'..-.', 
'G':'--.', 
'H':'....',                    
'I':'..', 
'J':'.---', 
'K':'-.-',                    
'L':'.-..', 
'M':'--', 
'N':'-.',                    
'O':'---', 
'P':'.--.', 
'Q':'--.-',                    
'R':'.-.', 
'S':'...', 
'T':'-',                    
'U':'..-', 
'V':'...-', 
'W':'.--',                   
'X':'-..-', 
'Y':'-.--', 
'Z':'--..', 


'.':'.-.-.-',                    
'?':'..--..', 
‘!’:’-.-.--’,

'1':'.----', 
'2':'..---', 
'3':'...--',                    
'4':'....-', 
'5':'.....', 
'6':'-....',                    
'7':'--...', 
'8':'---..', 
'9':'----.',                    
'0':'-----', 

'/':'-..-.', 
'-':'-....-',         
'(':'-.--.', 
')':'-.--.-'


Test Cases:
Input: SOS Output: ...---...


Input: Hello! Output: .... . .-.. .-.. --- -.-.--


Input: HUNTER2 Output: .... ..- -. - . .-. ..---
"""


##########################################################################
# MORSE DICTIONARY
##########################################################################

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', '.':'.-.-.-', '?':'..--..', '!':'-.-.--', 
                    '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}


##########################################################################
# Function to encrypt the string
# according to MORSE_CODE_DICT
##########################################################################

class Solution:
    def encrypt(message):
        cipher = ''
        for letter in message:
            if letter !='':

                cipher += MORSE_CODE_DICT[letter] +''
            else:
                cipher +=''
 
        return cipher

def main():
     str1=input()
     tc1= Solution()
     ans=tc1.encrypt(str1)
     print(ans)

if __name__ == '__main__':
    main()
