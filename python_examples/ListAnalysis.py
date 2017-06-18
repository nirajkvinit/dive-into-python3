#!/usr/bin/python3

from random import randrange as rand

def randomArray():
    nums = []
    for i in range(1000):
        nums.append(rand(0, 10))
    return nums

"""
biggest: Returns the biggest number in a sorted list.
"""
def biggest(list):
    return list[ len(list) - 1 ]

"""
smallest: Returns the smallest number in a sorted list.
"""
def smallest(list):
    return list[0]
"""
mean: Returns the mean of the list
"""
def mean(list):
    return( sum(int(i) for i in list) ) / len(list)

"""
median: Returns the median of the list
"""
def median(list):
    return list[int(len(list)/2)]

"""
mode: Returns the mode of the list.
"""
def mode(list):
    mode = {}
    for num in list:
        #if mode.has_key(num):
        if num in mode:
            mode[num] += 1
        else:
            mode[num] = 1

    foundKey = -1

    for key in mode:
        if mode[key] > foundKey:
            foundKey = key
    return key

def main():
    randomList = randomArray()
    randomList.sort()

    noDuplicates = list(set(randomList))
    big = biggest(noDuplicates)
    small = smallest(noDuplicates)
    average = mean(randomList)
    middle = median(randomList)
    most = mode(randomList)

    print("Biggest: " + str(big))
    print("Smallest: " + str(small))
    print("Mean: " + str(average))
    print("Median: " + str(middle))
    print("Mode: " + str(most))

main()
