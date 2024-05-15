#!/usr/bin/python3
num = int(ord('a'))
while num <= int(ord('z')):
    print("{}".format(chr(num)),  end="")
    num += 1

