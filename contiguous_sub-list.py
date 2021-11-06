#ls = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#ls = [3, -2, 5, -1]
#ls = [-2, -3, 4, -1, -2, 1, 5, -3]
ls = [1, -3, 2, 1]


# Look for all positive contiguous sub-lists
def contiguous(ls):
    max_sum = 0
    max_current = 0
    output = list()
    # pointers to find the sublist elements
    start = 0
    end = 0

    for i in range(0, len(ls)):
        max_current += ls[i]  # Add the element to the current maximum
        if(max_sum < max_current):  # if the max sublist is < the current maximum, update the end pointer and max sublist
            end = i
            max_sum = max_current
        if(max_current < 0):  # if the current maximum is < 0, set current sublist to 0 (reset)
            max_current = 0
            # Might cause an error but im too lazy to check
            start = i + 1
    
    if max_sum <= 0:
        return None

    # Add elements to the sublist
    for i in range(start, end+1):
        output.append(ls[i])
    print("The sum of the maximum contiguous sub-list is " + str(max_sum))
    return output

print(contiguous(ls))
        
# Kadane's algorithm
# O(n) time complexity

    
