#!/usr/bin/env python3

# Minimum Algorithm
# By: revpmin
# LICENSE GNU/GPL

import sys

data = [1.0, 3.14, 6.2, 5.3, 0.1]

minimum = sys.float_info.max

for x in data:
    if x < minimum:
        minimum = x

print(minimum)
