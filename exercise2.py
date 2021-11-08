matrix = [[6,-5,-7,4,-4],
          [-9,3,-6,5,2],
          [-10,4,7,-6,3],
          [-8,9,-3,3,-7]]

def brute_force(matrix, column, row):
    max_sum = -10000
    current_sum = 0
    max_left = 0
    max_right = 0
    max_up = 0
    max_down = 0
    left, right = 0,1
    temp = []
    for r in range(row):
        temp.append(0)

    for i in range(row):
        for x1 in range(left,right):
            for y1 in range(row):
                temp[y1] += matrix[y1][x1]
            right += 1 
            current_sum = 0
            for j in range(len(temp)):
                current_sum += temp[j]
                if(max_sum < current_sum):
                    max_sum = current_sum
                    max_down = y1
                if(current_sum < 0):
                    current_sum = 0
                    max_up = y1           

    return max_sum

print(brute_force(matrix, 5, 4))
