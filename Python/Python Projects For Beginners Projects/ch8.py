# the binary search algorithm and its implementation
def binarySearch(aList, num):
    # set a base case for the evaluation
    if not aList:
        return False
    
    # sort the list in ascending order
    aList.sort()

    mid = len(aList) // 2 # floor division

    if (aList[mid]) == num:
        return True
    elif aList[mid] > num:
        return binarySearch(aList[:mid], num)
    else:
        return binarySearch(aList[mid + 1: ], num)
    
def main():
    listTest = [56,78,34,24,67,21,56,3,732,52,2,562,26,4,6,23,24,54,24,642,134,53]
    print(binarySearch(listTest, 2))
    
if __name__ == "__main__":
    main()