
def twoStrings(s1, s2):
    flag = False
    for x in s1:
        if x in s2:
            flag = True
    if flag == True:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    q = 2
    text = [("hello", "world"), ("hello", "cat")]
    for q_itr in range(q):
        s1 = text[q_itr][0]
        s2 = text[q_itr][1]

        result = twoStrings(s1, s2)
        print(result)





# import math
# import os
# import random
# import re
# import sys
#
#
#
# if __name__ == '__main__':
#     t = int(input().strip())
#
#     for t_itr in range(t):
#         s = input()
#
#         p = input()
#
#         q = int(input().strip())
#
#         for q_itr in range(q):
#             first_multiple_input = input().rstrip().split()
#
#             x = int(first_multiple_input[0])
#
#             c = first_multiple_input[1][0]
