# how to print subarray of array

array = [ 1 , 3, 4, 5 ,6 ,7]

n = len(array)

for st in range(n):
    for en in range(st , n):
        subarray = array[st:en +1]
        print(subarray)

