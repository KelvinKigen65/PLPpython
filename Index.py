#!/usr/bin/python
my_list = []
my_list.extend([10, 20, 30, 40])
my_list.insert(1, 15)
my_list.extend([50, 60, 70])
my_list.pop(-1)
my_list.sort()
print(my_list[3])