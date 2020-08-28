#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = "marcornett, received help from JT, Joseph, and Daniel"

from morse_dict import MORSE_2_ASCII
import re
# stuff = '1100110011'
# splt_word = re.split('(0+)', stuff)
# print(splt_word)


def decode_bits(bits):
    split_bits = re.split('(0+)', bits)
    split_bits = list(filter(None, split_bits))
    if '0' in split_bits[0]:
        split_bits.pop(0)
    if '0' in split_bits[-1]:
        split_bits.pop()

    multiplier = min(split_bits, key=len)
    morse_list = []

    for bit in split_bits:
        if len(bit) == len(multiplier) and bit[0] == '1':
            morse_list.append('.')
        elif len(bit) == len(multiplier) * 3 and bit[0] == '1':
            morse_list.append('-')
        elif len(bit) == len(multiplier) * 3 and bit[0] == '0':
            morse_list.append(' ')
        elif len(bit) == len(multiplier) * 7 and bit[0] == '0':
            morse_list.append('   ')
    return ''.join(morse_list)


def decode_morse(morse):
    morse_words = morse.split('  ')
    letter_str = ''
    for word in morse_words:
        for letter in word.split(' '):
            if letter in MORSE_2_ASCII:
                letter_str += MORSE_2_ASCII.get(letter)
            elif letter == '':
                letter_str += ' '
    return letter_str.strip()


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "11001100110011000000110000001111110011001111110011111100000000000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"  # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
