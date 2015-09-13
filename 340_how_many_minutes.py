#!/usr/bin/python3

# This problem is http://yukicoder.me/problems/340

first_line  = input()
second_line = input()
completed_rate  = int(first_line)
minutes         = int(second_line)

# print(int(100 / (100 - completed_rate) * minutes))
print(int(100 * minutes / (100 - completed_rate)))
