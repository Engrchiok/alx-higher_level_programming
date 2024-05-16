#!/usr/bin/python3
num = int(ord('a'))
while num <= int(ord('z')):
    if chr(num) == 'q' or chr(num) == 'e':
        num += 1
        continue
    print("{}".format(chr(num)),  end="")
    num += 1
