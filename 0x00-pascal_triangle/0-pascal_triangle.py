#!/usr/bin/python3
'''Pascal's Triangle'''


def pascal_triangle(n):
    '''Return a list of integers representing pascal's principle'''
    if n <= 0:
        return []
    list1 = []
    for i in range(n):
        temp_list = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(list1[i - 1][j - 1] + list1[i - 1][j])
        list1.append(temp_list)
    return list1
