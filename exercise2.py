matrix = [[6,-5,-7,4,-4],
          [-9,3,-6,5,2],
          [-10,4,7,-6,3],
          [-8,9,-3,3,-7]]

def brute_force(matrix, column, row):
    max_sum = -10000
    current_sum = 0
    left, right = 0,0

    for y1 in range(row):
        for x1 in range(column):
            for y2 in range(right, row):
                for x2 in range(left, column):
                    current_sum += matrix[y2][x2]
                    if max_sum < current_sum:
                        max_sum = current_sum
            left += 1
        right += 1
            
    return max_sum

print(brute_force(matrix, 5, 4))
