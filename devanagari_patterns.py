# -*- coding: utf-8 -*-

def create_word_pattern_hindi(word):

    consonants = [\
        'क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ', 'ट', 'ठ', \
        'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न', 'ऩ', 'प', 'फ', 'ब', \
        'भ', 'म', 'य', 'र', 'ऱ', 'ल', 'ळ', 'ऴ', 'व', 'श', 'ष', 'स', 'ह']
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
    maatras = ['a', 'e', 'i', 'o', 'u', 'y']

    word_buffer = ""

    #Latin Capital Letter V: u"\u0056"
    #Combining Macron: u"\u0304"

    for letter in word:
        if letter in consonants:
            word_buffer = word_buffer + 'C'
        elif letter in vowels:
            word_buffer = word_buffer + 'V'
        elif letter in maatras:
            word_buffer = word_buffer + 'v'
        else:
            word_buffer = word_buffer + letter

    return word_buffer

# CALL:
pattern = create_word_pattern_hindi('शहर')
print(pattern)
#print create_word_patterns(cleaned_content)