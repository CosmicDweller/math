from collections import deque
import numpy as np
import re

initial_text = input('Input: ')
rotor_1_setting = int(input('Rotor 1 setting (1-26): '))
rotor_2_setting = int(input('Rotor 2 setting (1-26): '))
rotor_3_setting = int(input('Rotor 3 setting (1-26): '))

sanatized_input = re.sub('[^a-zA-Z\s]', '', initial_text.upper())

alphabet = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

plugboard = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])

reflector = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

rotor_1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
rotor_2 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
rotor_3 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])

rotor_1 = np.roll(rotor_1, rotor_1_setting)
rotor_2 = np.roll(rotor_2, rotor_2_setting)
rotor_3 = np.roll(rotor_3, rotor_3_setting)

np.random.shuffle(plugboard)


# print(alphabet[rotor_1[rotor_2[rotor_3[rotor_2[rotor_1[5]]]]]])

code = ''
num = 0

for i in sanatized_input:
    if num % 26 == 0:
        rotor_2 = np.roll(rotor_2, 1)
    for j in range(len(alphabet)):
        if i == alphabet[j]:
            print(plugboard[rotor_1[rotor_2[rotor_3[reflector[rotor_3[rotor_2[rotor_1[plugboard[j]]]]]]]]])
            print(alphabet[plugboard[rotor_1[rotor_2[rotor_3[reflector[rotor_3[rotor_2[rotor_1[plugboard[j]]]]]]]]]])
    rotor_1 = np.roll(rotor_1, 1)
    num += 1

            
