#!/usr/bin/env python3

# Maximum algorithm
# By: revpmin
# LICENSE GNU/GPL

data = [1.0, 3.14, 6.2, 0.1, 5.3]

maximum = -99999.99

for x in data:
    if x > maximum:
        maximum = x

print(maximum)
