# Start with Pair Sum:

# Input: [1, 2, 4, 5, 7, 10] and target = 12
# Write code to find if such a pair exists.

array = [1, 2, 4, 5, 7, 10]
target = 12
l = 0
r = len(array) - 1 

while( l < r ):
        if array[l] + array[r] == target:
            print([array[l] , array[r]])
            break
        elif array[l] + array[r] < target:
            l += 1
        else:
            r -=1
