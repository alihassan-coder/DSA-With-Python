# Original List
my_list = [4, 3, 5]

# 1. sort()
print("1. sort()")
my_list.sort()
print("Sorted list:", my_list)  # Output: [3, 4, 5]

# ------------------------------------------------

# 2. clear()
print("\n2. clear()")
my_list = [1, 2, 3]
my_list.clear()
print("Cleared list:", my_list)  # Output: []

# ------------------------------------------------

# 3. append()
print("\n3. append(4)")
my_list = [1, 2, 3]
my_list.append(4)
print("After append:", my_list)  # Output: [1, 2, 3, 4]

# ------------------------------------------------

# 4. count()
print("\n4. count(1)")
my_list = [1, 1, 1, 2]
count = my_list.count(1)
print("Count of 1:", count)  # Output: 3

# ------------------------------------------------

# 5. extend()
print("\n5. extend([4])")
my_list = [1, 2, 3]
my_list.extend([4])
print("After extend:", my_list)  # Output: [1, 2, 3, 4]

# ------------------------------------------------

# 6. insert()
print("\n6. insert(3, 4)")
my_list = [1, 2, 3]
my_list.insert(3, 4)
print("After insert:", my_list)  # Output: [1, 2, 3, 4]

# ------------------------------------------------

# 7. index()
print("\n7. index(2)")
my_list = [1, 2, 3]
index = my_list.index(2)
print("Index of 2:", index)  # Output: 1

# ------------------------------------------------

# 8. remove()
print("\n8. remove(2)")
my_list = [1, 2, 3]
my_list.remove(2)
print("After remove:", my_list)  # Output: [1, 3]

# ------------------------------------------------

# 9. pop()
print("\n9. pop(2)")
my_list = [1, 2, 3]
my_list.pop(2)
print("After pop:", my_list)  # Output: [1, 2]

# ------------------------------------------------

# 10. reverse()
print("\n10. reverse()")
my_list = [1, 2, 3]
my_list.reverse()
print("After reverse:", my_list)  # Output: [3, 2, 1]

# ------------------------------------------------

# 11. copy()
print("\n11. copy()")
my_list = [1, 2, 3]
copied_list = my_list.copy()
print("Copied list:", copied_list)  # Output: [1, 2, 3]

# ------------------------------------------------

# 12. len()
print("\n12. len()")
my_list = [1, 2, 3]
print("Length of list:", len(my_list))  # Output: 3

# ------------------------------------------------

# 13. min()
print("\n13. min()")
my_list = [1, 2, 3]
print("Minimum value:", min(my_list))  # Output: 1

# ------------------------------------------------

# 14. max()
print("\n14. max()")
my_list = [1, 2, 3]
print("Maximum value:", max(my_list))  # Output: 3

# ------------------------------------------------

# 15. del (Error if list is already empty)
print("\n15. del")
my_list = [1, 2, 3]
del my_list
try:
    print(my_list)  # This will raise an error since my_list is deleted
except NameError as e:
    print("Error:", e)


