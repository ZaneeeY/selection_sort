'''
Author: Zheng Yu(Zane)
Student ID: 31839746
This file contains a function that sorts a list of numbers in ascending order, an example
explanation of the application of the function and other common examples.
'''

def selection_sort(aList):
    """
    Input: A disordered list of numbers
    Output: List of numbers sorted in ascending order
    """
    for index in range(len(aList)-1):# Traverse the list
        minPos = index
        for curPos in range(index+1,len(aList)): # Iterate through the list after index to find minimum index
            if aList[curPos] < aList[minPos]:# Compare the size of the numbers represented by minPos and curPos
                minPos = curPos # Update new minimum index
                aList[minPos],aList[index] = aList[index],aList[minPos] # Swap aList[minPos] and aList[index]
    return aList


if __name__ == "__main__":
    #An example:
    print(selection_sort([2, 4, 3, 1]))
    """
    Explain selection_sort([2, 4, 3, 1]) function:
    for index in range(3) -----index = 0
        minPos = 0
        for curPos in range(1, 4) ----- curPos = 1
            if aList[1]<aList[0] ----- 4<2? => False, then skip.
        for curPos in range(1, 4) ----- curPos = 2
            if aList[2]<aList[0] ----- 3<2? => False, then skip.
        for curPos in range(1, 4) ----- curPos = 3
            if aList[3]<aList[0] ----- 1<2? => True, then minPos = 3 and swap the 0th and 3rd numbers in the list.
            Thus, aList becomes [1, 4, 3, 2].
    for index in range(3) ----- index = 1
        minPos = 1
        for curPos in range(2, 4) ----- curPos = 2
            if aList[2]<aList[1] ----- 3<4? => True, then minPos = 2 and swap the 1th and 2nd numbers in the list.
            Thus, aList becomes [1, 3, 4, 2].
        for curPos in range(2, 4) ----- curPos = 3
            if aList[3]<aList[1] ----- 2<4? => True, then minPos = 3 and swap the 1th and 3rd numbers in the list.
            Thus, aList becomes [1, 2, 4, 3].
    for index in range(3) ----- index = 2
        minPos = 2
        for curPos in range(3, 4) ----- curPos = 3
            if aList[3]<aList[2] ----- 3<4? => True, then minPos = 3 and swap the 2nd and 3rd numbers in the list.
            Thus, aList becomes [1, 2, 3, 4].   
    """
    #Other examples:
    print(selection_sort([200, 14, 0, -1]))
    print(selection_sort([21, -4, 99,24, 43, 21]))
