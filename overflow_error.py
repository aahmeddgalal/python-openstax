# An overflow error occurs when a value is too large to be stored. The maximum and minimum floating-point values that can be represented are and , respectively. Attempting to store a floatingpoint value outside the range leads to an overflow error.

# Below, and can be represented, but is too large and causes an overflow error.

# print(3.0**512 < 1.8*10**308) # True
# print('3.0 to the power of 256 =', 3.0**256)
# print('3.0 to the power of 1024 = ', 3.0**1024)

# python overflow_error.py
# 3.0 to the power of 256 = 1.3900845237714473e+122
# Traceback(most recent call last):
#   File "D:\myWork\Galileo100\codes\python-openstax\overflow_error.py", line 5, in <module >
#   print('3.0 to the power of 1024 = ', 3.0**1024)
#   ~~~ ^ ^~~~~
# OverflowError: (34, 'Result too large')

print(round(0.1, 1))