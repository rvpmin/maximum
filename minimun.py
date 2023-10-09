#!/usr/bin/env python3

# Minimum Algorithm
# By: revpmin
# LICENSE GNU/GPL

data = [1.0, 3.14, 0.6, 5.3, 0.1]

minimum = 999999.99

for x in data:
    if x < minimum:
        minimum = x

print(minimum)
