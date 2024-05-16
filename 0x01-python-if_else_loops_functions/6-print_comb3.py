#!/usr/bin/python3
count1 = 0
while count1 < 9:
    count2 = count1 + 1
    if count2 == 9 and count1 == 9 - 1:
        break
    while count2 <= 9 and count2 > count1:
        print("{}{}, ".format(count1, count2), end='')
        count2 += 1
    count1 += 1
print("{}{}".format(count1, count2))
