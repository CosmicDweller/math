import numpy as np
import re

input = input('Input: ')

sanatized_input = re.sub('[^a-z]', '',input.upper())

alphabet = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

plugboard = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

np.random.shuffle(plugboard)

code = ''

for i in sanatized_input:
    for j in range(len(alphabet)):
        if i == alphabet[j]:
            code += plugboard[j]
            print(plugboard[j])

print(code)

