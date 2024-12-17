# Basic Patterns

# 1. Square Pattern

n = int(input("Enter the number n : "))

for i in range(n):
    print( "*" * n)

# output
# *****
# *****
# *****
# *****
# *****

# 2. Inverted Right-Angled Triangle

n = int(input("Enter the number n : "))

for i in range(n):
    print( "1" * n)
    n = n -1

#output

# 11111
# 1111
# 111
# 11
# 1

# 3.Right-Angled Triangle

n = int(input("Enter the number n : "))

for i in range(n):
    print( "1" * n)
    n = n +1

# output

# 1111111111
# 11111111111
# 111111111111
# 1111111111111
# 11111111111111
# 111111111111111
# 1111111111111111
# 11111111111111111
# 111111111111111111
# 1111111111111111111

# 4.pyramid pattern

n = 4
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

#output
#    *
#   ***
#  *****
# *******