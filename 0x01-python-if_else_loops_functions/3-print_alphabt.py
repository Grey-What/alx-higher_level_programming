#!/usr/bin/python3
# prints ASCII alphabet, in lowercase, not followed by newline, except q and e

for letter in range(97, 123):
    if chr(letter) == 'q' or chr(letter) == 'e':
        continue
    print(chr(letter).format(letter), end='')
